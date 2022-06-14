from django.db import connection
from django.http import HttpRequest
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from noteManager.models import *


def afficheNote(valeur):
    if(not valeur):
        return "/"
    elif(valeur < 0):
        return "EL"
    else:
        return valeur
# Create your views here.
@api_view(['GET'])
def etudiantNoteView(req:HttpRequest, id):
    row= Evaluation.objects.raw("SELECT evaluer.id, cc, tp, ee, cours_programmes.ues_id FROM (SELECT * FROM evaluations WHERE etudiants_id=%s) AS evaluer INNER JOIN cours_programmes ON evaluer.ues_id=cours_programmes.ues_id ", [id])
    tab=[]
    serializer = EvaluationSerializer(row, many=True)
    
    
    for i in serializer.data :
        tab.append({
            'cc': afficheNote(i["cc"]),
            'tp': afficheNote(i["tp"]),
            'ee': afficheNote(i['ee']),
            'email': i["ues"]["enseignants"][0]["email"],
            'module_code': i["ues"]["code"],
        })
    
    print(f'\n{tab}\n')
    return Response(tab)

class EvaluationViewSet(ModelViewSet):
    serializer_class = EvaluationSerializer
    queryset = Evaluation.objects.all()

    def get_serializer_class(self):
        
        if self.request.method=='POST' or self.request.method=='PUT':
            return EvaluationWriteSerializer
        else:
            return EvaluationSerializer