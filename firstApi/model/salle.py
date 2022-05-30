from django.db import models
from rest_framework import serializers
from .batiment import *
from .type_salle import *


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