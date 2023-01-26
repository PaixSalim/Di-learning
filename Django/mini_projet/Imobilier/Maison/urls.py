from django import views
from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',home, name='home'),
    path('information<int:id>/',information , name='info' ),
    path('information_maison<int:id>/',informatio , name='infom' ),
    path("a propos",about , name="abouts" ),
    path('login',connecter , name='connecter' ),
    path('listesMaison',listes , name='listes' ),
    path('logout',deconnecter , name='deconnecter' ),
    path("inscription",inscrireuser , name="inscrire" ),
    path("Recherche",rechercher , name="search" ),
    path("Tableau de bord",dashboard , name="dashboard" ),
    

   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)