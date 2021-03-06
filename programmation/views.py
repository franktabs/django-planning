from typing import AnyStr
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
    query = "SELECT * FROM ues"

    def get_serializer_class(self):
        
        if self.request.method=='POST' or self.request.method=='PUT':
            return UeWriteSerializer
        else:
            return UeSerializer

class ClasseGroupeViewSet(ModelViewSet):
    serializer_class = ClasseGroupeSerializer
    queryset = ClasseGroupe.objects.all()
    query = "SELECT * FROM classes"


class GroupeViewSet(ModelViewSet):
    serializer_class = GroupeSerializer
    queryset = Groupe.objects.all()
    query = "SELECT * FROM groupes"


class PlageViewSet(ModelViewSet):
    serializer_class = PlageSerializer
    queryset = Plage.objects.all()
    query = "SELECT * FROM plages"


class SpecialiteViewSet(ModelViewSet):
    serializer_class = SpecialiteSerializer
    queryset = Specialite.objects.all()
    query = "SELECT * FROM specialites"


class CoursProgrammeViewSet(ModelViewSet):
    queryset = CoursProgramme.objects.all()
    query = "SELECT * FROM cours_programmes"

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return CoursProgrammeWriteSerializer
        else:
            return CoursProgrammeSerializer


class ClasseViewSet(ModelViewSet):
    serializer_class = ClasseSerializer
    queryset = Classe.objects.all()
    query = "SELECT * FROM classes"


