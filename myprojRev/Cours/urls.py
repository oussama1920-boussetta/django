

from django.urls import path

from Cours.views import listCours


urlpatterns = [
path('list',listCours , name="list"),]