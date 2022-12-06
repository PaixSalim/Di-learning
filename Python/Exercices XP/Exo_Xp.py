###Exercice 1 ###
print('Hello World'*4)

###Exercice 2 ###
print('(99¨3)*8 = ',pow(99,3)*8)

###Exercice 3 ###
5 < 3  #donne false
3 == 3  #donne true
3 == '3'  #donne false
'3' > 3  #donne false
"Hello" == "hello" #donne false

###Exercice 4 ###
computer_brand = 'HP EliteBook'
print("je possède un ordinateur ", computer_brand)

###Exercice 5 ###
nom = 'KONATE'
age = '20'
shoe_size = '39'
info = 'je suis ' +nom+ " jai " +age+ ' et je chausse du ' +shoe_size
print(info)

###Exercice 6 ###
a = 14
b= 6
if a>b :
    print('Hello World')
    
    
###Exercice 7 ###

nob = input("Entrer un nombre")
if (nob % 2 == 0) :
    print("le nombre ", nob, ' est un monbre paire')
else:
    print("le nombre ", nob, ' est un monbre impaire')
    
###Exercice 8 ###
nom = input('Entrer votre : ')
if (nom[0]=='s'):
    print("Les serpent ne parle pas woo!!!!")
elif (nom[0]=='R'):
    print("Les Rats sont des marmayeurs pas woo!!!!")
else :
    print("jai pas de blague")
    
    
###Exercice 9 ###
tail= input("Entrer votre taille")
if (tail>145):
    print('Vous avez la taille normale monsieur')
else:
    print("Vous avez besoin de grandir d'avantage")

