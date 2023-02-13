from django.urls import path

from rest_api_lecture.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name="index"),
)

