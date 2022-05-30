from django.db import models
from rest_framework import serializers
from .classe import *
from .enseignant import *


class Etudiant(models.Model):
    matricule = models.CharField(null=True, blank=True, max_length=45)
    noms = models.CharField(max_length=255, null=False)
    adresse = models.CharField(null=True, blank=True, max_length=255)
    email = models.EmailField(null=False, unique=True, max_length=45)
    password = models.CharField(null=False, blank=False, max_length=255, name="password")
    classes = models.ForeignKey(
        Classe, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        db_table = "etudiants"


class EtudiantSerializer(serializers.ModelSerializer):
    classes = ClasseSerializer(read_only=True)

    def validate_matricule(self, value):
        if(len(value)<7 and len(value)>=1):
            raise serializers.ValidationError('au-moins 7 caractères')
        return value
    
    def validate_email(self, value):
        email = Enseignant.objects.filter(email=value)
        if email:
            raise serializers.ValidationError('Sorry!! email already exists')
        return value
    
    class Meta:
        model = Etudiant
        fields = "__all__"

