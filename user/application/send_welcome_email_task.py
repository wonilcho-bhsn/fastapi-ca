import smtplib
from celery import Task
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import get_settings

settings = get_settings()

class SendWelcomeEmailTask(Task):
    name = "send_welcome_email_task"
    def run(self, receiver_email:str):
        sender_email = "dexter.haan@gmail.com"
        password = "password"
        # TODO ... (send email)

