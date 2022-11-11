from django.core import validators
from django.db import models

# Create your models here.



class Employee(models.Model):

    first_name = models.CharField(
        max_length=30
    )

    last_name = models.CharField(
        max_length=30
    )

    age = models.IntegerField(
        validators=[
            validators.MinValueValidator(18),
        ]
    )

    position = models.CharField(
        max_length=30,

        choices=(
            ('JUNIOR', 'Junior'),
            ('MID', 'MID'),
            ('Senior', 'Senior'),
        )
    )
