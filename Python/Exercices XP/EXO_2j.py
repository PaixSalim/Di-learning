import ast
#-----------------Exercice 1 -------------------------------#
my_fav_numbers ={11111:"salim", 51515123:"Madou" }

#Ajoutez deux nouveaux numéros à l’ensemble.
my_fav_numbers["7483893"]= "Bernard"
#Supprimer un element de la liste.
del my_fav_numbers[11111]
#creer un autre ensemble
friend_fav_numbers={234:'burkina', 67798:'Mali'}
#concaténer un nouvelle variable
contact={226:'burkina'}
contact = my_fav_numbers.update(friend_fav_numbers)
print(contact)
#-------------------Exercice 3 ------------------------------------#
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# retirer banana de la liste
basket.remove("Banana")
# retirer Myrtille de la liste
#basket.append("Myrtille")
# Ajouter Kiwi de la liste
basket.append("Kiwi")
# Ajouter Apple de la liste
basket.insert(0,"Apple")
# compter le nombre de Apple dans la liste
k=0
for i in range(0,len(basket)):
    if(basket[i]=='Apple'):
        k=k+1
print('il ya ',k,'pomme dans le panier ')
# suprimer la liste
basket.clear()
# imprimer la liste
print(basket)

#-------------------Exercice 5 ------------------------------------#
for on in range(1,11):
    print(on)
for no in range(1,21):
    if no% 2==0:
        print(no)
    
#-------------------Exercice 6 ------------------------------------#
moi = 'salim'
toi = input('Entrer votre nom : ')
while (moi!=toi):
    toi = input('veuillez essayer encore : ')
    
#-------------------Exercice 8 ------------------------------------#
#Écrivez une boucle qui demande à un utilisateur d’entrer une série de garnitures de pizza
grani=[]
i=0
graniture=input('Entrer une garniture : ')
grani.append(graniture)
while graniture !='quitter':
    print('la garniture ',graniture, ' sera ajouté sur votre pizza \n')
    graniture=input('Entrer une garniture encore (ecrire quitter pour quitter) :')
    grani.append(graniture)
    i=i+1
j=i
print('Voici la liste des garniture choisi ')
for k in range(0,j):
    print(grani[k])
print("prix total : ",10+(2.5*i))