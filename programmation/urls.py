
from django.urls import include, path
from .views import *
from rest_framework import routers

route = routers.SimpleRouter(False)

route.register('ue/?', UeViewSet)
route.register('specialite/?', SpecialiteViewSet)
route.register('plage/?', PlageViewSet)

route.register('groupe/?', GroupeViewSet)
route.register('classe/?', ClasseViewSet)
route.register('groupe-classe/?', ClasseGroupeViewSet)

route.register('cours-programme/?', CoursProgrammeViewSet)
# route.register('enseigne/?', EnseigneViewSet)

urlpatterns=[
    path('', include(route.urls)),
    path('salle-cours', salle_cours),
    path('salle-cours/<int:id>', salle_cours_id),
    path('enseignant-cours', enseignant_cours),
    path('enseignant-cours/<int:id>', enseignant_cours_id),
    path('classe-cours', classe_cours),
    path('classe-cours/<int:id>', classe_cours_id),
    
]