from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.
from .models import *

class UeViewSet(ModelViewSet):
    serializer_class = UeSerializer
    queryset = Ue.objects.all()

class GroupeViewSet(ModelViewSet):
    serializer_class = GroupeSerializer
    queryset = Groupe.objects.all()

class PlageViewSet(ModelViewSet):
    serializer_class = PlageSerializer
    queryset = Plage.objects.all()

class SpecialiteViewSet(ModelViewSet):
    serializer_class = SpecialiteSerializer
    queryset = Specialite.objects.all()

class CoursProgrammeViewSet(ModelViewSet):
    serializer_class = CoursProgrammeSerializer
    queryset = CoursProgramme.objects.all()
    
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        datas = serializer.data
        tab = []
        for i in datas:
            myjson = {}
            myjson['codeClasse']= i['classes']['code']
            myjson['cours'] = [
                {
                    'plage': i['plages']['id'] - 2,
                    'ue': i['ues']['code'],
                    'enseignant': i['enseignatns']['noms'],
                    'salle': i['salles']['code'],
                }
            ]
            tab.append(myjson)
        
        return Response(tab, 200)
            
        
        
        
    
class ClasseViewSet(ModelViewSet):
    serializer_class = ClasseSerializer
    queryset = Classe.objects.all()
    