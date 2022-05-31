from django.db import models
from rest_framework import serializers
from firstApi.model.salle import Salle, SalleSerializer
from firstApi.model.utilisateur import Enseignant, EnseignantSerializer

from programmation.model.classes_groupe import Classe, ClasseSerializer
from programmation.model.plage import Plage, PlageSerializer

class Ue(models.Model):
    code = models.CharField(max_length=45, null=False, unique=True)
    intitule = models.CharField(max_length=255)
    credit =models.PositiveSmallIntegerField(max_length=1, null=False)
    # classes = models.ManyToManyField(Classe, through='Enseigne', related_name='ues')
    # enseignants = models.ManyToManyField(Enseignant, through='Enseigne', related_name='ues')
    
    enseignants= models.ManyToManyField(Enseignant, through='CoursProgramme', related_name='enseignants')
    plages = models.ManyToManyField(Plage, through='CoursProgramme', related_name='enseignants')
    salles= models.ManyToManyField(Salle, through='CoursProgramme', related_name='enseignants')
    classes = models.ManyToManyField(Classe, through='CoursProgramme', related_name='enseignants')
    class Meta:
        db_table = 'ues'
        

class UeSerializer(serializers.ModelSerializer):
    enseignants= EnseignantSerializer()
    plages = PlageSerializer()
    salles= SalleSerializer()
    classes = ClasseSerializer()
    
    class Meta:
        model = Ue
        fields = "__all__"

