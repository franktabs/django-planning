
from firstApi.model.departement import *
from firstApi.model.salle import Salle, SalleSerializer
from firstApi.model.utilisateur import Enseignant, EnseignantSerializer
from programmation.model.plage import Plage, PlageSerializer
from programmation.model.ue import Ue, UeSerializer

class Groupe(models.Model):
    code = models.CharField(max_length = 45, unique=True, null=False)
    nom = models.CharField(max_length = 45)
    # classes = models.ManyToManyField('Classe', through='groupes_classes', related_name='groupes', )
    
    class Meta:
        db_table = 'groupes'
    
    def __str__(self):
        return self.code
    
class GroupeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Groupe
        fields = "__all__"
    
# _____________________________________________________________________________________________________


# _______________________________________________________________________________________________________
class Classe(models.Model):
    code = models.CharField(unique=True, max_length=45, null=False)
    effectif = models.IntegerField()
    departements = models.ForeignKey(Departement, on_delete=models.PROTECT)
    groupes = models.ManyToManyField(Groupe, through="ClassesGroupe", related_name='classes')
    
    enseignants= models.ManyToManyField(Enseignant, through='CoursProgramme', related_name='plages')
    ues = models.ManyToManyField(Ue, through='CoursProgramme', related_name='plages')
    salles= models.ManyToManyField(Salle, through='CoursProgramme', related_name='plages')
    plages = models.ManyToManyField(Plage, through='CoursProgramme', related_name='plages')
    
    
    class Meta:
        db_table = 'classes'
    
    def __str__(self):
        return self.code


class ClasseSerializer(serializers.ModelSerializer):
    departements = DepartementSerializer(read_only=True)

    enseignants= EnseignantSerializer(many=True)
    ues = UeSerializer(many=True)
    salles= SalleSerializer(many=True)
    plages = PlageSerializer(many=True)
    class Meta:
        model = Classe
        fields = "__all__"

# ________________________________________________________________________________________________________

# _________________________________________________________________________________________________________

class ClassesGroupe(models.Model):
    groupes = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classe, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "classes_groupes"
    

class ClassesGroupeSerializer(serializers.ModelSerializer):
    groupes = GroupeSerializer()
    classes = ClasseSerializer()
    class Meta:
        model = ClassesGroupe
        fields = '__all__'
        

# _____________________________________________________________________________________