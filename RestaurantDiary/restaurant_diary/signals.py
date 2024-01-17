from django.db.models.signals import Signal, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_q.tasks import async_task
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

password_reset_signal = Signal()


@receiver(post_save, sender=User)
def user_post_save(sender, instance, **kwargs):
    if instance.created:
        password_reset_signal.send(sender=instance.__class__, user=instance)
