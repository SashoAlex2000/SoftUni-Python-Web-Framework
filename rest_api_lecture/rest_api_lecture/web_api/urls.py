from django.urls import path

from rest_api_lecture.web_api.views import EmployeesListAPIView, EmployeesCreateListAPIView

urlpatterns = (
    path('employees/', EmployeesListAPIView.as_view(), name="api list of employees"),
    path('employees/create', EmployeesCreateListAPIView.as_view(), name="api list of employees"),
)

