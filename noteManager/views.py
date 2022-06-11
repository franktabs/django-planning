from django.db import connection
from django.http import HttpRequest
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from noteManager.models import *

# Create your views here.
@api_view(['GET'])
def etudiantNoteView(req:HttpRequest, id):
    row= Evaluation.objects.raw("SELECT * FROM (SELECT * FROM evaluations WHERE etudiants_id=%s) AS evaluer INNER JOIN cours_programmes ON evaluer.ues_id=cours_programmes.ues_id INNER JOIN enseignants ON enseignants.id=cours_programmes.enseignants_id", [id])
    
    print(f"\n\n {row}\n\n")
    return Response(row)

class EvaluationViewSet(ModelViewSet):
    serializer_class = EvaluationSerializer
    queryset = Evaluation.objects.all()

    def get_serializer_class(self):
        
        if self.request.method=='POST' or self.request.method=='PUT':
            return EvaluationWriteSerializer
        else:
            return EvaluationSerializer