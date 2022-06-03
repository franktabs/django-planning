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


@api_view(['GET'])
def salle_cours(req: HttpRequest):
    coursprogramme = CoursProgramme.objects.all()
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
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

    return Response(tab, 200)


@api_view(['GET'])
def salle_cours_id(req: HttpRequest, *args, **kwargs):
    
    cours_programme = CoursProgramme.objects.filter(
            classes_id=kwargs['id'])
    serializer = CoursProgrammeSerializer(cours_programme, many=True)
    datas = serializer.data
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

    return Response(tab, 200)
    
    