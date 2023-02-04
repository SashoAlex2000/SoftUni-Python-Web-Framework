import random
import time

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from web_tools.web.models import Employee

REFRESHES_COUNT_SESSION = 'REFRESHES_COUNT_SESSION'
LATEST_VALUES_SESSION = 'LATEST_VALUES_SESSION'

UserModel = get_user_model()

random_first_names = ['ALex', 'Sasho', 'Misho', 'George', 'John', 'Test', 'Sandio', 'Tony']
random_last_names = ['Malinov', 'Cooper', 'Smith', 'Ortega', 'Bulgakov', 'Koothrappali', 'Soprano']
CURRENT_RETIREMENT_AGE = 63


# some hypothetical heavy operation, which requires a lot of computing power and time, and thus has to be cached
def some_resource_heavy_operation():
    time.sleep(1.5)
    return random.randint(1, 1024)


@cache_page(15)
def index(request):

    #creating a random Employee
    current_first_name = random_first_names[random.randint(0, len(random_first_names) - 1)]
    current_last_name = random_last_names[random.randint(0, len(random_last_names) - 1)]

    Employee.objects.create(
        first_name=current_first_name,
        last_name=current_last_name,
        age=random.randint(18, CURRENT_RETIREMENT_AGE),
    )

    value = some_resource_heavy_operation()
    latest_values = request.session.get(LATEST_VALUES_SESSION, [])
    latest_values = [value] + latest_values
    latest_values = latest_values[:3]
    request.session[LATEST_VALUES_SESSION] = latest_values

    return HttpResponse(f'Value is {value}, latest values: {", ".join([str(x) for x in latest_values])}')


def refreshes_count_view(request):
    number_of_refreshes = request.session.get(REFRESHES_COUNT_SESSION, 0) + 1
    request.session[REFRESHES_COUNT_SESSION] = number_of_refreshes

    return HttpResponse(f'Refreshed {number_of_refreshes} times')


def raise_error_view(request):
    UserModel.objects.get(pk=101010)
    return HttpResponse(f'Impossible')

