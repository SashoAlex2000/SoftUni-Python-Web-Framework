from django import forms

from petstagram.core.form_mixins import DisabledFormMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Pet Name'

    class Meta:
        model = Pet
        # fields = '__all__'
        fields = ('name', 'date_of_birth', 'personal_photo',)
        # exclude = ('slug',)

        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link To Image',
            'date_of_birth': 'Date of Birth',
        }

        widgets = {
            # 'name': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Pet name',
            #     }
            # ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            ),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm, DisabledFormMixin):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance

