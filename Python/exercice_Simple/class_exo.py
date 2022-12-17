
class Voiture:
    marque = 'kia'
    def __init__(self):
        self.couleur = 'noir'
        
    def setCouleur(self,rouge):
        rouge=input('Entrer votre couleur préférée : ')
        self.couleur= rouge
        
    

c= Voiture()
c.setCouleur('rouge')
print('votre voiture est de couleur ',c.couleur)

        