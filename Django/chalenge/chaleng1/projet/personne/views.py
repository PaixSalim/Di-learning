from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'index.html',)


def people(request):
    people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]
    trie = sorted(people,key = lambda d: d['age'])

    context = {
        'personne' : trie,
        
    }
    return render(request, 'people.html', context)
  
def choi(request, id):
    people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]  
    for k in people:
       for o, l in k.items():
        if o=='id' and l ==id :
          pi=k
    
          return render(request, 'peopl1.html', {'person':pi})
