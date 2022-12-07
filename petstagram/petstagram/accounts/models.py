from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from petstagram.core.validators import validate_only_letters


# Create your models here.

# naming the custom user model has two conventions:
# generic one like AppUser OR {name_of_app}User -> PetstagramUser
# doesn't really matter, since outside this file model will be called with get_user_model()

# it should be split into two mixins in the perfect case, the second one for max. length
class ChoicesEnumMixin:

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotSHow = 'Do not show'


class AppUser(auth_models.AbstractUser):
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 30
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    # USERNAME_FIELD = 'email' <--- if we want the default login to be email
