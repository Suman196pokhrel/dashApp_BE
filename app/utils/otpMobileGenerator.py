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



async def send_otp_mobile(recipient_detail):


    print("RECIPIENT_DETAIL +> ", recipient_detail)
    client = Client(settings.TWILIO_ACC_SID,settings.TWILIO_AUTH_TOKEN)
    
     # Generate a random OTP
    otp = ''.join(random.choices(string.digits, k=6)) 
    try:
        # Send SMS with OTP
        message =  client.messages.create(
            body=f"Your DashApp verification code is {otp}. This OTP will expire in {settings.OTP_EXPIRES_MINUTES} minutes.",
            # from_=settings.verified_number,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=recipient_detail
        )
           
        
        print("TWILIO RESPONSE__++>> , ", message)
        return {"status":True, "otp":otp,"expires_at":calculate_otp_expiry(settings.OTP_EXPIRES_MINUTES)}
    except Exception as e:
        print(e)
        return {"status":False, "message":str(e)}





