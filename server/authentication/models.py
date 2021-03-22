from django.db.models import EmailField, DateTimeField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = EmailField(blank=False, null=False, unique=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
