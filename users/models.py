# from django.db import models
# from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     ROLE_CHOICES = (
#         ('user', 'user'),
#         ('moderator', 'moderator'),
#         ('admin', 'admin'),
#     )
#     username = models.CharField(max_length = 30, unique=True)
#     email = models.EmailField(max_length = 254, unique=True)
#     role = models.CharField(max_length=9, choices=ROLE_CHOICES,
#                             default='user')
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     bio = models.CharField(max_length=254, blank=True)
#     confirmation_code =models.CharField(max_length=30, blank=True)

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=30, blank=True,)
    email = models.EmailField(unique=True,)

    class UserRole:
        USER = 'user'
        ADMIN = 'admin'
        MODERATOR = 'moderator'
        choices = [
            (USER, 'user'),
            (ADMIN, 'admin'),
            (MODERATOR, 'moderator'),
        ]

    role = models.CharField(max_length=9, choices=UserRole.choices,
                            default=UserRole.USER,)
    confirmation_code = models.UUIDField(default=uuid.uuid4, editable=False,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
