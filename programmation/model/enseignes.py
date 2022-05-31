from django.db import models
from rest_framework import serializers
from .ue import Ue, UeSerializer
from firstApi.model.enseignant import Enseignant, EnseignantSerializer
from firstApi.model.classe import Classe, ClasseSerializer

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