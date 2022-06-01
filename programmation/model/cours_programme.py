from django.db import models
from rest_framework import serializers

from firstApi.model.salle import Salle, SalleSerializer
from programmation.model.plage import Plage, PlageSerializer
from .ue import Ue, UeSerializer
from firstApi.model.enseignant import Enseignant, EnseignantSerializer
from firstApi.model.classe import Classe, ClasseSerializer

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