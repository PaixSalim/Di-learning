from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import EnregistreUser

# Create your views here.
def home(request):
    if request.method == 'POST':
    
        fm = EnregistreUser(request.POST)
        if fm.is_valid() :
            usm= fm.cleaned_data['username']
            nm = fm.cleaned_data['name']
            pm = fm.cleaned_data['number']
            reg = User(name = nm, number = pm, username=usm )
            reg.save()
            fm = EnregistreUser()
            messages.success(request, 'Information du Utilisateur enregistré  avec succès')
            return redirect('home')
             
    else :
        fm = EnregistreUser()
    return render(request,'home.html', {'form':fm})
