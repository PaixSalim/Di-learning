from django import forms
from .models import client


class EnregistreUser(forms.ModelForm):
    class Meta:
        model = client
        fields = ['nom', 'prenom', 'adresse', 'email', 'ville', 'pays']
        widgets = {
            'nom' :forms.TextInput(attrs = {'class': "form-control"}),
            'prenom' : forms.TextInput(attrs = {'class': "form-control"}),
            'adresse' :forms.TextInput(attrs = {'class': "form-control"}),
            'email' : forms.TextInput(attrs = {'class': "form-control"}),
            'ville' : forms.TextInput(attrs = {'class': "form-control"}),
            'pays' : forms.TextInput(attrs = {'class': "form-control"}),
        }