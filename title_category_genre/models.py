from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=25)
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    
class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['-id']

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
    
    class Meta:
        ordering = ['year']

    def __str__(self):
        return self.name
