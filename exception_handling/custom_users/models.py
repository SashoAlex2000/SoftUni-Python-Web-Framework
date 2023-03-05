from django.db import models


# Create your models here.

class CustomUser(models.Model):
    MAX_NAME_LENGTH = 255
    MAX_PASS_LENGTH = 255
    MAX_PROFILE_LINK_LENGTH = 255

    email = models.EmailField(
        unique=True,
    )

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    password = models.CharField(
        max_length=MAX_PASS_LENGTH,
    )

    profile_link_url = models.CharField(
        max_length=MAX_PROFILE_LINK_LENGTH,
    )
