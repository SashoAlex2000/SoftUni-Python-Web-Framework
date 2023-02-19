from django.shortcuts import render

# Create your views here.
from rest_framework import generics as rest_generic_views, serializers, permissions, exceptions as rest_exceptions

from sample_rest_api.api_todos.models import Todo, Category
from sample_rest_api.api_todos.serializers import TodoForCreateSerializer, TodoForListSerializer, CategorySerializer, \
    TodoForDetailsSerializer


class ListCreateTodoApiView(rest_generic_views.ListCreateAPIView):
    queryset = Todo.objects.all()
    create_serializer_class = TodoForCreateSerializer
    list_serializer_class = TodoForListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    # a tuple of things to be filtered (depending on the request reveived) for the response
    filter_names = (
        'category',
    )

    # manages which serializer class is used based on the type of request; we can list and create from the same view
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class

        return self.create_serializer_class

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)

        return self.__apply_filters_to_queryset(queryset)

    def __apply_filters_to_queryset(self, queryset):

        query_filter_dict = {

        }

        for filter_name in self.filter_names:
            filter_id = self.request.query_params.get(filter_name, None)

            if filter_id:
                query_filter_dict[f'{filter_name}'] = filter_id

        # category_id = self.request.query_params.get('category', None)
        #
        # if category_id:
        #     queryset = queryset.filter(category_id=category_id)

        return queryset.filter(**query_filter_dict)


class DetailsTodoApiView(rest_generic_views.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoForDetailsSerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_object(self):
        object = super().get_object()

        if object.user != self.request.user:
            raise rest_exceptions.PermissionDenied

        return object


class ListCategoriesApiView(rest_generic_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self): # to avoid sending and displaying categories, which are empty
        return self.queryset.filter(todo__user_id=self.request.user.id).distinct()

