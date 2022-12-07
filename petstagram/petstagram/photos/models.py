from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.core.model_mixins import StrFromFieldMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_less_than_5mb


# Create your models here.
UserModel = get_user_model()

class Photo(StrFromFieldMixin, models.Model):

    str_fields = ('pk','photo', 'location')

    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        # using this technique, in db, only the path to the image is saved
        # we can change it with:
        # upload_to='mediafiles/pet_photos/',
        upload_to='pet_photos/',

        null=False,
        blank=False,
        validators=(
            validate_file_less_than_5mb, # should maybe be in a list ??
        )
    )

    description = models.CharField(
        # DB postgre validation
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            # Django / pYthon validation
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,

    )

    publication_date = models.DateField(
        auto_now = True,
        null=False,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
        # null = True ?
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
