
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
route.register('enseigne/?', EnseigneViewSet)

urlpatterns=[
    path('', include(route.urls)),
    path('salle-cours', salle_coursView),
    path('salle-cours/<int:id>', salle_cours_idView),
    path('enseignant-cours', enseignant_coursView),
    path('enseignant-cours/<int:id>', enseignant_cours_idView),
    path('classe-cours', classe_coursView),
    path('classe-cours/<int:id>', classe_cours_idView),
    path('classe-notcours', classe_notCoursView),
    path('classe-notcours/<int:id>', classe_notCours_idView),
    path('salle-libre', salle_libreView),
    path('ue-enseignant/<int:id>', ue_enseignantView)
]