from django.urls import path

from rest_api_lecture.web_api.views import EmployeesListAPIView, EmployeesCreateListAPIView, DepartmentsListApiView, \
    DemoApiView

urlpatterns = (
    path('employees/', EmployeesListAPIView.as_view(), name="api list of employees"),
    path('employees/create', EmployeesCreateListAPIView.as_view(), name="api create list of employees"),
    path('departments/', DepartmentsListApiView.as_view(), name="api list departments"),
    path('demo/', DemoApiView.as_view(), name="demo view"),
)

