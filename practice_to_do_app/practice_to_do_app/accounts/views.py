from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from practice_to_do_app.accounts.forms import UserCreateForm


# Create your views here.


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register.html'
    # model = UserModel
    # fields = ('username', 'password',)
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


