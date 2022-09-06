from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from application.database import db
from application.models import User

SMPTP_SERVER_HOST = "localhost"
SMPTP_SERVER_PORT = 1025
SENDER_ADDRESS = "iankitagupta02@gmail.com"
SENDER_PASSWORD = ""

def send_email(to_address,subject,message):
    msg =MIMEMultipart()
    msg["From"] = SENDER_ADDRESS
    msg["To"]= to_address
    msg["Subject"] = subject

    msg.attach(MIMEText(message,"html"))

    s=smtplib.SMTP(host=SMPTP_SERVER_HOST, port=SMPTP_SERVER_PORT)
    s.login(SENDER_ADDRESS,SENDER_PASSWORD)
    s.send_message(msg)
    s.quit()

    return True

def main():
    users=db.session.query(User).all
    emails=[]
    for e in users:
        emails.append(e.email)
    for email in emails:
        send_email(email,subject="Hello",message="Hello! hope you have revised today.")

if __name__ == "__main__":
    main()
