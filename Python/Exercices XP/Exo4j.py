#-----------Exercice 1-------------------------#
def message() :
    print("Dans ce cour nous apprenons le language Python \n")

message()
#---------------Exercice 2---------------------#
def appelle( livre ) :
    lire = 'Mon livre préferé est ',livre
    print(lire)
    
appelle('soleil des indépendance ')

#--------------Exercice 3 -----------------------#
def geograph(pays, ville) : 
   
    print(ville ,' est en ',pays)
pays = 'COTE DIVOIRE '    
geograph(pays, 'Abobo')

#-------------Exercice 4 -------------------#
import random
def hasar(ran, moi):
    if ran == moi :
        print('félicitation !!! tu as gagné ')
    else:
        print('oohh vous avez perdu ')
ran = random.randint(1,101)
moi = int(input('Entrer un nombre : '))
while (moi<=0 and moi>=100):
    moi = int(input('Entrer un nombre : '))
hasar(ran, moi )
print('la machine a choisi ',ran)
#---------------Exercice 5 ------------------#
def Tshirt(taille, text) : 
    print('La taille de mon T-shirt est ',taille , ' le text imprimé decu est ', text)
tail=int(input('Entrer la taille de votre t-shirt : '))
text=input('Entrer le texte de votre t-shirt : ')
Tshirt(tail, text)

    