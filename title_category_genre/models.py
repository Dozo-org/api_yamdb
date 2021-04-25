from django.db import models
from django.db.models import UniqueConstraint


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        UniqueConstraint(fields=['slug'], name="unique_field")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        UniqueConstraint(fields=['slug'], name="unique_field")  
        
    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='genres')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='categories', blank=True,
                                 null=True)
    rating = models.FloatField()
    
    class Meta:
        ordering = ['year']

    def __str__(self):
        return self.name
