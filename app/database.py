from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.database_hostname}:{settings.database_port}/{settings.POSTGRES_DB}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker( autoflush=False, bind=engine)

Base= declarative_base()



# Dependency to handle database connection 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
