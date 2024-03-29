"""exception_handling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from custom_users.exception_handler import page_not_found
from custom_users.views import handler500 as global500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("custom_users.urls")),
]

# NOTHING WORKED --- because of DEBUG=True ?? YES
handler404 = page_not_found
handler500 = global500
# handler500 = 'custom_users.views.handler500'
# handler500 = 'custom_users.views.second_handler_500'
# handler500 = 'custom_users.views.custom_error_view'
# ^ the string representation is not preferable, since it may not pick up changes down the road,
# better with function reference
