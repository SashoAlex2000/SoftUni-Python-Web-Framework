from django.shortcuts import render
from django.views import generic as views
from rest_framework import generics as rest_views

from rest_api_lecture.web_api.models import Employee
from rest_framework import serializers


# Create your views here.

# What serializes the views
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


# SSR ; returns HTML
class EmployeesListView(views.ListView):
    model = Employee
    template_name = ''


# JSON serialization, transforms model info to JSON to send
class EmployeesListAPIView(rest_views.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# A view to create entities in the Model via the browsable API ;
class EmployeesCreateListAPIView(rest_views.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
