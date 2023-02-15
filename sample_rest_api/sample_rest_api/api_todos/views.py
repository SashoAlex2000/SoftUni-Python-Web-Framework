from django.shortcuts import render

# Create your views here.
from rest_framework import generics as rest_generic_views, serializers

from sample_rest_api.api_todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title')


class ListCreateTodoApiView(rest_generic_views.ListCreateAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
