from django.db import models
from rest_framework import serializers
from .faculte import *

class Departement(models.Model):
    code = models.CharField(unique=True, max_length=45, null=False)
    nom = models.CharField(max_length=45)
    facultes = models.ForeignKey(Faculte, on_delete=models.PROTECT)
    class Meta:
        db_table = 'departements'

class DepartementSerializer(serializers.ModelSerializer):
    facultes = FaculteSerializer()
    class Meta:
        model = Departement
        fields = '__all__'
