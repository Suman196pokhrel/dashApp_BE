import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ..settings import settings
import random
import string
import httpx
from datetime import datetime, timedelta
from twilio.rest import Client






def calculate_otp_expiry(expires_after=5):
    current_time = datetime.utcnow()
    expiry_time = current_time + timedelta(minutes=expires_after)
    return expiry_time

def calculate_otp_expiry(expires_after=5):
    current_time = datetime.utcnow()
    expiry_time = current_time + timedelta(minutes=expires_after)
    return expiry_time



async def send_otp_mobile(recipient_detail):

    client = Client(settings.twilio_acc_sid,settings.twilio_auth_token)
    
     # Generate a random OTP
    otp = ''.join(random.choices(string.digits, k=6)) 
    try:
        # Send SMS with OTP
        message =  client.messages.create(
            body=f"Your DashApp verification code is {otp}. This OTP will expire in {settings.otp_expires_minutes} minutes.",
            # from_=settings.verified_number,
            from_=settings.twilio_phone_number,
            to=recipient_detail
        )
        return {"status":True, "otp":otp,"expires_at":calculate_otp_expiry(settings.otp_expires_minutes)}
    except Exception as e:
        print(e)
        return {"status":False, "message":str(e)}





