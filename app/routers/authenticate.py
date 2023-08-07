from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db, engine
from ..schemas.authSchemas import NEW_USER
from sqlalchemy.orm import Session
from ..models import authModel
from sqlalchemy.exc import IntegrityError
from ..schemas.authSchemas import LoginCredentials, UserOut, ForGotPw, OTPVALIDATE, RESETPASS
from ..utils.dependencies import get_hash, verify_hash
from ..utils.oauth2 import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..utils.oauth2 import get_current_user
from ..models.authModel import User,OTP
import random
from ..settings import settings
import httpx
import string
from ..utils.otpEmailGenerator import send_otp_email
from ..utils.otpMobileGenerator import send_otp_mobile
from datetime import datetime

router = APIRouter()


@router.post("/login")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    
    user = db.query(authModel.User).filter(authModel.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong Credentials")
    
  
    if not verify_hash(plain_password=user_credentials.password, hashed_password=user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")

    
    # Create a Sccess Tokens
    access_token = create_access_token(data={
        "user_id":user.id,
        "fName":user.fName,
        "lName":user.lName,
        "email":user.email,
        })


    return {
        "access_token":access_token,
        "token_type":"bearer"
        }




@router.post("/newUser")
def create_new_user(user:NEW_USER, db:Session=Depends(get_db)):

    # hash the password
    hashed_pw = get_hash(user.password)
    user.password = hashed_pw
    new_user = authModel.User(**user.dict())

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {
            "message":"Successfully created new user",
            "new_user" : new_user
        }

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email or Mobile Number already in use")



@router.get("/{id}", response_model=UserOut)
def get_user(id:int, db:Session= Depends(get_db),current_user = Depends(get_current_user)):


    user = db.query(authModel.User).filter(authModel.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")

    else:
        return user



@router.post("/forgotPw")
async def forgot_password(otpMode: ForGotPw, db: Session = Depends(get_db)):


    if otpMode.mode not in ['email', 'mobile']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Selected Password Reset Method Not Allowed")

    if otpMode.mode == 'email':
        recipient_field = 'email'
        send_otp_func = send_otp_email
    else:
        recipient_field = 'mobileNum'
        send_otp_func = send_otp_mobile

    recipient_value = getattr(otpMode, recipient_field)
    current_user = db.query(User).filter_by(**{recipient_field: recipient_value}).first()
    
    if not current_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    existing_otp = db.query(OTP).filter_by(user_id=current_user.id).first()
    
    otp_data = await send_otp_func(recipient_detail=recipient_value)  # Change to recipient_email or recipient_mobile accordingly

    if not otp_data['status']:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=otp_data['message'])

    hashed_otp = get_hash(otp_data['otp'])
    expires_at = otp_data['expires_at'].strftime('%Y-%m-%d %H:%M:%S.%f')

    if existing_otp:
        existing_otp.value = hashed_otp
        existing_otp.expires_at = expires_at
    else:
        new_otp_row = OTP(user_id=current_user.id, value=hashed_otp, expires_at=expires_at)
        db.add(new_otp_row)

    db.commit()
    
    return {"status": f"Successfully sent password reset {'email' if otpMode.mode == 'email' else 'sms'} to {recipient_value}"}


@router.post("/validateNewPw")
async def validate_forgotPw_otp(otp:OTPVALIDATE,db:Session=Depends(get_db)):

    current_user = db.query(User).filter_by(email=otp.email).first()

    # CHECK IF THAT USER EXISTS OR NOT 
    if current_user:

        existing_row =  db.query(OTP).filter_by(user_id=current_user.id).first() 
        


        if existing_row:
            if existing_row.user_id == current_user.id and verify_hash(otp.value, existing_row.value):
                # Check if OTP time has expired 
                expires_at = datetime.strptime(existing_row.expires_at, '%Y-%m-%d %H:%M:%S.%f')
                valid_otp = expires_at <= datetime.utcnow()
                # print("OTP VALID VALUE => ", valid_otp, expires_at, datetime.utcnow())
                if not valid_otp:

                    # Setting New User pASsword 
                    current_user.password = get_hash(otp.password)
                    db.commit()

                    # Deleting row of validated otp 
                    db.delete(existing_row)
                    db.commit()
                    return {
                    "message" : "Valid OTP"
                    }
                else:
                    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="OTP Expired")
                

            else:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong OTP")
            

        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No OTP generated")

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User with that email is not registered")

