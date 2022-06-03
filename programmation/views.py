from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .models import *


class UeViewSet(ModelViewSet):
    serializer_class = UeSerializer
    queryset = Ue.objects.all()

class ClasseGroupeViewSet(ModelViewSet):
    serializer_class = ClasseGroupeSerializer
    queryset = ClasseGroupe.objects.all()

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

    def retrieve(self, request, *args, **kwargs):
        
        cours_programme = CoursProgramme.objects.filter(
            classes_id=kwargs['pk'])
        serializer = self.serializer_class(cours_programme, many=True)

        datas = serializer.data
        tab = []
        classes = []
        for i in datas:

            if i['classes']:
                k = -1
                existes = False
                for j in classes:
                    k += 1
                    if i['classes']['code'] == j:
                        existes = True
                        tab[k]['cours'].append({
                            'plage': i['plages']['id'] - 2,
                            'ue': i['ues']['code'],
                            'enseignant': i['enseignants']['noms'],
                            'salle': i['salles']['code'],
                        })
                        break

                if not existes:

                    myjson = {}
                    myjson['id'] = i['id']
                    myjson['classes'] = i['classes']['id']
                    myjson['codeClasse'] = i['classes']['code']
                    classes.append(i['classes']['code'])
                    myjson['cours'] = [
                        {
                            'plage': i['plages']['id'] - 2,
                            'ue': i['ues']['code'],
                            'enseignant': i['enseignants']['noms'],
                            'salle': i['salles']['code'],
                        }
                    ]
                    tab.append(myjson)
        return Response(tab, 200)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        datas = serializer.data
        tab = []
        classes = []
        for i in datas:

            if i['classes']:
                k = -1
                existes = False
                for j in classes:
                    k += 1
                    if i['classes']['code'] == j:
                        existes = True
                        tab[k]['cours'].append({
                            'plage': i['plages']['id'] - 2,
                            'ue': i['ues']['code'],
                            'enseignant': i['enseignants']['noms'],
                            'salle': i['salles']['code'],
                        })
                        break

                if not existes:

                    myjson = {}
                    myjson['id'] = i['id']
                    myjson['classes'] = i['classes']['id']
                    myjson['codeClasse'] = i['classes']['code']
                    classes.append(i['classes']['code'])
                    myjson['cours'] = [
                        {
                            'plage': i['plages']['id'] - 2,
                            'ue': i['ues']['code'],
                            'enseignant': i['enseignants']['noms'],
                            'salle': i['salles']['code'],
                        }
                    ]
                    tab.append(myjson)

        return Response(tab, 200)


class ClasseViewSet(ModelViewSet):
    serializer_class = ClasseSerializer
    queryset = Classe.objects.all()


class EnseigneViewSet(ModelViewSet):
    serializer_class = EnseigneSerializer
    queryset = Enseigne.objects.all()


def enum_salle_cours(datas):
    tab = []
    salles = []

    for i in datas:

        if i['salles']:
            k = -1
            existes = False
            for j in salles:
                k += 1
                if i['salles']['code'] == j:
                    existes = True
                    tab[k]['cours'].append({
                        'plage': i['plages']['id'] - 2,
                        'ue': i['ues']['code'],
                        'enseignant': i['enseignants']['noms'],
                        'classe': i['classes']['code'],
                    })
                    break

            if not existes:

                myjson = {}
                myjson['id'] = i['id']
                myjson['salles'] = i['salles']['id']
                myjson['codeSalle'] = i['salles']['code']
                salles.append(i['salles']['code'])
                myjson['cours'] = [
                    {
                        'plage': i['plages']['id'] - 2,
                        'ue': i['ues']['code'],
                        'enseignant': i['enseignants']['noms'],
                        'classe': i['classes']['code'],
                    }
                ]
                tab.append(myjson)
    return tab


def enum_enseignant_cours(datas):

    tab = []
    enseignants = []

    for i in datas:

        if i['enseignants']:
            k = -1
            existes = False
            plage = None
            salle = None
            classe = None
            if i['plages']:
                plage = i['plages']['id']-2
            if i['salles']:
                salle = i['salles']['code']
            if i['classes']:
                classe = i['classes']['code']
            for j in enseignants:
                k += 1
                if i['enseignants']['noms'] == j:
                    existes = True

                    tab[k]['cours'].append({
                        'plage': plage,
                        'ue': i['ues']['code'],
                        'salle': salle,
                        'classe': classe,
                    })
                    break

            if not existes:

                myjson = {}
                myjson['id'] = i['id']
                myjson['enseignants'] = i['enseignants']['id']
                myjson['codeEnseignant'] = i['enseignants']['noms']
                enseignants.append(i['enseignants']['noms'])
                myjson['cours'] = [
                    {
                        'plage': plage,
                        'ue': i['ues']['code'],
                        'salle': salle,
                        'classe': classe,
                    }
                ]
                tab.append(myjson)
    return tab


def enum_classe_cours(datas):
    tab = []
    classes = []
    for i in datas:

        if i['classes']:
            k = -1
            existes = False

            plage = None
            salle = None

            if i['plages']:
                plage = i['plages']['id'] - 2
            if i['salles']:
                salle = i['salles']['code']
            for j in classes:
                k += 1
                if i['classes']['code'] == j:
                    existes = True
                    tab[k]['cours'].append({
                        'plage': plage,
                        'ue': i['ues']['code'],
                        'enseignant': i['enseignants']['noms'],
                        'salle': salle,
                    })
                    break

            if not existes:

                myjson = {}
                myjson['id'] = i['id']
                myjson['classes'] = i['classes']['id']
                myjson['codeClasse'] = i['classes']['code']
                classes.append(i['classes']['code'])
                myjson['cours'] = [
                    {
                        'plage': plage,
                        'ue': i['ues']['code'],
                        'enseignant': i['enseignants']['noms'],
                        'salle': salle,
                    }
                ]
                tab.append(myjson)
    return tab


@api_view(['GET'])
def salle_cours(req: HttpRequest):
    coursprogramme = CoursProgramme.objects.all()
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    
    datas = serializer.data
    tab = enum_salle_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def salle_cours_id(req: HttpRequest, *args, **kwargs):

    cours_programme = CoursProgramme.objects.filter(
        salles_id=kwargs['id'])
    serializer = CoursProgrammeSerializer(cours_programme, many=True)
    datas = serializer.data
    tab = enum_salle_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def enseignant_cours(req: HttpRequest):
    coursprogramme = CoursProgramme.objects.all()
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
    tab = enum_enseignant_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def enseignant_cours_id(req: HttpRequest, *args, **kwargs):
    coursprogramme = CoursProgramme.objects.filter(
        enseignants_id=kwargs['id'])
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
    tab = enum_enseignant_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def classe_cours(req: HttpRequest):
    coursprogramme = CoursProgramme.objects.all()
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
    tab = enum_classe_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def classe_cours_id(req: HttpRequest, *args, **kwargs):
    coursprogramme = CoursProgramme.objects.filter(classes_id=kwargs['id'])
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
    tab = enum_classe_cours(datas)
    return Response(tab, 200)
