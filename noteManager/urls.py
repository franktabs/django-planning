


from django.urls import path

from noteManager.views import *


urlpatterns = [
    path('etudiant-note/<int:id>', etudiantNoteView)
]