from django import views
from django.urls import path,include
from .views import *

urlpatterns = [

   
    path('',Afficher_nom, name='Afficher_nom'),
    path('home',Afficher_numero, name='Afficher_numero'),
   
]