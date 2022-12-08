from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from django.views import generic as views

from practice_to_do_app.to_do_app.forms import TaskEditForm, TaskCreateForm
from practice_to_do_app.to_do_app.models import Task


# Create your views here.

def index(request):
    context = {
        'user_name': request.user.username,
    }

    return render(request,
                  'index.html',
                  context
                  )


def about_view(request):
    return render(request,
                  'about.html')


class TasksListView(views.ListView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    model = Task

    template_name = 'catalog.html'


class TaskDetailView(views.DetailView):
    model = Task

    template_name = 'details.html'


@login_required
def add_task(request):
    if request.method == 'GET':
        form = TaskCreateForm
    else:
        form = TaskCreateForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)

            task.user = request.user
            task.save()

            return redirect('catalog')

    context = {
        'form': form,
    }

    return render(request,
                  'create_task.html',
                  context,
                  )


@login_required
def edit_task(request, pk):
    current_task = Task.objects.filter(pk=pk).get()
    print(current_task)

    if request.method == 'GET':
        form = TaskEditForm(instance=current_task)
    else:
        form = TaskEditForm(request.POST, instance=current_task)

        if form.is_valid():
            form.save()
            return redirect('details', pk=current_task.pk)

    context = {
        'form': form,
        'id': current_task.pk,
    }

    return render(
        request,
        'edit_task.html',
        context,
    )