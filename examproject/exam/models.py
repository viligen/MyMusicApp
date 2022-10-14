from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from examproject.core.validators import validate_chars_username


# Create your models here.


class Profile(models.Model):
    MAX_LEN_USERNAME = 15
    MIN_LEN_USERNAME = 2

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            MinLengthValidator(MIN_LEN_USERNAME),
            validate_chars_username,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Item(models.Model):

    MAX_LEN = 30
    GENRES = ["Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", "Other"]
    CHOICES = tuple([(c, c) for c in GENRES])

    album_name = models.CharField(
        max_length=MAX_LEN,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Album Name'
    )
    artist = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,

        choices=CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        ),
        null=False,
        blank=False,

    )