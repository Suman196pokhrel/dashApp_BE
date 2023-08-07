from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    mailgun_api_url:str
    mailgun_public_api:str
    mailgun_private_api:str
    sender_email:str
    otp_expires_minutes:int
    twilio_acc_sid:str
    twilio_auth_token:str
    verify_sid:str
    verified_number:str
    recipient_number:str


    
    class Config:
        env_file=".env"


settings = Settings()
