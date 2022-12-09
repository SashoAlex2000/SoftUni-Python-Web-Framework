from django.urls import path

from practice_to_do_app.accounts.views import SignInView, SignUpView, SignOutView, ProfileDetailView, \
    FinishedTasksListView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('<int:pk>/finished', FinishedTasksListView.as_view(), name='finished'),

)