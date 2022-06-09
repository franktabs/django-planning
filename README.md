
# BACKEND API

- depot github: 

         https://github.com/franktabs/django-planning/settings

- api deployer en ligne à l'url:  https://server-planning.herokuapp.com

Exemple de visualisation de l'api deployer qui fourni les différentes salles : 

         https://server-planning.herokuapp.com/api/salle

-------------------------------------------------------
GESTION DU PLANNING COTE BACKEND
_______________________________________________________

PREREQUIS:

- Python installé mis à jour
- Système d'exploitation Ubuntu mis à jour
- Connexion Internet

DEPLOYER LE SERVEUR

Pour deployer l'application étant à la racine du dossier contenant le fichier manage.py à l'aide de l'invite de commande : 


- lancer 

         python3 -m venv .env 
_______________________________________________________
- lancer  

         pip install --upgrade pip 
_______________________________________________________
- lancer 

         pip install -r requirements.txt
_______________________________________________________
- lancer 

         source .env/bin/active 
_______________________________________________________
- lancer 

         python manage.py runserver 0.0.0.0:8000 


Le serveur étant lancer on peut y acceder via le frontend de l'application

NB: Le code de la BASE DE DONNEES se trouve dans le fichier sql planning-backend.sql du même repertoire que manage.py