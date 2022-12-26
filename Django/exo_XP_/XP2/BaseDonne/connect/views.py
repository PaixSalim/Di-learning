from django.shortcuts import render
from .models import *

def index(request):
    ani = Annimal.objects.all()
   # fami = Famille.objects.all()
    return render(request, 'index.html', {'com':ani},)
def famille(request):
   fami = Famille.objects.all()
   return render(request, 'famille.html', {'families':fami},)

def afficher(request, id):
    if request.method == 'POST':
        pi = Annimal.objects.get(pk=id)
      
    else:
        pi = Annimal.objects.get(pk=id)
   
    return render(request, 'Ajouter.html', {'person':pi})
