from django.db import models
from rest_framework import serializers

class Ue(models.Model):
    code = models.CharField(max_length=45, null=False, unique=True)
    intitule = models.CharField(max_length=255)
    credit =models.PositiveSmallIntegerField(null=False)
    # classes = models.ManyToManyField(Classe, through='Enseigne', related_name='ues')
    # enseignants = models.ManyToManyField(Enseignant, through='Enseigne', related_name='ues')
    
    
    class Meta:
        db_table = 'ues'
    
    def __str__(self):
        return self.code
        

class UeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ue
        fields = "__all__"

