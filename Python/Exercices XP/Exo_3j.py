#-------------Exercice 1-------------------#
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)

#-------------Exercice 2-------------------#
prix = 0
pri = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for i in family:
    if family[i] < 3:
        prix=prix +0
    elif (family[i]<=12):
        prix=prix + 10
    elif (family[i]>12):
        prix=prix +15
print('le montant total que votre famille doit payer est : ', prix)
#-------------Bonus-------------------------------#
fami = {}
print('--------Bonus----entrer nom = q et age= 0 pour quitter ----')
menbr = 'ok'
while menbr !='q':
    menbr = input('Entrer le mon : ')
    age = int(input('Entrer age ')) 
    fami[menbr]=age
print(fami)
for i in fami:
    if fami[i] < 3:
        pri=pri +0
    elif (fami[i]<=12):
        pri=pri + 10
    elif (fami[i]>12):
        pri=pri +15
print('le montant total que votre famille doit payer est : ', pri, '$ \n')


#-------------Exercice 4-------------------#        
dic={}
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
for k in range(0, len(users)):
    print(k)
    dic[k]=users
print(dic)
for i in range(0, len(users)):
  
    dic[i]=users[i]
print(dic)