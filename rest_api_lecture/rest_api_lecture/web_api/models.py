from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

MIN_STATE_SALARY = 720


def validate_min_salary(value):
    if value < MIN_STATE_SALARY:
        raise ValidationError(
            f"A worker cannot receive less than {MIN_STATE_SALARY}!"
        )


class Department(models.Model):
    def __str__(self):
        return f'{self.name}'

    DEPARTMENT_NAME_MAX_LENGTH = 30
    name = models.CharField(
        max_length=DEPARTMENT_NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )


class Employee(models.Model):
    EMPLOYEE_NAME_MAX_LENGTH = 30

    name = models.CharField(
        max_length=EMPLOYEE_NAME_MAX_LENGTH,
        blank=False,
        null=False,
    )

    salary = models.PositiveIntegerField(
        validators=[
            validate_min_salary,
        ],
        blank=False,
        null=False,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'{self.name} - {self.salary} - {self.department}'
