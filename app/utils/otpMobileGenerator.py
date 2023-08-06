import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ..settings import settings
import random
import string
import httpx
from datetime import datetime, timedelta
# from vonage import Client





# vonage_client = Client(key=settings.vonage_api_key, secret=settings.vonage_api_secret)



def calculate_otp_expiry(expires_after=5):
    current_time = datetime.utcnow()
    expiry_time = current_time + timedelta(minutes=expires_after)
    return expiry_time

def calculate_otp_expiry(expires_after=5):
    current_time = datetime.utcnow()
    expiry_time = current_time + timedelta(minutes=expires_after)
    return expiry_time



# async def send_otp_mobile(recipient_mobile):
    
#     # Email data
#     emailSender = settings.sender_email  # Replace with your sender email addres
#      # Generate a random OTP
#     otp = ''.join(random.choices(string.digits, k=6)) 

#     # Send the OTP via SMS
#     response = vonage_client.send_message({
#         "from": settings.vonage_sender_id,
#         "to": recipient_mobile,
#         "text": f"Dash App , Your OTP for generating new password is : {otp}, Remember , the otp will expire in {calculate_otp_expiry(5)} minutes"
#     })

#     if response['messages'][0]['status'] == '0':
#         return {"status": True,"otp":otp,"expires_at":calculate_otp_expiry(2)}
#     else:
#         raise HTTPException(status_code=500, detail="Failed to send OTP")




