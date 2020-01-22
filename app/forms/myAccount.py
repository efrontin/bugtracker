from django import forms
from django.forms import widgets, ModelChoiceField

from app.models import Company


class CompaniesChoiceFieldStr(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class MyAccount(forms.Form):
    username = forms.CharField(
        max_length=200,
        label="Nom utilisateur",
        widget=widgets.Input(
            attrs={'class': 'form-control', 'placeholder': 'Nom utilisateur'}
        )
    )
    first_name = forms.CharField(
        max_length=55,
        label="Prénom",
        widget=widgets.Input(
            attrs={'class': 'form-control', 'placeholder': 'Prénom'}
        )
    )
    last_name = forms.CharField(
        max_length=55,
        label="Nom",
        widget=widgets.Input(
            attrs={'class': 'form-control', 'placeholder': 'Nom'}
        )
    )
    companies = CompaniesChoiceFieldStr(
        queryset=Company.objects.all(),
        to_field_name="name",
        empty_label=None,
        label="Entrprises",
        widget=widgets.Select(
            attrs={'class': 'form-control', 'placeholder': 'Nom'}
        )
    )

    def clean_username(self):
        return self.cleaned_data['username']
