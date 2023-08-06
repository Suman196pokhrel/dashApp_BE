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
    vonage_api_key:str
    vonage_api_secret:str
    vonage_sender_id:str

    
    class Config:
        env_file=".env"


settings = Settings()
