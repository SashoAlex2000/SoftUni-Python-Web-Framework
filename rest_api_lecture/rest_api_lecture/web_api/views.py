from django.shortcuts import render
from django.views import generic as views
from rest_framework import generics as rest_views
from rest_framework import views as rest_base_views
from rest_framework.response import Response

from rest_api_lecture.web_api.models import Employee, Department
from rest_framework import serializers

from rest_api_lecture.web_api.serializers import EmployeeSerializer, DepartmentSerializer, ShortEmployeeSerializer, \
    ShortDepartmentSerializer, DemoSerialzer
from rest_api_lecture.web_api.utils import get_most_populous_department
from rest_framework import viewsets


# Create your views here.


# SSR ; returns HTML
class EmployeesListView(views.ListView):
    model = Employee
    template_name = ''


# JSON serialization, transforms model info to JSON to send
class EmployeesListAPIView(rest_views.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # used to return employees only in a given department
    def get_queryset(self):
        department_id = self.request.query_params.get('department')
        queryset = self.queryset

        if department_id:
            queryset = queryset.filter(department_id=department_id)

        return queryset.all()


# A view to create entities in the Model via the browsable API ;
class EmployeesCreateListAPIView(rest_views.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentsListApiView(rest_views.ListAPIView):
    queryset = Department.objects.all()
    # serializer_class = ShortDepartmentSerializer
    serializer_class = DepartmentSerializer


# has the CRUD operations, alternative to Django view
class DemoApiView(rest_base_views.APIView):

    # we can return custom data, serialized, not in the built-in way
    def get(self, request):
        employees = Employee.objects.all()
        departments = Department.objects.all()
        most_pop_dep = get_most_populous_department()

        body = {
            'employees': employees,
            'employees_count': employees.count(),
            'departments': departments,
            'first_department': departments.get(id=1),
            'most_populous_department': most_pop_dep,
        }

        serializer = DemoSerialzer(body)

        # Not the HTTPResponse, but coming from DRF
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet): # < -- gives us all the CRUD operations, black magic :D
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
