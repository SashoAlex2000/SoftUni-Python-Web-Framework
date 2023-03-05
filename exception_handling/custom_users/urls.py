from django.urls import path
from custom_users.views import GetCreateUsers
urlpatterns = [
    path('users', GetCreateUsers.as_view())
]
