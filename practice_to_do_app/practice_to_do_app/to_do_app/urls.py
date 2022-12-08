from django.urls import path

from practice_to_do_app.to_do_app.views import index, about_view, TasksListView, TaskDetailView, add_task, edit_task

urlpatterns = (
    path('', index, name='index'),
    path('about/', about_view, name='about'),
    path('catalog/', TasksListView.as_view(), name='catalog'),
    path('create/', add_task, name='create task'),
    path('catalog/<int:pk>', TaskDetailView.as_view(), name='details'),
    path('catalog/<int:pk>/edit', edit_task, name='edit task'),
)
