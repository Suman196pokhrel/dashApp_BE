from jose import JWTError, jwt
from datetime import datetime, timedelta
from ..settings import settings
from ..schemas.authSchemas import TokenData
from fastapi import Depends, status , HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from ..models.authModel import User
from sqlalchemy.orm import Session
from ..database import get_db



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")  # Provides token to getCurrentUser dependency on endpoints 
SECRET_KEY = f"{settings.SECRET_KEY}"
ALGORITHM = f"{settings.ALGORITHM}"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES




def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token:str, credentials_Exception):
    
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id:str = payload.get("user_id")

        if id is None:
            raise credentials_Exception

        token_data = TokenData(id=id,fName=payload.get("fName"),lName=payload.get("lName"),email=payload.get("email"))


    except JWTError:
        raise credentials_Exception


    return token_data
    




def get_current_user(token:str = Depends(oauth2_scheme), db:Session=Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials", headers={"WWW-Authenticate:":"Bearer"})

    token =  verify_access_token(token, credentials_exception)
    user = db.query(User).filter(User.id == token.id).first()

    return user