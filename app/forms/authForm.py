from django import forms
from django.forms import widgets


class ConnectionForm(forms.Form):
    username = forms.CharField(max_length=200, widget=widgets.Input(attrs={'placeholder' : 'Votre nom'}))
    password = forms.CharField(max_length=200, widget=widgets.PasswordInput(attrs={'placeholder' : 'Votre mot de passe'}))

    def clean_username(self):
        return self.cleaned_data['username']