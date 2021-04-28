from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'
    MODERATOR = 'moderator'

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(max_length=9, choices=UserRole.choices,
                            default=UserRole.USER)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.CharField(max_length=254, blank=True)
    confirmation_code = models.CharField(max_length=30, blank=True)

    @property
    def is_admin(self):
        return (self.is_staff or self.role == UserRole.ADMIN)

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR
