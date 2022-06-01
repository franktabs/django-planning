

from django.urls import include, path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)

router.register('etudiant/?', EtudiantViewSet)
router.register('ressource/?', RessourceViewSet)
router.register('salle/?', SalleViewSet)
router.register('typeSalle/?', TypeSalleViewSet)
router.register('typeRessource/?', TypeRessourceViewSet)
router.register('faculte/?', FaculteViewSet)
router.register('batiment/?', BatimentViewSet)
router.register('enseignant/?', EnseignantViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('utilisateur', utilisateurView),
    path('batiment-salle', batiments_sallesView),
    path('faculte-batiment', facultes_batimentsView)
]
