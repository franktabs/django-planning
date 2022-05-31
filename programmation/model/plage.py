from django.db import models
from rest_framework import serializers
from firstApi.model.salle import Salle, SalleSerializer
from firstApi.model.utilisateur import Enseignant, EnseignantSerializer
from programmation.model.classes_groupe import Classe, ClasseSerializer
from programmation.model.ue import Ue, UeSerializer

class Plage(models.Model):
    jour = models.CharField(max_length=45, null=False)
    periode = models.CharField(max_length=45, null=False)
    
    
    enseignants= models.ManyToManyField(Enseignant, through='CoursProgramme', related_name='enseignants')
    ues = models.ManyToManyField(Ue, through='CoursProgramme', related_name='plages')
    salles= models.ManyToManyField(Salle, through='CoursProgramme', related_name='plages')
    classes = models.ManyToManyField(Classe, through='CoursProgramme', related_name='plages')
    
    class Meta:
        db_table = 'plages'
        unique_together = (('jour', 'periode'))
        

class PlageSerializer(serializers.ModelSerializer):
    enseignants= EnseignantSerializer(read_only=True)
    ues = UeSerializer(read_only=True)
    salles= SalleSerializer(read_only=True)
    classes = ClasseSerializer(read_only=True)
    
    class Meta:
        model = Plage
        fields = "__all__"

