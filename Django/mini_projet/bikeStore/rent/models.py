from django.db import models

class type_vehicule(models.Model):
    nom = models.CharField(max_length=30)

class taille_vehicule(models.Model):
    nom = models.CharField(max_length=30)


class client(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    ville =models.CharField(max_length=20)
    pays = models.CharField(max_length=20)
    
    
class vehicule(models.Model):
    date_creation = models.DateTimeField()
    cout = models.IntegerField()
    taille_id = models.ForeignKey(taille_vehicule, default=0, on_delete=models.CASCADE)
    type_vehicule_id = models.ForeignKey(type_vehicule, default=0, on_delete=models.CASCADE)
    
class location(models.Model):
    date_location = models.DateTimeField(auto_now_add=0)
    date_retour = models.DateTimeField()
    cout = models.IntegerField()
    statu = models.BooleanField(default=0)
    client_id = models.ForeignKey(client, default=0, on_delete=models.CASCADE)
    vehicule_id = models.ForeignKey(vehicule, default=0, on_delete=models.CASCADE)
    
class location_tarif(models.Model):
    tarif_jour = models.IntegerField()
    taille_id = models.ForeignKey(taille_vehicule, default=0, on_delete=models.CASCADE)
    type_vehicule_id = models.ForeignKey(type_vehicule, default=0, on_delete=models.CASCADE)
    