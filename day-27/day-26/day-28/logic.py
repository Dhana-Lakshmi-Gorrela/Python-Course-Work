import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.import encoders

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "dhanalakshmigorrela798@gmail.com"
SENDER_PASSWORD = "aafj etha ozss jqyx"

def send_email(to_email, subject, body, attachments=None):
  try: 
    msg = MIMEMULtipart()
    msg["From"] = SENDER_EMAIL
    msg["TO"]= to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    if attachments:
        for file_path in attachments:
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                   mime_base = MIMEBase("application", "octet-stream")
                   mime_base.set_payload(f.read())
                   encoders.encode_base64(mime_base)
                   mime_base.add_header(
                      "Content-Disposition",
                      f"attachment; filename={od.path.basename(file_path)}")
                   
                

    