from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(
        MaxValueValidator(datetime.now().year,
                          message='Введен некорректный год'))
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='genres')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='categories', blank=True,
                                 null=True)

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return self.name
