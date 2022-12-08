from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models


# Create your models here.

class AppUser(auth_models.AbstractUser):
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 30
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
        )
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
        )
    )

    email = models.EmailField(
        unique=True,
    )
