from django.db import models
from programmation.models import Ue, UeSerializer
from rest_framework.response import Response
from rest_framework import serializers
def importEtudiant():
    from firstApi.models import Etudiant, EtudiantSerializer
    return [Etudiant, EtudiantSerializer]

def importDepartement():
    from firstApi.models import Departement
    return Departement
# Create your models here.

class Evaluation(models.Model):
    etudiants = models.ForeignKey(importEtudiant()[0], on_delete=models.CASCADE)
    ues = models.ForeignKey(Ue, on_delete=models.CASCADE)
    cc = models.FloatField(null=False, blank=True)
    tp = models.FloatField(null=False, blank=True)
    ee = models.FloatField(null=False, blank=True)
    
    class Meta:
        db_table = "evaluations"
        unique_together = (('etudiants_id', 'ues_id'))
        
class EvaluationWriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Evaluation
        fields = "__all__"

class EvaluationSerializer(EvaluationWriteSerializer):
    etudiants = importEtudiant()[1]()
    ues = UeSerializer()