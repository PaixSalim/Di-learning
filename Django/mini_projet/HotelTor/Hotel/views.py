from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *



# Create your views here.
def home(request):
    anim = chambre.objects.all()
    
    
    return render(request,'visiteur/index.html', {'voiture' : anim})








def listclient(request):
    clien = client.objects.all()
    
    return render(request,'visiteur/client.html', {'clients' : clien})

def afficher(request, id):
    if request.method == 'POST':
        pi = location.objects.get(pk=id)
      
    else:
        pi = location.objects.get(pk=id)
   
    return render(request, 'visiteur/afficher.html', {'info':pi})



def inscrire(request):  
    clien = client.objects.all()
    vhi = chambre.objects.all()
    if request.method == 'POST':
        clie = request.POST['client']
        vehicul = request.POST['voiture']
        date_crea = request.POST['date_crea']
        date_ret= request.POST['date_ret']
        cout = request.POST['cout'] 
        mon_user = location( client_id_id=clie, chambre_id_id=vehicul, date_location=date_crea, date_retour=date_ret, cout=cout)
        mon_user.save()
        messages.success(request, 'votre Location a été Enregistré avec succès')
        return redirect('home')
   
    return render(request, 'visiteur/ajouterloc.html',{'inf':clien, 'voit':vhi} )

def ajoutervehi(request): 
    vhi = client.objects.all() 
    if request.method == 'POST':
        clie = request.POST['client']
        cout = request.POST['avis'] 
        mon_vehi = avis( client_id_id=clie,  avis=cout)
        mon_vehi.save()
        messages.success(request, 'Merci pour votre commentaire')
        return redirect('home')
   
    return render(request, 'visiteur/ajoutervhi.html',{ 'voit':vhi}  )


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
   
    return render(request, 'visiteur/ajoutercli.html' )

def modifier(request, id):
    if request.method == 'POST':
        pi = client.objects.get(pk=id)
        fm = EnregistreUser(request.POST, instance=pi )
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Information du client modifié avec succès')
            return redirect('administration')
    else:
        pi = client.objects.get(pk=id)
        fm = EnregistreUser(instance= pi)
    return render(request, 'visiteur/modifier_client.html', {'form':fm})

def modifierloc(request, id):
    if request.method == 'POST':
        pi = location.objects.get(pk=id)
        fm = ModifierLoc(request.POST, instance=pi )
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Information sur la location modifié avec succès')
            return redirect('administration')
    else:
        pi = location.objects.get(pk=id)
        fm = ModifierLoc(instance= pi)
    return render(request, 'visiteur/modifier_loc.html', {'form':fm})





   