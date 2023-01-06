from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(client)
admin.site.register(vehicule)
admin.site.register(taille_vehicule)
admin.site.register(type_vehicule)
admin.site.register(location)
admin.site.register(location_tarif)
