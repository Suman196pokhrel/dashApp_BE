from pydantic import BaseModel, EmailStr, conint, Field
from datetime import datetime
from typing import Optional
from datetime import date
from sqlalchemy.sql.sqltypes import TIMESTAMP


class User(BaseModel):
    fName:str
    lName:str
    email:str



class LoginCredentials(BaseModel):
    email:str
    password:str

class NEW_USER(User):
    dob:date
    mobileNum: str
    password:str


class UserOut(BaseModel):
    id: int
    fName:str
    lName:str
    email: str
    

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int
    fName:str
    lName:str
    email: str


class ForGotPw(BaseModel):
    mode:str
    email:str
    mobileNum:str

class ForGotMobile(BaseModel):
    mode:str
    email:str
    mobile:str


class OTPVALIDATE(BaseModel):
    value:str
    password:str
    mode:str
    identifier:str


class RESETPASS(BaseModel):
    password:str





