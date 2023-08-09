from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    MAILGUN_API_URL:str
    MAILGUN_PUBLIC_API:str
    MAILGUN_PRIVATE_API:str
    SENDER_EMAIL:str
    OTP_EXPIRES_MINUTES:int
    TWILIO_ACC_SID:str
    TWILIO_AUTH_TOKEN:str
    VERIFY_SID:str
    TWILIO_PHONE_NUMBER:str
    RECIPIENT_NUMBER:str
    DOCKER_HUB_ACCESS_TOKEN:str
    DOCKER_HUB_USERNAME:str


    
    class Config:
        env_file=".env"


settings = Settings()
