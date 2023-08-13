import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..settings import settings
from .otpEmailGenerator import calculate_otp_expiry
import random
import string

def send_email_gmail(recipient_detail):
    # Generate OTP
    otp = ''.join(random.choices(string.digits, k=6))

    subject = "DashApp Account Password Reset"
    message_body = f"Here is your OTP for creating a new password: {otp}. This OTP will expire in {settings.OTP_EXPIRES_MINUTES} minutes."

    # Create MIMEText object
    message = MIMEMultipart()
    message["From"] =  'spokhrel196@gmail.com'
    message["To"] = recipient_detail
    message["Subject"] = subject
    message.attach(MIMEText(message_body, "plain"))

    # Connect to Gmail's SMTP server
    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(settings.SMTP_EMAIL, settings.SMTP_PASSWORD)
        smtp_server.sendmail(settings.SMTP_EMAIL, recipient_detail, message.as_string())
        smtp_server.quit()

        return {
            "status": True,
            "otp": otp,
            "expires_at": calculate_otp_expiry(settings.OTP_EXPIRES_MINUTES)
        }
    except Exception as e:
        print('An error occurred:', e)
        return {"status": False}
