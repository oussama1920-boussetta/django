import datetime
from django.db import models
from django.core.exceptions import ValidationError  # Import correct pour la validation
from django.utils.timezone import now  # Utilisé pour gérer les dates
from Enseignant.models import Enseignant  # Assurez-vous que le chemin est correct

# Liste des catégories pour le champ `categorie`
CATEGORY_LIST = (
    ('Mobile', 'Mobile'),
    ('BI', 'BI'),
    ('WEB', 'WEB'),
)

# Modèle Cours
class Cours(models.Model):
    code = models.AutoField(primary_key=True)  # Utilisation d'AutoField pour un ID automatique
    titre = models.CharField(max_length=255, blank=False, null=False)
    categorie = models.CharField(choices=CATEGORY_LIST, max_length=20)
    date_publication = models.DateTimeField(default=now())  # Valeur par défaut pour éviter les erreurs
    created_date = models.DateTimeField(auto_now_add=True)  # Correction : DateTimeField pour la cohérence
    updated_date = models.DateTimeField(auto_now=True)  # Correction : DateTimeField pour la cohérence
    enseignant = models.ForeignKey(
        Enseignant, 
        on_delete=models.CASCADE, 
        related_name='cours',  # Correction pour éviter les conflits avec d'autres relations
        null=True
    )
    
    

    def clean(self):
        """Validation personnalisée pour s'assurer que `date_publication` est future."""
        super().clean()  # Appeler le nettoyage par défaut
        if self.date_publication and self.date_publication <= now():
            raise ValidationError("La date de publication doit être dans le futur.")

    def __str__(self):
        """Représentation textuelle de l'objet Cours."""
        return self.titre
    
    class Meta:
        verbose_name = "Cour"

