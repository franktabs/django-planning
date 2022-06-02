from rest_framework import serializers
from django.db import models
from firstApi.models import Departement, DepartementSerializer, Enseignant, EnseignantSerializer, Salle, SalleSerializer

# Create your models here.

# _______________________________________________________________________

# _______________________________________________________________________

class Groupe(models.Model):
    code = models.CharField(max_length = 45, unique=True, null=False)
    nom = models.CharField(max_length = 45)
    # classes = models.ManyToManyField('Classe', through='groupes_classes', related_name='groupes', )
    
    class Meta:
        db_table = 'groupes'
    
    def __str__(self):
        return self.code
    
class GroupeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Groupe
        fields = "__all__"
    
# _____________________________________________________________________________________________________

class Plage(models.Model):
    jours = (('LUNDI', 'LUNDI'), ('MARDI', 'MARDI'), ('MERCREDI', 'MERCREDI'), ('JEUDI', 'JEUDI'), ('VENDREDI', 'VENDREDI'), ('SAMEDI', 'SAMEDI'), ('DIMANCHE', 'DIMANCHE'))
    heures = (('7h00 - 9h55', '7h00 - 9h55'), ('10h05 - 12h55', '10h05 - 12h55' ), ('13h05 - 15h55', '13h05 - 15h55'), ('16h05 - 18h55', '16h05 - 18h55'), ('19h05 - 21h55', '19h05 - 21h55'))
    # code = models.PositiveIntegerField(null=True, blank=True)
    jour = models.CharField(max_length=45, null=False, choices=jours)
    periode = models.CharField(max_length=45, null=False, choices=heures)
    # enseignants= models.ManyToManyField(Enseignant, through='CoursProgramme', related_name='plages')
    # ues = models.ManyToManyField(Ue, through='CoursProgramme', related_name='plages')
    # salles= models.ManyToManyField(Salle, through='CoursProgramme', related_name='plages')
    # classes = models.ManyToManyField(Classe, through='CoursProgramme', related_name='plages')
    
    
    def __str__(self):
        return  '{} {}'.format(self.jour, self.periode) 
    
    class Meta:
        db_table = 'plages'
        unique_together = (('jour', 'periode'))
        

class PlageSerializer(serializers.ModelSerializer):
    # enseignants= EnseignantSerializer(many=True)
    # ues = UeSerializer(many=True)
    # salles= SalleSerializer(many=True)
    # classes = ClasseSerializer(many=True)
    
    class Meta:
        model = Plage
        fields = "__all__"

# _______________________________________________________________________________________________________

class Classe(models.Model):
    code = models.CharField(unique=True, max_length=45, null=False)
    effectif = models.IntegerField()
    departements = models.ForeignKey(Departement, on_delete=models.PROTECT)
    groupes = models.ManyToManyField(Groupe, through="ClassesGroupe", related_name='classes')

    
    
    class Meta:
        db_table = 'classes'
    
    def __str__(self):
        return self.code


class ClasseSerializer(serializers.ModelSerializer):
    departements = DepartementSerializer(read_only=True, many = False)
    groupes = GroupeSerializer(many=True)
    
    
    class Meta:
        model = Classe
        fields = "__all__"
        depth = 1
        

# ________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

class ClassesGroupe(models.Model):
    groupes = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classe, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "classes_groupes"
    

class ClassesGroupeSerializer(serializers.ModelSerializer):
    groupes = GroupeSerializer()
    classes = ClasseSerializer()
    class Meta:
        model = ClassesGroupe
        fields = '__all__'
        depth = 1
        

# ___________________________________________________________________________

class Specialite(models.Model):
    code = models.CharField(null=False, unique=True, max_length=45)
    nom = models.CharField(max_length=45) 
    classes = models.ForeignKey(Classe, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'specialites'
    
    def __str__(self):
        return self.code

class SpecialiteSerializer(serializers.ModelSerializer):
    classes = ClasseSerializer()
    class Meta:
        model = Specialite
        fields = '__all__'
        depth = 1
        
# _______________________________________________________________________

class Ue(models.Model):
    code = models.CharField(max_length=45, null=False, unique=True)
    intitule = models.CharField(max_length=255)
    credit =models.PositiveSmallIntegerField(null=False)
    # classes = models.ManyToManyField(Classe, through='Enseigne', related_name='ues')
    # enseignants = models.ManyToManyField(Enseignant, through='Enseigne', related_name='ues')
    
    enseignants= models.ManyToManyField(Enseignant, through='CoursProgramme', related_name='ues')
    classes = models.ManyToManyField(Classe, through='CoursProgramme', related_name='ues')
    salles= models.ManyToManyField(Salle, through='CoursProgramme', related_name='ues')
    plages = models.ManyToManyField('Plage', through='CoursProgramme', related_name='ues')
    
    class Meta:
        db_table = 'ues'
    
    def __str__(self):
        return self.code
        

class UeSerializer(serializers.ModelSerializer):
    
    enseignants= EnseignantSerializer(many=True)
    classes = ClasseSerializer(many=True)
    salles= SalleSerializer(many=True)
    plages = PlageSerializer(many=True)
    
    class Meta:
        model = Ue
        fields = "__all__"
# _______________________________________________________________________

class CoursProgramme(models.Model):
    ues = models.ForeignKey(Ue, on_delete=models.CASCADE)
    enseignants = models.ForeignKey(Enseignant, on_delete=models.CASCADE) 
    classes = models.ForeignKey(Classe, on_delete=models.SET_NULL, null=True)
    salles = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True)
    plages= models.ForeignKey(Plage, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'{self.ues} {self.enseignants}' 
    
    class Meta:
        db_table = 'cours_programmes'
        unique_together = (('ues_id', 'classes_id'), ('salles_id', 'plages_id'))

class CoursProgrammeSerializer(serializers.ModelSerializer):
    classes = ClasseSerializer()
    ues = UeSerializer()
    enseignants = EnseignantSerializer()
    salles= SalleSerializer()
    # plages = PlageSerializer()
    class Meta:
        model = CoursProgramme
        fields = '__all__'
        depth = 1

# _______________________________________________________________________

class Enseignes(models.Model):
    ues = models.ForeignKey(Ue, on_delete=models.CASCADE)
    enseignants = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True) 
    classes = models.ForeignKey(Classe, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'enseignes'
        unique_together = (('ues_id', 'classes_id'))

class EnseignesSerializer(serializers.ModelSerializer):
    classes = ClasseSerializer()
    ues = UeSerializer()
    enseignants = EnseignantSerializer()
    
    class Meta:
        model = Enseignes
        fields = '__all__'
        depth = 1
        

# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________



# _______________________________________________________________________





# _______________________________________________________________________

