from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import *



# Create your views here.
def home(request):
    propri = Propriete.objects.all()
    per = Propriete.objects.all()
    if request.method == 'POST':
        per = Propriete.objects.all().filter(chambre=request.POST['villa'], ville=request.POST['ville'] )
        propri = per
    else: 
        propri = Propriete.objects.all()
        
     
    return render(request,'index.html', {'maison' : propri})

def listes(request):
    propri = Propriete.objects.all()
        
    return render(request,'listings.html',{'maison' : propri})

def about(request):
   
    
    
    return render(request,'about.html' )

def demande(request):
    avis = Contact.objects.all()
    
    
    return render(request,'avis.html', {'avis' : avis})



def deconnecter(request):
    logout(request)
    messages.success(request, 'votre compte a été deconnecté')
    return redirect('inscrire')
    
def dashboard(request):
    user_contacts= Contact.objects.filter(user_id=request.user.id)


    context ={
        'contacts':user_contacts
    }
    return render(request,'dashboard.html',context) 
    
def connecter(request):
    if request.method == 'POST':
         username = request.POST['username'],
         passwor = request.POST['password'],
         use= authenticate(username=request.POST['username'], password=request.POST['password'])
         if use is not None:
             login(request, use)
             nom = User.id
             messages.success(request, 'Vous etes connecté!!!!')
             return redirect('dashboard')
         else:
            messages.error(request,'Connection impossible')
            return redirect('connecter')
    return render(request, 'login.html')


    
def information(request, id):
    if request.method == 'POST':
        pi = Propriete.objects.get(pk=id)
        clie = request.POST['nom']
        email = request.POST['mail']
        msg = request.POST['mssg']
        z = request.POST['maiz']
        user = request.POST['user_id']
        mon_user = Contact( nom=clie, mail=email, message=msg, propriete_id_id=z, user_id=user)
        mon_user.save()
        messages.success(request, 'votre Demande a été Enregistré avec succès')        
        return redirect('home')
      
    else:
        pi = Propriete.objects.get(pk=id)
   
    return render(request, 'listing.html', {'info':pi})
   
def informatio(request, id):
    if request.method == 'POST':
        pi = Propriete.objects.get(pk=id)
    else:
        pi = Propriete.objects.get(pk=id)
   
    return render(request, 'listing.html', {'infom':pi})

def inscrireuser(request):
     if request.method == 'POST':
         username = request.POST['username']
         lastname = request.POST['last_name']
         firstname = request.POST['first_name']
         email= request.POST['email']
         password = request.POST['password'] 
         mon_user = User.objects.create_user(username, email, password)
         mon_user.first_name = firstname
         mon_user.last_name = lastname
         mon_user.save()
         messages.success(request, 'votre compte a été crée')
         return redirect('home')
   
     return render(request, 'register.html')
 

def demande(request):  
    if request.method == 'GET':
        clie = request.POST['nom']
        email = request.POST['mail']
        msg = request.POST['mssg']
        z = request.POST['maiz']
        user = request.POST['user_id']
        mon_user = Contact( nom=clie, mail=email, message=msg, propriete_id_id=z, user_id=user)
        mon_user.save()
        messages.success(request, 'votre Demande a été Enregistré avec succès')        
        return redirect('info')

    return render(request, 'listing.html' )

def rechercher(request):
    per = Propriete.objects.all()
    if request.method == 'POST':
        per = Propriete.objects.all().filter(pays=request.POST['pays'], ville=request.POST['ville'] )
        return redirect('home', {'maison':per})
        
    
    return render(request,'index.html', {'info':per})
    



   