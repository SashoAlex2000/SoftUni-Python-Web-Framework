from django.urls import path

from class_base_views.web.views import IndexView, SecondTestView, IndexClassView, IndexViewWithTemplate, \
    IndexViewWithListView, EmployeeDetailView, EmployeeCreateView, EmployeeEditView
from django.views import generic as views


urlpatterns = (
    path('', IndexView.get_view()),
    path('test/', SecondTestView.get_view()),
    path('class/', IndexClassView.as_view()),
    path('template/', IndexViewWithTemplate.as_view(), name='template view'),
    path('create/', EmployeeCreateView.as_view(), name='create employee'),
    path('list/', IndexViewWithListView.as_view(), name='list view'),
    path('details/<int:pk>', EmployeeDetailView.as_view(), name='details view'),
    path('edit/<int:pk>', EmployeeEditView.as_view(), name='edit view'),
    path('redirect/', views.RedirectView.as_view(url='http://127.0.0.1:8000/template/')),
)

