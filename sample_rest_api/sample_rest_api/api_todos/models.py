from django.db import models


# Create your models here.


class Category(models.Model):
    MAX_CATEGORY_LENGTH = 15

    name = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )


class Todo(models.Model):
    MAX_TITLE_LENGTH = 30
    DEFAULT_TODO_STATE = False

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        default=DEFAULT_TODO_STATE,
        null=False,
        blank=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
    )
