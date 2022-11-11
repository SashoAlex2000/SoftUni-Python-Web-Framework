import random

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic as views

from class_base_views.web.models import Employee

from django import forms


# Create your views here.

class IndexView:
    def __init__(self):
        self.value = random.randint(1, 100)

    @classmethod  # factory method
    def get_view(cls):
        instance = cls()
        the_view = instance.view
        print(the_view)

        return the_view

    def view(self, request):
        return HttpResponse(f'It works: {self.value}')


class SecondTestView(IndexView):

    def get_random_num(self):
        return random.randint(1, 100)

    def view(self, request):
        context = {
            'value1': self.get_random_num(),
            'value2': self.get_random_num(),
            'value3': self.get_random_num(),
            'value4': self.get_random_num(),
        }

        return render(
            request,
            'test.html',
            context,
        )


class IndexClassView(views.View):

    def get(self, requst):
        return HttpResponse('It works from Class Based View Inherited from views')


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'template.html'  # for static context

    extra_context = {
        'title': 'Template view!'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['employees'] = Employee.objects.all()

        return context


class IndexViewWithListView(views.ListView):
    model = Employee

    template_name = 'list_view.html'

    context_object_name = 'employees'  # this could be skipped, Django automatically names it object_list,
    # we just have to use it as such in the template

    extra_context = {
        'title': 'List view'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        valid_fields = [field.name for field in self.model._meta.fields]
        pattern = self.__get_pattern()
        sort_criteria = self.__get_sorting_param()
        print(valid_fields)
        print(sort_criteria)
        if sort_criteria and (sort_criteria in valid_fields or sort_criteria == 'pk'):
            queryset = queryset.order_by(sort_criteria)
        else:
            queryset = queryset.order_by('first_name')

        if pattern:
            # queryset = queryset.order_by('first_name')
            queryset = queryset.filter(first_name__icontains=pattern.lower())

        return queryset

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)

    def __get_sorting_param(self):
        return self.request.GET.get('sorting', None)


class EmployeeDetailView(views.DetailView):
    context_object_name = 'employee'

    model = Employee

    template_name = 'details.html'


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your name here: ',
                }
            )
        }


class EmployeeCreateView(views.CreateView):
    template_name = 'create_employee.html'
    model = Employee
    fields = '__all__'

    # success_url = '/list'  # static success URL

    def get_success_url(self):
        return reverse_lazy('details view', kwargs={
            'pk': self.object.pk,
        })

    # form_class = EmployeeCreateForm # if we want a custom form we can do it here and use a model form class

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for name, field in form.fields.items():
            field.widget.attrs['placeholder'] = f'Please, enter your {name}'

        return form


class EmployeeEditView(views.UpdateView):

    success_url = '/list'  # static success URL

    template_name = 'edit_employee.html'
    model = Employee
    fields = '__all__'

