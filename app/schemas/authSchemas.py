from pydantic import BaseModel
from datetime import date


class NEW_USER(BaseModel):
    fName:str
    lName:str
    email:str
    dob:date
    mobileNum: str
    password:str