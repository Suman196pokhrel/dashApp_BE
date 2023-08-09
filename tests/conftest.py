# THIS FILE IF FOR FIXTURES , THE FIXTURES PRESENT IN THIS FILE WILL BE AVAILABE TO ALL THE TEST FILES WITHIN THE TEST FOLDER 
from fastapi.testclient import TestClient
from fastapi import HTTPException, status
from app.main import app
import pytest

from app.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.database import get_db, Base


# TEST DATABASE SETTING

SQLALCHEMY_TEST_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}_test"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker( autoflush=False, bind=engine)



# FIXTURES RUN BEFORE EVERY OCCOURANCE OF CLIENT KEYWORD 

@pytest.fixture(scope="module")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    
    


@pytest.fixture(scope="module")
def client(session):
    def get_test_db():
        
        try:
            yield session
        finally:
            session.close()
            
    app.dependency_overrides[get_db] = get_test_db
    yield TestClient(app)
    
    
