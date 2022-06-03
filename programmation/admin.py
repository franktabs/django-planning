from django.contrib import admin
# from programmation.model.classes_groupe import ClassesGroupe, Groupe
# from programmation.model.cours_programme import CoursProgramme
# from programmation.model.plage import Plage

# from programmation.model.specialite import Specialite
# from programmation.model.ue import Ue

from .models import *

# Register your models here.
admin.site.register(Classe)
admin.site.register(Specialite)
admin.site.register(Ue)
admin.site.register(Plage)
admin.site.register(Groupe)
admin.site.register(CoursProgramme)
admin.site.register(ClassesGroupe)
admin.site.register(Enseignes)