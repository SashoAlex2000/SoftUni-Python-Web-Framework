from django.urls import path

from web_tools.web.views import index, refreshes_count_view, raise_error_view

urlpatterns = (
    path('', index, name='index'),
    path('refresher/', refreshes_count_view, name='refresher'),
    path('error/', raise_error_view, name='error view'),
)

# we have to write this in order for the signals to load
from .signals import *

