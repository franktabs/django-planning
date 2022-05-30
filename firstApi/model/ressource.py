from django.db import models
from rest_framework import serializers
from .type_ressource import *
from .faculte import *

class Ressource(models.Model):
    code = models.CharField(max_length = 45, unique=True)
    nom = models.CharField(max_length = 45, null=False)
    description = models.CharField(max_length = 45, blank=True)
    type_ressources=models.ForeignKey(TypeRessource, on_delete=models.SET_NULL, null=True)
    facultes = models.ForeignKey(Faculte, on_delete=models.PROTECT)
    class Meta:
        db_table = 'ressources'
        
class RessourceSerializer(serializers.ModelSerializer):
    type_ressources = TypeRessourceSerializer(read_only=True)
    facultes = FaculteSerializer(read_only=True)
    class Meta:
        model = Ressource
        fields = "__all__"