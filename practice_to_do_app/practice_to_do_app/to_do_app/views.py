from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from django.views import generic as views

from practice_to_do_app.to_do_app.forms import TaskEditForm, TaskCreateForm
from practice_to_do_app.to_do_app.models import Task

# Create your views here.

UserProfile = get_user_model()


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

    # queryset = Task.objects.filter(name__icontains='tidy')
    # queryset = Task.objects.filter(urgency_level__exact='urgent')

    def get_queryset(self):
        queryset = super().get_queryset()
        valid_fields = [field.name for field in self.model._meta.fields]
        sort_criteria = self.__get_sorting_param()
        print(valid_fields)
        print(sort_criteria)
        if sort_criteria:
            if sort_criteria == 'urgency-desc':
                queryset = queryset.order_by("-urgency_level")
            else:
                queryset = queryset.order_by("urgency_level")
        else:
            # queryset = queryset.order_by('name')
            pass

        return queryset

    def __get_sorting_param(self):
        return self.request.GET.get('sorting', None)


class TasksSearchListView(views.ListView):
    model = Task

    template_name = 'search-by-urgency.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # print(Task.objects.get(urgency_level=self.kwargs.get('slug')))
        # print(self.kwargs.get('slug'))
        current_search = self.kwargs['urgency']
        print(current_search)
        context['urgency'] = current_search
        context['current_tasks'] = Task.objects \
            .filter(user_id=self.request.user.pk) \
            .filter(urgency_level__icontains=current_search)\
            .filter(completed=False).all()
        return context


class TaskDetailView(views.DetailView):
    model = Task

    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        print(self.kwargs.get('pk'))
        print(Task.objects.get(pk=self.kwargs.get('pk')))

        print(context)

        return context


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


def task_completed(request, pk):

    current_task = Task.objects.filter(pk=pk).get()
    print(current_task.completed)
    current_task.completed = True
    print(current_task.completed)
    current_task.save()

    return redirect('index')


class TasksSearchForRealListView(views.ListView):
    model = Task

    template_name = "search.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.__get_pattern()

        print(pattern)
        print(queryset)

        if not pattern:
            return None

        queryset = queryset.filter(user_id=self.request.user.pk).filter(completed=False)

        if pattern:
            # queryset = queryset.order_by('first_name')
            queryset = queryset.filter(name__icontains=pattern.lower())

        print(queryset)
        return queryset

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)


