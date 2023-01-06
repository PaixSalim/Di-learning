from django.db import models

# Create your models here.
class gif_categorie(models.Model):
    nom = models.CharField(max_length=20)

class gif(models.Model):
    titre = models.CharField(max_length=20)
    url = models.URLField(max_length=20)
    created_at = models.DateTimeField()
    uploader_name = models.CharField(max_length=20)
    id_cat = models.ForeignKey(gif_categorie, default=0, on_delete=models.CASCADE)