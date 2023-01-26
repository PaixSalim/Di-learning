from django import forms
from .models import *


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
        
class EnregistreChambre(forms.ModelForm):
    class Meta:
        model = chambre
        fields =   '__all__'
      
        
class ModifierLoc(forms.ModelForm):
    class Meta:
        model = location
        fields = ['date_retour', 'cout', 'statu']
        widgets = {
            'date_retour' : forms.TextInput(attrs = {'class': "form-control"}),
            'cout' :forms.TextInput(attrs = {'class': "form-control"}),
            'statu' : forms.TextInput(attrs = {'class': "form-control", 'placeholder':'veuillez remplacer False par OK'})
        }
    
