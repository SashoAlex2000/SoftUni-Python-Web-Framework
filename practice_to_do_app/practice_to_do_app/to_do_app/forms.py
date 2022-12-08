from django import forms

from practice_to_do_app.to_do_app.models import Task


class TaskBaseForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('completed', 'user',)

        widgets = {

            'due_date': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
        }


class TaskCreateForm(TaskBaseForm):
    pass


class TaskEditForm(TaskBaseForm):
    pass
