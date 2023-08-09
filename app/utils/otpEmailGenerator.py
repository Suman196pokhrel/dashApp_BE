import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ..settings import settings
import random
import string
import httpx
from datetime import datetime, timedelta



def calculate_otp_expiry(expires_after=5):
    current_time = datetime.utcnow()
    expiry_time = current_time + timedelta(minutes=expires_after)
    return expiry_time




async def send_otp_email(recipient_detail):
    
    # Email data
    emailSender = settings.SENDER_EMAIL  # Replace with your sender email addres
     # Generate a random OTP
    otp = ''.join(random.choices(string.digits, k=6)) 
    text =f"Here is your OTP for creating a new password: {otp}. This OTP will expire in {settings.otp_expires_minutes} minutes."
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
            settings.MAILGUN_API_URL,
                auth=("api", settings.MAILGUN_PRIVATE_API),
                data={
                    "from": emailSender,
                    "to": recipient_detail,
                    "subject": "DashApp Account Password Reset",
                    "text": text
                }
            )
            return {"status":True, "otp":otp,"expires_at":calculate_otp_expiry(settings.OTP_EXPIRES_MINUTES)}


        except Exception as e:
            return False



def calculate_otp_expiry(expires_after=5):
    current_time = datetime.utcnow()
    expiry_time = current_time + timedelta(minutes=expires_after)
    return expiry_time



