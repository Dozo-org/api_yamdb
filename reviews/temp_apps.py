from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Title(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name

