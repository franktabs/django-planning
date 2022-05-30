from django.db import models
from rest_framework import serializers
from .departement import *
from .etudiant import *

class Enseignant(models.Model):
    roles = (('admin', 'Administrateur'), ('simple', 'Simple'), ('chef_departement', 'Chef de Departement'))
    matricule = models.CharField(unique=True, null=False, max_length=45)
    nom = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False, unique=True, max_length=45)
    password = models.CharField(null=False, max_length=255, name="password", blank=False)
    role = models.CharField(max_length = 45, default='simple', null=False, choices=roles)
    
    departements = models.ForeignKey(
        Departement, on_delete=models.SET_NULL, null=True, blank=True)
        
    class Meta:
        db_table = "enseignants"


class EnseignantSerializer(serializers.ModelSerializer):
    departements = DepartementSerializer(read_only=True)

    def validate_matricule(self, value):
        if(len(value)<7 and len(value)>=1):
            raise serializers.ValidationError('min 7 caractères')
        return value
    
    def validate_email(self, value):
        email = Etudiant.objects.filter(email=value)
        if email:
            raise serializers.ValidationError('Sorry!! email already exists')
        return value
    
    class Meta:
        model = Enseignant
        fields = "__all__"