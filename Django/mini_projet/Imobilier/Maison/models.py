from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Agent(models.Model):
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=50)
    Telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    descript = models.TextField()
    photo = models.ImageField(verbose_name='photo de Agent' , upload_to='img_agent')
    date_servie =models.DateField(default='0')
    statu = models.BooleanField(default='False')
    
    def __str__(self):
        return self.nom
    
    
class Propriete(models.Model):
    nom = models.CharField(max_length=40)
    adresse = models.CharField(max_length=20)
    chambre = models.IntegerField(default='1')
    garage = models.IntegerField(default='1')
    douche = models.IntegerField(default='1')
    date_cons = models.DateField()
    prix = models.IntegerField()
    superficie = models.FloatField()
    descript = models.TextField()
    ville =models.CharField(max_length=20)
    pays = models.CharField(max_length=20)
    agent = models.ForeignKey(Agent, default=0, on_delete=models.CASCADE)
    photo_pri = models.ImageField(verbose_name='photo principale' , upload_to='img_Maison')
    photo1 = models.ImageField(verbose_name='photo de Maison' , default="0", upload_to='img_Maison')
    photo2 = models.ImageField(verbose_name='photo de Maison' , default="0", upload_to='img_Maison')
    photo3 = models.ImageField(verbose_name='photo de Maison' , default="0", upload_to='img_Maison') 
    def __str__(self):
        return self.nom
    
    def photoUrl(self ):
        try:
            url=self.photo.url 
        except : 
            url=""
        return url
       

    
    
class Contact(models.Model):
    nom = models.CharField(max_length=40,  default=0)
    mail = models.CharField(max_length=40, default=0)
    message = models.CharField(max_length=400,  default=0)
    propriete_id = models.ForeignKey(Propriete, default=0, on_delete=models.CASCADE)
    contact_date=models.DateTimeField(default=datetime.now,  blank=True)
    user_id=models.IntegerField(blank=True, default=0)
    def __str__(self):
        return self.nom

    