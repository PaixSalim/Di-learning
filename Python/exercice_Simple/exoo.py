datas = {
    "animals": [
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
    ],
    "families": [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
        {
            "id": 1,
            "name": "Mamifère"
        },
        {
            "id": 2,
            "name": "Ovipare"
        }
    ]
}

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
        if o=='id' and l ==1 :
            print(k)
for i in datas:
    print(i)
    for don in datas[i]:
        for k, l in don.items():
            print(k, l)
