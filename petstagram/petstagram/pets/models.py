from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

from petstagram.core.model_mixins import StrFromFieldMixin

# Create your models here.
UserModel = get_user_model()


class Pet(StrFromFieldMixin, models.Model):
    str_fields = ('id', 'name')

    MAX_NAME = 30  # since we do not have constants in Python we use conventions
    # it is good practice to all sorts of such numbers in outer constants/variables for clarity

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,  # always pass the explicitly
    )

    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,

    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    # do with init maybe ?

    def save(self, *args, **kwargs):
        # have to save first, in order to have derived an ID
        super().save(*args, **kwargs)

        # put the slug ; have to keep the if, since w/o it the url can get changed in the future, which we don't want
        if not self.slug:
            self.slug = slugify(f"{self.id}-{self.name}")

        return super().save(*args, **kwargs)

    # def __str__(self):
    #     return f'{self.id}: {self.name}'
