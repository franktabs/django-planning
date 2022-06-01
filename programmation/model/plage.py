from django.db import models
from rest_framework import serializers
from firstApi.model.salle import Salle, SalleSerializer
from firstApi.model.utilisateur import Enseignant, EnseignantSerializer
from programmation.model.classes_groupe import Classe, ClasseSerializer
from programmation.model.ue import Ue, UeSerializer

class Plage(models.Model):
    jours = (('LUNDI', 'LUNDI'), ('MARDI', 'MARDI'), ('MERCREDI', 'MERCREDI'), ('JEUDI', 'JEUDI'), ('VENDREDI', 'VENDREDI'), ('SAMEDI', 'SAMEDI'), ('DIMANCHE', 'DIMANCHE'))
    heures = (('7h00 - 9h55', '7h00 - 9h55'), ('10h05 - 12h55', '10h05 - 12h55' ), ('13h05 - 15h55', '13h05 - 15h55'), ('16h05 - 18h55', '16h05 - 18h55'), ('19h05 - 21h55', '19h05 - 21h55'))
    # code = models.PositiveIntegerField(null=True, blank=True)
    jour = models.CharField(max_length=45, null=False, choices=jours)
    periode = models.CharField(max_length=45, null=False, choices=heures)
    enseignants= models.ManyToManyField(Enseignant, through='CoursProgramme', related_name='plages')
    ues = models.ManyToManyField(Ue, through='CoursProgramme', related_name='plages')
    salles= models.ManyToManyField(Salle, through='CoursProgramme', related_name='plages')
    classes = models.ManyToManyField(Classe, through='CoursProgramme', related_name='plages')
    
    
    def __str__(self):
        return  '{} {}'.format(self.jour, self.periode) 
    
    class Meta:
        db_table = 'plages'
        unique_together = (('jour', 'periode'))
        

class PlageSerializer(serializers.ModelSerializer):
    enseignants= EnseignantSerializer(many=True)
    ues = UeSerializer(many=True)
    salles= SalleSerializer(many=True)
    classes = ClasseSerializer(many=True)
    
    class Meta:
        model = Plage
        fields = "__all__"

