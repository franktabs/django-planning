from django.db import models
from rest_framework import serializers
from .faculte import *

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
