from django.db import models
from rest_framework import serializers
from .departement import  *

class Classe(models.Model):
    code = models.CharField(unique=True, max_length=45, null=False)
    effectif = models.IntegerField()
    departements = models.ForeignKey(Departement, on_delete=models.PROTECT)

    class Meta:
        db_table = 'classes'


class ClasseSerializer(serializers.ModelSerializer):
    departements = DepartementSerializer(read_only=True)

    class Meta:
        model = Classe
        fields = "__all__"