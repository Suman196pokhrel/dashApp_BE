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




async def send_otp_email(recipient_email, subject):
    
    # Email data
    emailSender = settings.sender_email  # Replace with your sender email addres
     # Generate a random OTP
    otp = ''.join(random.choices(string.digits, k=6)) 
    text =f"Here is your OTP for creating a new password: {otp}. This OTP will expire in {settings.otp_expires_minutes} minutes."
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
            settings.mailgun_api_url,
                auth=("api", settings.mailgun_private_api),
                data={
                    "from": emailSender,
                    "to": recipient_email,
                    "subject": subject,
                    "text": text
                }
            )
            return {"status":True, "otp":otp,"expires_at":calculate_otp_expiry(settings.otp_expires_minutes)}


        except Exception as e:
            return False



def calculate_otp_expiry(expires_after=5):
    current_time = datetime.utcnow()
    expiry_time = current_time + timedelta(minutes=expires_after)
    return expiry_time



