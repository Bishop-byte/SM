import smtplib
from config import EMAIL_SETTINGS
from email.mime.text import MIMEText

def send_alert_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SETTINGS['sender_email']
    msg['To'] = EMAIL_SETTINGS['receiver_email']

    with smtplib.SMTP(EMAIL_SETTINGS['smtp_server'], EMAIL_SETTINGS['port']) as server:
        server.starttls()
        server.login(EMAIL_SETTINGS['sender_email'], EMAIL_SETTINGS['password'])
        server.send_message(msg)