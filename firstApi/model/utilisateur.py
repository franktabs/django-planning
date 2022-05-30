from django.db import models
from rest_framework import serializers

class Utilisateur(models.Model):
    email = models.EmailField(max_length=45, null=False)
    password= models.CharField(max_length=45, null=False)
    
class UtilisateurSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Utilisateur
        fields = "__all__"