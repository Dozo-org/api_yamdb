from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from title_category_genre.models import Title



class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='review',
    )
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='review',
    )
    score = models.IntegerField(
        default=5, 
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        'Дата отзыва',
        auto_now_add=True,
    )

    def __str__(self):
        return self.text[:20]

class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comment',
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True, 
        db_index=True,
    )
