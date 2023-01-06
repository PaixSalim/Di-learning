from django.shortcuts import render, HttpResponseRedirect

from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html',)


def index(request):
    per = personne.objects.all()
   
    return render(request,'index.html', {'personnage':per})

def Afficher_nom(request):
    per = personne.objects.all()
    if request.method == 'POST':
        per = personne.objects.all().filter(nom=request.POST['nom'])
    
    return render(request,'index.html', {'personnage':per})


def Afficher_numero(request):
    per = personne.objects.all()
    if request.method == 'POST':
        per = personne.objects.all().filter(num=request.POST['num'])
    
    return render(request,'home.html', {'personnage':per})