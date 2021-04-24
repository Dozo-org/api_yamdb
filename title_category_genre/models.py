from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='genres')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='categories', blank=True,
                                 null=True)
    rating = models.FloatField()
