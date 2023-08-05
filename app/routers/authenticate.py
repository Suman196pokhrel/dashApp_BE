from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db, engine
from ..schemas.authSchemas import NEW_USER
from sqlalchemy.orm import Session
from ..models import authModel
from sqlalchemy.exc import IntegrityError
from ..schemas.authSchemas import LoginCredentials, UserOut
from ..utils.dependencies import get_hash, verify_hash
from ..utils.oauth2 import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..utils.oauth2 import get_current_user
from ..models.authModel import User

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