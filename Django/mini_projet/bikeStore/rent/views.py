from django.shortcuts import render, redirect

from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    anim = vehicule.objects.all()
    
    return render(request,'index.html', {'voiture' : anim})

def locations(request):
    anima = location.objects.all()
    
    return render(request,'location.html', {'locations' : anima})

def afficher(request, id):
    if request.method == 'POST':
        pi = location.objects.get(pk=id)
      
    else:
        pi = location.objects.get(pk=id)
   
    return render(request, 'afficher.html', {'info':pi})


def inscrire(request):   
    if request.method == 'POST':
        client = request.POST['client']
        vehicule = request.POST['voiture']
        date_crea = request.POST['date_crea']
        date_ret= request.POST['date_ret']
        cout = request.POST['cout'] 
        mon_user = location( client_id=client, vehicule_id=vehicule, date_location=date_crea, date_retoure=date_ret, cout=cout)
        mon_user.save()
        messages.success(request, 'votre compte a été crée')
        return redirect('home')
   
    return render(request, 'ajouterloc.html')


    