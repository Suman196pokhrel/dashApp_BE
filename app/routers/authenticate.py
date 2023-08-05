from fastapi import APIRouter, Depends, HTTPException, status
from ..database import get_db, engine
from ..schemas.authSchemas import NEW_USER
from sqlalchemy.orm import Session
from ..models import authModel
from sqlalchemy.exc import IntegrityError
from ..schemas.authSchemas import LoginCredentials
from ..utils.dependencies import get_hash

router = APIRouter()


@router.post("/login")
def login(loginForm:LoginCredentials, db: Session = Depends(get_db)):
    
    user = db.query(authModel.User).filter(authModel.User.email == loginForm.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong Credentials")
    
    
    else:
        
        # return token
        return {
            "message":"Login SuccessFul"
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



@router.get("/{id}")
def get_user(id:int, db:Session= Depends(get_db)):


    user = db.query(authModel.User).filter(authModel.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")

    else:
        return {
            "message":"User found sucessfully",
            "user_info":user
        }