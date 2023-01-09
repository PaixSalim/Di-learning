from django import views
from django.urls import path,include
from .views import *

urlpatterns = [

    path('',home, name='home'),
    path('location',locations, name='locations'),
    path('inscrire',inscrire, name='inscrire'),
    path('inscrire_client',ajoutercli, name='inscriree'),
    path('inscrire_vehicule',ajoutervehi, name='inscrirer'),
    path('location<int:id>/',afficher , name='afficher' ),
    path('client<int:id>/',modifier , name='modifier_cl' ),
    path('client',listclient , name='liste' ),
   
]