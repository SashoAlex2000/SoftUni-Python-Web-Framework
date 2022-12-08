from django.urls import path

from practice_to_do_app.accounts.views import SignInView, SignUpView, SignOutView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', SignOutView.as_view(), name='logout'),
)