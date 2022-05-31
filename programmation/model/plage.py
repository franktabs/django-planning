from django.db import models
from rest_framework import serializers

class Plage(models.Model):
    jour = models.CharField(max_length=45, null=False)
    periode = models.CharField(max_length=45, null=False)
    
    class Meta:
        db_table = 'plages'
        unique_together = (('jour', 'periode'))
        

class PlageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plage
        fields = "__all__"

