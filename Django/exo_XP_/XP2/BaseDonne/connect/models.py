from django.db import models

# Create your models here.
class Famille(models.Model):
    nom = models.CharField(max_length=20)
    
    
class Annimal(models.Model):
    nom = models.CharField(max_length=20)
    patte = models.IntegerField()
    vitesse = models.IntegerField()
    #id_famille= models.ForeignKey(Famille, default=0,  on_delete=models.CASCADE)

def __str__(self):
        return {self.nom}
    


