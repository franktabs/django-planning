from django.db import models
from rest_framework import serializers

def importClass():
    from programmation import models
    return models
# # Create your models here.

# from .model import *

# # Creation Faculte______________________________________________________



class Faculte(models.Model):
    code = models.CharField(max_length=45, unique=True, null=False)
    nom = models.CharField(max_length=45, null=False)
    
    class Meta:
        db_table = 'facultes'

    def __str__(self):
        return self.code

class FaculteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculte
        fields = '__all__'

# # _________________________________________________________________________



class Batiment(models.Model):
    code = models.CharField(unique=True, max_length=45, null=False)
    nom = models.CharField(max_length=45)
    localisation = models.CharField(max_length=45, null=True, blank=True)
    facultes = models.ForeignKey(Faculte, on_delete=models.PROTECT)
    class Meta:
        db_table = 'batiments'

    def __str__(self):
        return self.nom

class BatimentSerializer(serializers.ModelSerializer):
    facultes = FaculteSerializer()
    class Meta:
        model = Batiment
        fields = '__all__'
        
        
# # ___________________________________________________________________________

class Departement(models.Model):
    code = models.CharField(unique=True, max_length=45, null=False)
    nom = models.CharField(max_length=45)
    facultes = models.ForeignKey(Faculte, on_delete=models.PROTECT)
    class Meta:
        db_table = 'departements'
        
    def __str__(self):
        return self.nom

class DepartementSerializer(serializers.ModelSerializer):
    facultes = FaculteSerializer()
    class Meta:
        model = Departement
        fields = '__all__'

# # typeSalle _______________________________________________________________________


class TypeSalle(models.Model):
    code = models.CharField(max_length=45, null=False, unique=True)
    nom = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = "type_salles"
    
    def __str__(self):
        return self.code


class TypeSalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeSalle
        fields = "__all__"

# # _________________________________________________________________________________

# # Salle ___________________________________________________________________________


class Salle(models.Model):
    electricite = ((1, "OUI"), (0, "NON"))
    code = models.CharField(max_length=45, null=False)
    nom = models.CharField(max_length=45)
    etat_electricite = models.IntegerField(choices=electricite)
    capacite = models.IntegerField()
    batiments = models.ForeignKey(
        Batiment, null=True, on_delete=models.SET_NULL,  blank=True)
    type_salles = models.ForeignKey(TypeSalle, on_delete=models.CASCADE)

    class Meta:
        db_table = 'salles'
        unique_together = (('code', 'batiments_id'))
        
    def __str__(self):
        return self.code

class SalleSerializer(serializers.ModelSerializer):
    batiments = BatimentSerializer()
    type_salles = TypeSalleSerializer()

    class Meta:
        model = Salle
        fields = '__all__'
# # ______________________________________________________________________________


# class Classe(models.Model):
#     code = models.CharField(unique=True, max_length=45, null=False)
#     effectif = models.IntegerField()
#     departements = models.ForeignKey(Departement, on_delete=models.PROTECT)

#     class Meta:
#         db_table = 'classes'


# class ClasseSerializer(serializers.ModelSerializer):
#     departements = DepartementSerializer(read_only=True)

#     class Meta:
#         model = Classe
#         fields = "__all__"

# # Etudiant __________________________________________________________________

class Utilisateur(models.Model):
    email = models.EmailField(max_length=45, null=False)
    password= models.CharField(max_length=45, null=False)
    
class UtilisateurSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Utilisateur
        fields = "__all__"



class Enseignant(models.Model):
    roles = (('admin', 'Administrateur'), ('simple', 'Simple'), ('chef_departement', 'Chef de Departement'))
    matricule = models.CharField(max_length=45, null=True, blank=True, unique=True)
    noms = models.CharField(max_length=45, null=False)
    email = models.EmailField(null=False, unique=True, max_length=45)
    password = models.CharField(null=False, max_length=255, name="password", blank=False)
    role = models.CharField(max_length = 45, default='simple', null=False, choices=roles)
    
    
    departements = models.ForeignKey(
        Departement, on_delete=models.SET_NULL, null=True, blank=True)
        
    class Meta:
        db_table = "enseignants"
    
    def __str__(self):
        return self.noms


class EnseignantSerializer(serializers.ModelSerializer):
    departements = DepartementSerializer(read_only=True)

    def validate_matricule(self, value):
        message = []
        erreur = False
        matricule = Etudiant.objects.filter(matricule=value)
        if matricule:
            erreur = True
            message.append('Sorry!! Matricule already exist')
        if(len(value)<7 and len(value)>=1):
            erreur = True
            message.append('min 7 caractères')
        if erreur:
            raise serializers.ValidationError(message)
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
        importClass().Classe, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        db_table = "etudiants"


class EtudiantSerializer(serializers.ModelSerializer):
    classes = importClass().ClasseSerializer(read_only=True)

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
# # ____________________________________________________________________________

# # TypeRessource __________________________________________________________________

class TypeRessource(models.Model):
    code = models.CharField(max_length = 45, unique=True)
    nom = models.CharField(max_length = 45, null=False)
    description = models.CharField(max_length = 45, blank=True)
    
    class Meta:
        db_table = 'type_ressources'
        
    def __str__(self):
        return self.code
        
class TypeRessourceSerializer(serializers.ModelSerializer):
    classes = importClass().ClasseSerializer(read_only=True)

    class Meta:
        model = TypeRessource
        fields = "__all__"

# # ____________________________________________________________________________

# # Ressource___________________________________________________________________

class Ressource(models.Model):
    code = models.CharField(max_length = 45, unique=True)
    nom = models.CharField(max_length = 45, null=False)
    description = models.CharField(max_length = 45, blank=True)
    type_ressources=models.ForeignKey(TypeRessource, on_delete=models.SET_NULL, null=True)
    facultes = models.ForeignKey(Faculte, on_delete=models.PROTECT)
    class Meta:
        db_table = 'ressources'
    
    def __str__(self):
        return self.code
        
class RessourceSerializer(serializers.ModelSerializer):
    type_ressources = TypeRessourceSerializer(read_only=True)
    facultes = FaculteSerializer(read_only=True)
    class Meta:
        model = Ressource
        fields = "__all__"

# # ____________________________________________________________________________


