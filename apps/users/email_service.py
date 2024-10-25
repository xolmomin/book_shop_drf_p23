from time import time

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from users.tasks import send_activation_email_task


class ActivationEmailService:
    def __init__(self, user, host_url):
        self.user = user
        self.host_url = host_url
        self.token_generator = PasswordResetTokenGenerator()

    def generate_activation_link(self):
        token = self.token_generator.make_token(self.user)
        uid = urlsafe_base64_encode(force_bytes(f"{self.user.pk}/{self.user.is_active}{int(time())}"))
        return f"{self.host_url}/api/v1/users/activate/{uid}/{token}"

    def send_activation_email(self, email, first_name='Botirjon', priority=None):
        activation_link = 'valivali'
        from django.template.loader import render_to_string
        from django.utils.html import strip_tags

        subject = 'Registration'
        context = {
            'user': first_name,
            'activation_link': activation_link,
        }
        html_message = render_to_string('email.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <from@example.com>'
        to = email
        if priority == 'high':
            return send_activation_email_task.apply_async(args=[subject, plain_message, to, html_message], priority=8)
        else:
            return send_activation_email_task.apply_async(args=[subject, plain_message, to, html_message])
