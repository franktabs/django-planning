from django.db import models
from rest_framework import serializers
# from firstApi.model.salle import Salle
# from programmation.model.plage import Plage

# from programmation.model.ue import Ue
from .departement import *
from .classe import *


class Utilisateur(models.Model):
    email = models.EmailField(max_length=45, null=False)
    password= models.CharField(max_length=45, null=False)
    
class UtilisateurSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Utilisateur
        fields = "__all__"



class Enseignant(models.Model):
    roles = (('admin', 'Administrateur'), ('simple', 'Simple'), ('chef_departement', 'Chef de Departement'))
    matricule = models.CharField(unique=True, max_length=45, null=True, blank=True)
    nom = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False, unique=True, max_length=45)
    password = models.CharField(null=False, max_length=255, name="password", blank=False)
    role = models.CharField(max_length = 45, default='simple', null=False, choices=roles)
    
    
    departements = models.ForeignKey(
        Departement, on_delete=models.SET_NULL, null=True, blank=True)
        
    class Meta:
        db_table = "enseignants"
    
    def __str__(self):
        return self.nom


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