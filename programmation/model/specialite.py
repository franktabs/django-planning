# from rest_framework import serializers
from firstApi.model.classe import *

class Specialite(models.Model):
    code = models.CharField(null=False, unique=True, max_length=45)
    nom = models.CharField(max_length=45) 
    classes = models.ForeignKey(Classe, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'specialites'

class SpecialiteSerializer(serializers.ModelSerializer):
    classes = ClasseSerializer()
    class Meta:
        model = Specialite
        fields = '__all__'