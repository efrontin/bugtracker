from django import forms
from django.forms import widgets, ModelChoiceField

from app.models import Project, Company


class CompaniesChoiceFieldStr(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class ProjectForm(forms.Form):
    company = CompaniesChoiceFieldStr(
        queryset=Company.objects.all(),
        to_field_name="name",
        empty_label=None,
        label="Entreprises",
        widget=widgets.Select(
            attrs={'class': 'form-control', 'placeholder': 'Nom'}
        )
    )
    name = forms.CharField(label='Le nom de votre entreprise',
                           max_length=200,
                           widget=widgets.Input(
                               attrs={'placeholder': 'Nom de votre projet'})
                           )

    class Meta:
        model = Project
