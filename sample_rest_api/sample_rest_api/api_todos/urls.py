from django.urls import path

from sample_rest_api.api_todos.views import ListCreateTodoApiView, ListCategoriesApiView, DetailsTodoApiView

urlpatterns = (
    path('', ListCreateTodoApiView.as_view(), name="api list todos"),
    path('<int:pk>/', DetailsTodoApiView.as_view(), name="api details todos"),
    path('categories/', ListCategoriesApiView.as_view(), name="api list categories"),
)

