from collections import OrderedDict

from django import forms
from django.forms import widgets, ModelChoiceField

from app.models import Project, Company


# class CompaniesChoiceFieldStr(ModelChoiceField):
#     def label_from_instance(self, obj):
#         return obj.name


class ProjectForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        initial = kwargs.get('initial', {})

        company = forms.ChoiceField(
            choices=initial['companies_choices'],
            # to_field_name="name",
            # empty_label=None,
            label="Entreprises",
            widget=widgets.Select(
                attrs={'class': 'form-control'},
            )
        )
        name = forms.CharField(
            label='Le nom de votre projet',
            max_length=200,
            widget=widgets.Input(
                attrs={'class': 'form-control', 'placeholder': 'Nom de votre projet'})
        )
        is_client = forms.BooleanField(
            label='Client',
            widget=widgets.CheckboxInput(
                attrs={'class': 'form-check-input'}
            )
        )
        self.fields = OrderedDict([
            ('name', name),
            ('company', company),
            ('is_client', is_client),
        ])
