from django.apps import AppConfig
from django.contrib import admin

from Enseignant.models import Enseignant

# Register your models here.
class EnseignantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Enseigant'
    admin.site.register(Enseignant)