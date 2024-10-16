from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


@shared_task
def send_activation_email_task(subject, message, recipient_list, html_message):
    for recipient in recipient_list:
        send_mail(subject, message, EMAIL_HOST_USER, [recipient], html_message=html_message)
    return f"Emails sent to {', '.join(recipient_list)}."
