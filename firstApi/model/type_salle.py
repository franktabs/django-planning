from django.db import models
from rest_framework import serializers

class TypeSalle(models.Model):
    code = models.CharField(max_length=45, null=False, unique=True)
    nom = models.CharField(max_length=45, null=False)
    description = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = "type_salles"
    
    def __str__(self):
        return self.code


class TypeSalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeSalle
        fields = "__all__"