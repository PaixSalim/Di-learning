from django import forms
from .models import User
from phonenumber_field.modelfields import PhoneNumberField


class EnregistreUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'number']
        widgets = {
            'username' :forms.TextInput(attrs = {'class': "form-control"}),
            'name' :forms.TextInput(attrs = {'class': "form-control"}),
            'number' : forms.NumberInput(attrs = {'class': "form-control"}),
        }