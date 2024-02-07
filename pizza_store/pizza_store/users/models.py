import secrets
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from .managers import AuthUserManager
from django.utils.translation import gettext_lazy as _
from .utils.constants import ACTIVATION_AVAILABILITY



#AuthUserModel = get_user_model()

class AuthUser(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True
    )
    password = models.CharField(_('password'), max_length=128,null=True, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email



AVAILABILITY = {
    ACTIVATION_AVAILABILITY['unit']: ACTIVATION_AVAILABILITY['value']
}

class Activation(models.Model):
    user = models.OneToOneField(
        AuthUser,
        on_delete=models.CASCADE,
        related_name='activation'
    )
    token = models.CharField(
        max_length=64,
        null=True,
        default=secrets.token_hex(32)
    )
    expires_at=models.DateTimeField(
        default=timezone.now() + timezone.timedelta(**AVAILABILITY)
    )
    activated_at = models.DateTimeField(
        default=None,
        null=True
    )

