from django.db import models
from rest_framework import serializers


class Faculte(models.Model):
    code = models.CharField(max_length=45, unique=True, null=False)
    nom = models.CharField(max_length=45, null=False)
    
    class Meta:
        db_table = 'facultes'

    def __str__(self):
        return self.code

class FaculteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculte
        fields = '__all__'
        