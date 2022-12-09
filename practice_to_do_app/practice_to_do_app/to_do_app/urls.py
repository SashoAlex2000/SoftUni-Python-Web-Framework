from django.urls import path

from practice_to_do_app.to_do_app.views import index, about_view, TasksListView, TaskDetailView, add_task, edit_task, \
    TasksSearchListView, task_completed, TasksSearchForRealListView

urlpatterns = (
    path('', index, name='index'),
    path('about/', about_view, name='about'),
    path('catalog/', TasksListView.as_view(), name='catalog'),
    path('create/', add_task, name='create task'),
    path('catalog/<int:pk>', TaskDetailView.as_view(), name='details'),
    path('catalog/<int:pk>/complete', task_completed, name='complete task'),
    path('catalog/<int:pk>/edit', edit_task, name='edit task'),
    path('catalog/<slug:urgency>', TasksSearchListView.as_view(), name='filter by urgency'),
    path('search/', TasksSearchForRealListView.as_view(), name="search"),
)

