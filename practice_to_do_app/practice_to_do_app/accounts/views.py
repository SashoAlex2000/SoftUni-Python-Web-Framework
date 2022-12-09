from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from practice_to_do_app.accounts.forms import UserCreateForm
from practice_to_do_app.to_do_app.models import Task

# Create your views here.
UserProfile = get_user_model()


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


class ProfileDetailView(views.DetailView):
    model = UserProfile

    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['username'] = UserProfile.objects.filter(pk=self.request.user.pk).get()
        context['task_count'] = self.object.task_set.count()
        print(UserProfile)
        print(context)
        return context


class FinishedTasksListView(views.ListView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    model = Task

    template_name = 'accounts/finished.html'


