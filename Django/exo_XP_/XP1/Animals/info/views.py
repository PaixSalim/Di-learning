from django.shortcuts import render, HttpResponseRedirect

from .models import *

# Create your views here.
def animal(request, id):
    animals = [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        }
    ]
    
    families = [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
           {
            "id": 3,
            "name": "Reptile"
        }
    ]


    context = {
        'animals' : animals,
        'families': families
    }
    for k in animals:  
        for o, l in k.items():
            if o=='id' and l ==id :
                pi=k
    
                return render(request, 'animal.html', {'person':pi})

def famille(request, id):
    animals = [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        }
    ]
    
    families = [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
           {
            "id": 3,
            "name": "Reptile"
        }
    ]


    context = {
        'animals' : animals,
        'families': families
    }
    for k in animals:  
        for o, l in k.items():
            if o=='family' and l ==id :
                pi=k
    
                return render(request, 'famille.html', {'animal':pi})

def index(request):
    animals = [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        }
    ]
    
    families = [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
           {
            "id": 3,
            "name": "Reptile"
        }
    ]


    context = {
        'animals' : animals,
        'families': families
    }
       # for k in people:
       #for o, l in k.items():
        #if o=='id' and l ==id :
         # pi=k
    
          #return render(request, 'peopl1.html', {'person':pi})
    return render(request, 'index.html', context)
