from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )
    username = models.CharField(max_length = 30, unique=True)
    email = models.EmailField(max_length = 254, unique=True)
    role = models.CharField(max_length=9, choices=ROLE_CHOICES, default='user')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.CharField(max_length=254, blank=True)
    confirmation_code =models.CharField(max_length=30, blank=True)
