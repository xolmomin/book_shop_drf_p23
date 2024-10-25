import time

from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


@shared_task
def send_activation_email_task(subject, message, recipient, html_message):
    print(f"({recipient}) ga yuborish BOSHLANDI")
    time.sleep(3)
    send_mail(subject, message, EMAIL_HOST_USER, [recipient], html_message=html_message)
    time.sleep(3)
    print(f"({recipient}) ga yuborish TUGADI")
    return f"Emails sent to recipient"
