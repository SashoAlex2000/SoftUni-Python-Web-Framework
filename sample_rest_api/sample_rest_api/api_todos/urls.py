from django.urls import path

from sample_rest_api.api_todos.views import ListCreateTodoApiView

urlpatterns = (
    path('', ListCreateTodoApiView.as_view(), name="api list todos"),
)

