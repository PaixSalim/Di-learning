from django.db import models

# Create your models here.
class Personne(models.Model):
    nom = models.CharField(max_length=40)
    adresse = models.CharField(max_length=20)
    number =models.CharField(max_length=20)
    email = models.CharField(max_length=20)
