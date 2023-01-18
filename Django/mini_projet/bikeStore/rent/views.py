from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *



# Create your views here.
def home(request):
    anim = vehicule.objects.all()
    
    
    return render(request,'index.html', {'voiture' : anim})

def locations(request):
    anima = location.objects.all()
    statu = location.objects.all()
    
    return render(request,'location.html', {'locations' : anima, 'statut':statu})

def listclient(request):
    clien = client.objects.all()
    
    return render(request,'client.html', {'clients' : clien})

def afficher(request, id):
    if request.method == 'POST':
        pi = location.objects.get(pk=id)
      
    else:
        pi = location.objects.get(pk=id)
   
    return render(request, 'afficher.html', {'info':pi})



def inscrire(request):  
    clien = client.objects.all()
    vhi = vehicule.objects.all()
    if request.method == 'POST':
        clie = request.POST['client']
        vehicul = request.POST['voiture']
        date_crea = request.POST['date_crea']
        date_ret= request.POST['date_ret']
        cout = request.POST['cout'] 
        mon_user = location( client_id_id=clie, vehicule_id_id=vehicul, date_location=date_crea, date_retour=date_ret, cout=cout)
        mon_user.save()
        messages.success(request, 'votre compte a été crée')
        return redirect('home')
   
    return render(request, 'ajouterloc.html',{'inf':clien, 'voit':vhi} )

def ajoutervehi(request): 
    clien = taille_vehicule.objects.all()
    vhi = type_vehicule.objects.all() 
    if request.method == 'POST':
        clie = request.POST['taille']
        vehicul = request.POST['type']
        date_crea = request.POST['date_crea']
        cout = request.POST['cout'] 
        mon_vehi = vehicule( taille_id_id=clie, type_vehicule_id_id=vehicul, date_creation=date_crea, cout=cout)
        mon_vehi.save()
        messages.success(request, 'Enregistrement validé')
        return redirect('home')
   
    return render(request, 'ajoutervhi.html',{'inf':clien, 'voit':vhi}  )


def ajoutercli(request):  
    if request.method == 'POST':
        nm = request.POST['nom']
        pnm = request.POST['prenom']
        adr = request.POST['adresse']
        em= request.POST['email']
        vil = request.POST['ville'] 
        pay = request.POST['pays'] 
        mon_client = client( nom=nm, prenom=pnm, adresse=adr, email=em, ville=vil, pays=pay)
        mon_client.save()
        messages.success(request, 'client enregistré avec succès')
        return redirect('home')
   
    return render(request, 'ajoutercli.html' )

def modifier(request, id):
    if request.method == 'POST':
        pi = client.objects.get(pk=id)
        fm = EnregistreUser(request.POST, instance=pi )
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Information du client modifié avec succès')
            return redirect('home')
    else:
        pi = client.objects.get(pk=id)
        fm = EnregistreUser(instance= pi)
    return render(request, 'modifier_client.html', {'form':fm})

def modifierloc(request, id):
    if request.method == 'POST':
        pi = location.objects.get(pk=id)
        fm = ModifierLoc(request.POST, instance=pi )
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Information sur la location modifié avec succès')
            return redirect('home')
    else:
        pi = location.objects.get(pk=id)
        fm = ModifierLoc(instance= pi)
    return render(request, 'modifier_loc.html', {'form':fm})


   