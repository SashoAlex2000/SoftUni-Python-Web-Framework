from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class ChoicesEnumMixin:

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Urgency(ChoicesEnumMixin, Enum):
    low = 'Low'
    medium = 'Medium'
    high = 'High'
    urgent = 'Urgent!'


class Task(models.Model):
    MAX_LENGTH_NAME = 35

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
    )

    due_date = models.DateField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    urgency_level = models.CharField(
        choices=Urgency.choices(),
        max_length=Urgency.max_len(),
        blank=False,
        null=False,
    )

    completed=models.BooleanField(
        default=False,
        blank=False,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
