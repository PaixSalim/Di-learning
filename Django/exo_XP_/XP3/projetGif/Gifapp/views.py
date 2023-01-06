from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    anim = gif.objects.all()
    
    return render(request,'index.html', {'gif' : anim})

def afficher(request, id):
    if request.method == 'POST':
        pi = gif.objects.get(pk=id)
      
    else:
        pi = gif.objects.get(pk=id)
   
    return render(request, 'afficher.html', {'info':pi})

def mafami(request, id):
    if request.method == 'POST':
        pi = gif.objects.all().filter(famil_id=id)
      
    else:
        pi = gif.objects.all().filter(famil_id=id)
   
    return render(request, 'index.html', {'fami':pi})
    