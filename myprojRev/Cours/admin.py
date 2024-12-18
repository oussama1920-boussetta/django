from django.apps import AppConfig
from django.contrib import admin
from Cours.models import Cours



class CoursAdmin(admin.ModelAdmin):
    # Champs affichés dans la liste des événements
    list_display = ('titre', 'categorie', 'date_publication','enseignant')
    search_fields = ('titre',)
    list_filter = ('categorie',)
    
       # Actions en bloc pour changer la catégorie
    def changer_categorie_WEB(modeladmin, request, queryset):
        queryset.update(categorie='WEB')
    changer_categorie_WEB.short_description = "Changer la catégorie en WEB"

    def changer_categorie_MOBILE(modeladmin, request, queryset):
        queryset.update(categorie='MOBILE')
    changer_categorie_MOBILE.short_description = "Changer la catégorie en MOBILE"
    
    def changer_categorie_BI(modeladmin, request, queryset):
        queryset.update(categorie='BI')
    changer_categorie_BI.short_description = "Changer la catégorie en BI"

    actions = [changer_categorie_WEB,changer_categorie_MOBILE,changer_categorie_BI]

    
    
admin.site.register(Cours, CoursAdmin)

 
    