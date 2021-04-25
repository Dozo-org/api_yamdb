from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    class UserRole:
        USER = 'user'
        ADMIN = 'admin'
        MODERATOR = 'moderator'
        choices = [
            (USER, 'user'),
            (ADMIN, 'admin'),
            (MODERATOR, 'moderator'),
        ]

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(max_length=9, choices=UserRole.choices,
                            default=UserRole.USER)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.CharField(max_length=254, blank=True)
    confirmation_code = models.CharField(max_length=30, blank=True)
