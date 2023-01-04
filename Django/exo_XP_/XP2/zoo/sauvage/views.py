from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    anim = animal.objects.all()
    
    return render(request,'animal.html', {'animaux' : anim})

def afficher(request, id):
    if request.method == 'POST':
        pi = animal.objects.get(pk=id)
      
    else:
        pi = animal.objects.get(pk=id)
   
    return render(request, 'afficher.html', {'info':pi})

def mafami(request, id):
    if request.method == 'POST':
        pi = animal.objects.all().filter(famil_id=id)
      
    else:
        pi = animal.objects.all().filter(famil_id=id)
   
    return render(request, 'index.html', {'fami':pi})
    