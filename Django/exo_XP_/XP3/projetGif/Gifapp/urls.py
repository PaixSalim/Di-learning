from django import views
from django.urls import path,include
from .views import *

urlpatterns = [

    path('',home, name='home'),
    path('animal<int:id>/',afficher , name='afficher' ),
    path('famille<int:id>/',mafami , name='mafami' ),
   
]