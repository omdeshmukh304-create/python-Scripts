import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "omdeshmukh304@gmail.com"
SENDER_PASSWORD = "YOUR_APP_PASSWORD"   #  Gmail App Password
RECEIVER_EMAIL = "maxdeshmukh306@gmail.com"

def send_email(subject, body):
    # Create email
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject

    # Attach body
    msg.attach(MIMEText(body, "plain"))

    # Connect to SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)

    # Send email
    server.send_message(msg)
    server.quit()