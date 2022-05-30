from django.contrib import admin

from .model.batiment import Batiment
from .model.classe import Classe
from .model.faculte import Faculte
from .model.etudiant import Etudiant
from .model.salle import Salle
from .model.enseignant import Enseignant
from .model.type_ressource import TypeRessource
from .model.ressource import Ressource
from .model.type_salle import TypeSalle



# Register your models here.

admin.site.register(Etudiant)
admin.site.register(Classe)
admin.site.register(Salle)
admin.site.register(Faculte)
admin.site.register(TypeSalle)
admin.site.register(Batiment)
admin.site.register(Ressource)
admin.site.register(TypeRessource)
admin.site.register(Enseignant)



