from django.db import models

# Create your models here.
class personne(models.Model):
    nom = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    num = models.CharField(max_length=20)
    adresse = models.CharField(max_length=20)