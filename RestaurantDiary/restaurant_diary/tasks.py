from django_q.tasks import async_task
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse


def send_password_reset_email(user_id):
    from django.contrib.auth.models import User
    user = User.objects.get(pk=user_id)

    # Generate the reset link
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})

    # Construct and send the email
    subject = 'Password Reset'
    message = f'Click the following link to reset your password:\n\n{reset_url}'
    from_email = 'yourapp@example.com'
    to_email = [user.email]

    send_mail(subject, message, from_email, to_email)
