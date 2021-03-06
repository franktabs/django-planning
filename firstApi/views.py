from abc import ABC
from copy import deepcopy
from pprint import pprint
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
from firstApi.models import *


# Create your views here.
# @api_view(['GET', 'POST'])
# def etudiantView(req:HttpRequest):
#     if(req.method=="GET"):
#         etudiants = Etudiant.objects.all()
#         etudiants = EtudiantSerializer(etudiants, many=True)
#         return Response(etudiants.data)
#     if(req.method == "POST"):
#         etudiants = EtudiantSerializer(data=req.data)
#         print("\n\n")
#         print(etudiants.is_valid())
#         print("Exectution")
#         print("\n\n")
        
#         if(not etudiants.is_valid()):
#             return Response({"errors": etudiants.errors}, 400)
#         etudiants.save()
#         return Response(etudiants.data)
        


# @api_view(['GET'])
# def salleView(req:HttpRequest):
    
#     if(req.method=='GET'):
#         salles = Salle.objects.all()

class UtilisateurViewSet(ABC, ModelViewSet):
    serializer_class = ""
    queryset = ""
    mymodel = ""
    
    def create(self, req:HttpRequest, *args, **kwargs):
        utilisateur_test = self.serializer_class(data=req.data)
        utilisateur_test.is_valid(raise_exception=True)
        datas = deepcopy(req.data)
        datas['password']= make_password(datas['password'])
        utilisateur = self.serializer_class(data=datas)
        utilisateur.is_valid()
        utilisateur.save()
        utilisateur = self.mymodel.objects.filter(email=req.data['email'])
        utilisateur_test = self.serializer_class(utilisateur, many=True)
        
        # print('\n\n')
        # print(check_password(req.data['password'], datas['password']))
        # utilisateur_test.save()
        # value = {}
        # for k in utilisateur_test.data:
        #     if k != 'password':
        #         value[k]=utilisateur_test.data[k]
        return Response(utilisateur_test.data, status=201)

class SalleViewSet(ModelViewSet):
    queryset = Salle.objects.all()
    
    def get_serializer_class(self):
        
        if self.request.method=='POST' or self.request.method=='PUT':
            return SalleWriteSerializer
        else:
            return SalleSerializer
    
    # def list(self, request, *args, **kwargs):
        # SalleSerializer.batiments()
        # SalleSerializer.type_salles()
    #     serializer = SalleSerializer(self.queryset, many=True)
        
    #     return Response(serializer.data)

class EtudiantViewSet(UtilisateurViewSet):
    serializer_class = EtudiantSerializer
    queryset = Etudiant.objects.all()
    mymodel = Etudiant
    def create(self, req: HttpRequest, *args, **kwargs):
        return super().create(req, *args, **kwargs)
    
    def get_serializer_class(self):
        if self.request.method=='POST' or self.request.method=='PUT':
            return EtudiantWriteSerializer
        else:
            return EtudiantSerializer

class RessourceViewSet(ModelViewSet):
    serializer_class = RessourceSerializer
    queryset = Ressource.objects.all()
    
    def get_serializer_class(self):
        if self.request.method=='POST' or self.request.method=='PUT':
            return RessourceWriteSerializer
        else:
            return RessourceSerializer

class TypeRessourceViewSet(ModelViewSet):
    serializer_class = TypeRessourceSerializer
    queryset = TypeRessource.objects.all()

class FaculteViewSet(ModelViewSet):
    serializer_class = FaculteSerializer
    queryset = Faculte.objects.all()

class BatimentViewSet(ModelViewSet):
    serializer_class = BatimentSerializer
    queryset = Batiment.objects.all()
    
    def get_serializer_class(self):
        if self.request.method=='POST' or self.request.method=='PUT':
            return BatimentWriteSerializer
        else:
            return BatimentSerializer
    
    
class TypeSalleViewSet(ModelViewSet):
    serializer_class = TypeSalleSerializer
    queryset = TypeSalle.objects.all()
    


class DepartementViewSet(ModelViewSet):
    serializer_class = DepartementSerializer
    queryset = Departement.objects.all()
    
    def get_serializer_class(self):
        if self.request.method=='POST' or self.request.method=='PUT':
            return DepartementWriteSerializer
        else:
            return DepartementSerializer
    
class EnseignantViewSet(UtilisateurViewSet):
    serializer_class = EnseignantSerializer
    queryset = Enseignant.objects.all()
    mymodel = Enseignant
    
    def create(self, req: HttpRequest, *args, **kwargs):
        return super().create(req, *args, **kwargs)
    
    def get_serializer_class(self):
        if self.request.method=='POST' or self.request.method=='PUT':
            return EnseignantWriteSerializer
        else:
            return EnseignantSerializer

@api_view(['POST'])
def utilisateurView(req:HttpRequest):
    UtilisateurSerializer(data=req.data).is_valid(raise_exception=True)
    print('\n\n',req.data['email'])
    print('\n\n')
    etudiants = Etudiant.objects.filter(email=req.data['email'])
    if(etudiants):
        for etudiant in etudiants.values():
            if(check_password(req.data['password'], etudiant['password'] )):
                etudiant = EtudiantSerializer(etudiants, many=True)
                return Response(etudiant.data)
        return Response({'errors': 'password is incorrect'}, 400)
    enseignants = Enseignant.objects.filter(email=req.data['email'])
    if(enseignants):
        for enseignant in enseignants.values():
            if(check_password(req.data['password'], enseignant['password'] )):
                enseignant = EnseignantSerializer(enseignants, many=True)
                return Response(enseignant.data)
        return Response({'password is incorrect'}, 400)
        
    return Response({'user does\'nt exist'}, 400)

@api_view(['GET'])
def batiments_sallesView(req:HttpRequest):
    batiments = Batiment.objects.all()
    batiments = BatimentSerializer(batiments, many=True).data
    new_batiments = batiments.copy()
    table = []
    for batiment in new_batiments:
        salles = Salle.objects.filter(batiments_id=batiment['id'])
        if salles: 
            salles = SalleSerializer(salles, many=True).data
            batiment['salles']= salles
            table.append(batiment)
        else:
            table.append(batiment)
    return Response(table)

@api_view(['GET'])
def facultes_batimentsView(req:HttpRequest):
    facultes = Faculte.objects.all()
    facultes = FaculteSerializer(facultes, many=True).data
    new_facultes = facultes.copy()
    table = []
    for faculte in new_facultes:
        batiment = Batiment.objects.filter(facultes_id=faculte['id'])
        if batiment: 
            batiment = BatimentSerializer(batiment, many=True).data
            faculte['batiment']= batiment
            table.append(faculte)
        else:
            table.append(faculte)
    return Response(table)

@api_view(['GET'])
def type_salleView(req:HttpRequest):
    type_salles = TypeSalle.objects.all()
    type_salles = TypeSalleSerializer(type_salles, many=True).data
    new_type_salles = type_salles.copy()
    table = []
    for type_salle in new_type_salles:
        salle = Salle.objects.filter(type_salles_id=type_salle['id'])
        if salle: 
            salle = SalleSerializer(salle, many=True).data
            type_salle['salle']= salle
            table.append(type_salle)
        else:
            table.append(type_salle)
            
    return Response(table)