class EnseigneViewSet(ModelViewSet):
    serializer_class = EnseigneSerializer
    queryset = Enseigne.objects.all()
    query = "SELECT * FROM enseignes"


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
                        'id': i['id'],
                        'plage': i['plages']['id'],
                        'idUe': i['ues']['id'],
                        'ue': i['ues']['code'],
                        'idEnseignant': i['enseignants']['id'],
                        'enseignant': i['enseignants']['noms'],
                        'idClasse': i['classes']['id'],
                        'classe': i['classes']['code'],
                    })
                    break

            if not existes:

                myjson = {}
                myjson['salles'] = i['salles']['id']
                myjson['codeSalle'] = i['salles']['code']
                salles.append(i['salles']['code'])
                myjson['cours'] = [
                    {
                        'id': i['id'],
                        'plage': i['plages']['id'],
                        'idUe': i['ues']['id'],
                        'ue': i['ues']['code'],
                        'idEnseignant': i['enseignants']['id'],
                        'enseignant': i['enseignants']['noms'],
                        'idClasse': i['classes']['id'],
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

                    tab[k]['cours'].append(
                        {
                            'id': i['id'],
                            'plage': plage,
                            'idUe': i['ues']['id'],
                            'ue': i['ues']['code'],
                            'idSalle': i['salles']['id'] if salle else salle,
                            'salle': salle,
                            'idClasse': i['classes']['id'] if classe else classe,
                            'classe': classe,
                        }
                    )
                    break

            if not existes:

                myjson = {}
                myjson['enseignants'] = i['enseignants']['id']
                myjson['codeEnseignant'] = i['enseignants']['noms']
                enseignants.append(i['enseignants']['noms'])
                myjson['cours'] = [
                    {
                        'id': i['id'],
                        'plage': plage,
                        'idUe': i['ues']['id'],
                        'ue': i['ues']['code'],
                        'idSalle': i['salles']['id'] if salle else salle,
                        'salle': salle,
                        'idClasse': i['classes']['id'] if classe else classe,
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
                plage = i['plages']['id']

            if i['salles']:
                salle = i['salles']['code']

            for j in classes:
                k += 1
                if i['classes']['code'] == j:
                    existes = True
                    tab[k]['cours'].append({
                        'id': i['id'],
                        'plage': plage,
                        'idUe': i['ues']['id'],
                        'ue': i['ues']['code'],
                        'idEnseignant': i['enseignants']['id'],
                        'enseignant': i['enseignants']['noms'],
                        'idSalle': i['salles']['id'] if salle else salle,
                        'salle': salle,
                    })
                    break

            if not existes:

                myjson = {}
                myjson['classes'] = i['classes']['id']
                myjson['codeClasse'] = i['classes']['code']
                classes.append(i['classes']['code'])
                myjson['cours'] = [
                    {
                        'id': i['id'],
                        'plage': plage,
                        'idUe': i['ues']['id'],
                        'ue': i['ues']['code'],
                        'idEnseignant': i['enseignants']['id'],
                        'enseignant': i['enseignants']['noms'],
                        'idSalle': i['salles']['id'] if salle else salle,
                        'salle': salle,
                    }
                ]
                tab.append(myjson)
    return tab


def enum_classe_notCours(datas):
    tab = []
    classes = []
    for i in datas:

        if i['classes']:
            k = -1
            existes = False

            plage = None
            salle = None

            if i['plages']:
                plage = i['plages']['id']
                continue
            if i['salles']:
                salle = i['salles']['code']
                continue
            for j in classes:
                k += 1
                if i['classes']['code'] == j:
                    existes = True
                    tab[k]['cours'].append({
                        'id': i['id'],
                        'plage': plage,
                        'idUe': i['ues']['id'],
                        'ue': i['ues']['code'],
                        'idEnseignant': i['enseignants']['id'],
                        'enseignant': i['enseignants']['noms'],
                        'idSalle': i['salles']['id'] if salle else salle,
                        'salle': salle,
                    })
                    break

            if not existes:

                myjson = {}
                myjson['classes'] = i['classes']['id']
                myjson['codeClasse'] = i['classes']['code']
                classes.append(i['classes']['code'])
                myjson['cours'] = [
                    {
                        'id': i['id'],
                        'plage': plage,
                        'idUe': i['ues']['id'],
                        'ue': i['ues']['code'],
                        'idEnseignant': i['enseignants']['id'],
                        'enseignant': i['enseignants']['noms'],
                        'idSalle': i['salles']['id'] if salle else salle,
                        'salle': salle,
                    }
                ]
                tab.append(myjson)
    return tab




@api_view(['GET'])
def salle_coursView(req: HttpRequest):
    coursprogramme = CoursProgramme.objects.all()
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)

    datas = serializer.data
    tab = enum_salle_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def salle_cours_idView(req: HttpRequest, *args, **kwargs):

    cours_programme = CoursProgramme.objects.filter(
        salles_id=kwargs['id'])
    serializer = CoursProgrammeSerializer(cours_programme, many=True)
    datas = serializer.data
    tab = enum_salle_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def enseignant_coursView(req: HttpRequest):
    coursprogramme = CoursProgramme.objects.all()
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
    tab = enum_enseignant_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def enseignant_cours_idView(req: HttpRequest, *args, **kwargs):
    coursprogramme = CoursProgramme.objects.filter(
        enseignants_id=kwargs['id'])
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
    tab = enum_enseignant_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def classe_coursView(req: HttpRequest):
    coursprogramme = CoursProgramme.objects.all()
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
    tab = enum_classe_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def classe_cours_idView(req: HttpRequest, *args, **kwargs):
    coursprogramme = CoursProgramme.objects.filter(classes_id=kwargs['id'])
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
    tab = enum_classe_cours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def classe_notCoursView(req: HttpRequest):
    coursprogramme = CoursProgramme.objects.filter(plages_id=None)
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
    tab = enum_classe_notCours(datas)
    return Response(tab, 200)


@api_view(['GET'])
def classe_notCours_idView(req: HttpRequest, *args, **kwargs):
    coursprogramme = CoursProgramme.objects.filter(
        classes_id=kwargs['id'], plages_id=None)
    serializer = CoursProgrammeSerializer(coursprogramme, many=True)
    datas = serializer.data
    tab = enum_classe_notCours(datas)
    return Response(status=200, data=tab)


@api_view(['POST'])
def salle_libreView(req: HttpRequest):
    id_plage = req.data['plage']
    id_classe = req.data['classe']
    cours_programmes = CoursProgramme.objects.filter(plages_id=id_plage)
    salles = Salle.objects.all().order_by('capacite')
    classe = Classe.objects.filter(id=id_classe)
    all_salles = SalleSerializer(salles, many=True).data
    salles = all_salles.copy()
    eff = (float)(classe[0].effectif)
    tab = []
    if cours_programmes:
        for i in cours_programmes:
            j = 0
            for salle in salles:
                if salle['id'] == i.salles_id:
                    del salles[j]
                    break
                j += 1

    for salle in salles:
        cap = (float)(salle['capacite'])
        if (eff - eff*0.2 <= cap and cap <= eff + eff/2):
            tab.append(
                {
                    'id': salle['id'],
                    'code': salle['code'],
                    'nom': salle['nom'],
                    'etat_electricite': salle["etat_electricite"],
                    'capacite': salle['capacite'],
                })

    return Response(tab)


@api_view(['GET'])
def ue_enseignantView(req: HttpRequest, id):
    ues = CoursProgramme.objects.filter(ues_id=id)
    serializer = CoursProgrammeSerializer(ues, many=True)
    tab = []
    for i in serializer.data:
        tab.append({
            'id': i['id'],
            'idUe': i['ues']['id'],
            'ue': i['ues']['code'],
            'idEnseignant': i['enseignants']['id'],
            'enseignant': i['enseignants']['noms']
        })
    return Response(tab)


@api_view(['GET'])
def departement_enseignantView(req: HttpRequest, id):
    cours = CoursProgramme.objects.filter(ues_id=id)
    serializer = CoursProgrammeSerializer(cours, many=True)
    tab = []
    exist = []
    for i in serializer.data:
        tab.append({
            'id': i['id'],
            'idUe': i['ues']['id'],
            'ue': i['ues']['code'],
            'idEnseignant': i['enseignants']['id'],
            'enseignant': i['enseignants']['noms']
        })
        exist.append(i['enseignants']['id'])

    depart = None
    for i in serializer.data:
        depart = i['classes']['departements']['id']
        if depart:
            print('\n\n 436 execution {}\n\n'.format(depart))
            enseignants = Enseignant.objects.filter(departements_id=depart)
            for j in enseignants:
                if not (j.id in exist):
                    tab.append({
                        'id': i['id'],
                        'idUe': i['ues']['id'],
                        'ue': i['ues']['code'],
                        'idEnseignant': j.id,
                        'enseignant': j.noms
                    })
        break
    
    return Response(tab)

@api_view(['POST'])
def enseignant_libreView(req:HttpRequest):
    cours = CoursProgramme.objects.filter(enseignants_id=req.data['enseignants'], plages_id=req.data['plages'])
    existe = True if cours else False
    tab=[]
    if cours:
        existe=True
        cours = CoursProgrammeSerializer(cours, many=True)
        for i in cours.data:
            tab.append({
                'result': existe,
                'message': ' {} de {} en {} '.format(i['plages']['jour'], i['plages']['periode'], i['classes']['code'])
            })
    else:
        existe=False
        tab.append({
            'result': existe,
        })
            
            
    return Response(tab)