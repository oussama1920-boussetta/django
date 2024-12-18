from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser


def Verif_username(value):
    if len(value) > 10:  
        raise ValidationError("Username must has max 10 characters")  

class Enseignant(AbstractUser):
    username = models.CharField(max_length=10 ,unique=True,validators=[Verif_username]) 
    




