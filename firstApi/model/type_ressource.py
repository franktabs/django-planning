from django.db import models
from rest_framework import serializers
from .classe import *

class TypeRessource(models.Model):
    code = models.CharField(max_length = 45, unique=True)
    nom = models.CharField(max_length = 45, null=False)
    description = models.CharField(max_length = 45, blank=True)
    
    class Meta:
        db_table = 'type_ressources'
        
class TypeRessourceSerializer(serializers.ModelSerializer):
    classes = ClasseSerializer(read_only=True)

    class Meta:
        model = TypeRessource
        fields = "__all__"
  
