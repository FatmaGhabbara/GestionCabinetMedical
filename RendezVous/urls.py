from django.urls import path
from . import views
urlpatterns=[path('',views.liste_rendezvous,name='liste_rendezvous'),path('ajouter/',views.ajouter_rendezvous,name='ajouter_rendezvous'),path('<int:pk>/modifier/',views.modifier_rendezvous,name='modifier_rendezvous'),path('<int:pk>/supprimer/',views.supprimer_rendezvous,name='supprimer_rendezvous')]
