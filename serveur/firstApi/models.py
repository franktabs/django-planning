from importlib.metadata import files
from django.db import models
from rest_framework import serializers
# Create your models here.

# Creation Faculte______________________________________________________


class Faculte(models.Model):
    code = models.CharField(max_length=45, unique=True, null=False)
    nom = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'facultes'


class FaculteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculte
        fields = '__all__'
# _________________________________________________________________________


# Creation Batiment _______________________________________________________
class Batiment(models.Model):
    code = models.CharField(unique=True, max_length=45, null=False)
    nom = models.CharField(max_length=45)
    localisation = models.CharField(max_length=45, null=True, blank=True)
    facultes = models.ForeignKey(Faculte, on_delete=models.PROTECT)
    class Meta:
        db_table = 'batiments'


class BatimentSerializer(serializers.ModelSerializer):
    facultes = FaculteSerializer()
    class Meta:
        model = Batiment
        fields = '__all__'
# ___________________________________________________________________________


class Departement(models.Model):
    code = models.CharField(unique=True, max_length=45, null=False)
    nom = models.CharField(max_length=45)
    facultes = models.ForeignKey(Faculte, on_delete=models.PROTECT)
    class Meta:
        db_table = 'departements'

class DepartementSerializer(serializers.ModelSerializer):
    facultes = FaculteSerializer()
    class Meta:
        model = Departement
        fields = '__all__'

# typeSalle _______________________________________________________________________


class TypeSalle(models.Model):
    code = models.CharField(max_length=45, null=False, unique=True)
    nom = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = "type_salles"


class TypeSalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeSalle
        fields = "__all__"

# _________________________________________________________________________________

# Salle ___________________________________________________________________________


class Salle(models.Model):
    electricite = ((1, "OUI"), (0, "NON"))
    code = models.CharField(max_length=45, null=False)
    nom = models.CharField(max_length=45)
    etat_electricite = models.IntegerField(choices=electricite)
    capacite = models.IntegerField()
    batiments = models.ForeignKey(
        Batiment, on_delete=models.SET_NULL, null=True, blank=True)
    type_salles = models.ForeignKey(TypeSalle, on_delete=models.PROTECT)

    class Meta:
        db_table = 'salles'
        unique_together = (('code', 'batiments_id'))


class SalleSerializer(serializers.ModelSerializer):
    batiments = BatimentSerializer(read_only=True)
    type_salles = TypeSalleSerializer(read_only=True)

    class Meta:
        model = Salle
        fields = '__all__'

# ______________________________________________________________________________


class Classe(models.Model):
    code = models.CharField(unique=True, max_length=45, null=False)
    effectif = models.IntegerField()
    departements = models.ForeignKey(Departement, on_delete=models.PROTECT)

    class Meta:
        db_table = 'classes'


class ClasseSerializer(serializers.ModelSerializer):
    departements = DepartementSerializer(read_only=True)

    class Meta:
        model = Classe
        fields = "__all__"

# Etudiant __________________________________________________________________

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


# ___________________________________________________________________________

# Enseignant __________________________________________________________________

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

# ___________________________________________________________________________

# Utilisateur ________________________________________________________________

class Utilisateur(models.Model):
    email = models.EmailField(max_length=45, null=False)
    password= models.CharField(max_length=45, null=False)
    
class UtilisateurSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Utilisateur
        fields = "__all__"

# ____________________________________________________________________________

# TypeSalle __________________________________________________________________

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
  


# ____________________________________________________________________________

# Ressource___________________________________________________________________

class Ressource(models.Model):
    code = models.CharField(max_length = 45, unique=True)
    nom = models.CharField(max_length = 45, null=False)
    description = models.CharField(max_length = 45, blank=True)
    type_ressources=models.ForeignKey(TypeRessource, on_delete=models.SET_NULL, null=True)
    facultes = models.ForeignKey(Faculte, on_delete=models.PROTECT)
    class Meta:
        db_table = 'ressources'
        
class RessourceSerializer(serializers.ModelSerializer):
    type_ressources = TypeSalleSerializer(read_only=True)
    facultes = FaculteSerializer(read_only=True)
    class Meta:
        model = Ressource
        fields = "__all__"
  

# ____________________________________________________________________________