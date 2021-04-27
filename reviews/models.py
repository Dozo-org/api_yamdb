from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from title_category_genre.models import Title
from users.models import CustomUser as User


REVIEW_SCORE_ERROR_MESSAGE = 'The score value have to be between 1 and 10.'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1, message=REVIEW_SCORE_ERROR_MESSAGE),
                    MaxValueValidator(10, message=REVIEW_SCORE_ERROR_MESSAGE)]
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='Unique together relation between title and author',
            ),
        ]
        ordering = ['-pub_date', ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ['-pub_date']
