from django.db import models

# Create your models here.
class famille(models.Model):
    nom = models.CharField(max_length=20)

class animal(models.Model):
    nom = models.CharField(max_length=20)
    patte = models.CharField(max_length=20)
    poid = models.IntegerField()
    vitesse = models.CharField(max_length=20)
    famil = models.ForeignKey(famille, default=0, on_delete=models.CASCADE)
    
