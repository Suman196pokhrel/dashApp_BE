from ..database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    fName = Column(String, nullable=False,unique=False)
    lName = Column(String, nullable=False,unique=False)
    email= Column(String, nullable=False,unique=True)
    dob = Column(Date, nullable=False, unique=False)
    mobileNum = Column(String)
    password = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    
