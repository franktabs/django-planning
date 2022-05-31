
from django.urls import include, path
from .views import *
from rest_framework import routers

route = routers.SimpleRouter(False)

route.register('ue/?', UeViewSet)
route.register('specialite/?', SpecialiteViewSet)
route.register('plage/?', PlageViewSet)
route.register('groupe/?', GroupeViewSet)

urlpatterns=[
    path('', include(route.urls))
]