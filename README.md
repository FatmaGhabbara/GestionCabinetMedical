# GestionCabinetMedical

Application de gestion d'un cabinet médical réalisée avec Django. Les noms existants du projet et des applications (`Cabinet`, `RendezVous`, `GestionCabinetMedical`) sont conservés.

## Fonctionnalités
- Connexion / déconnexion et tableau de bord.
- Gestion CRUD des patients et médecins.
- Gestion des spécialités médicales.
- Gestion des rendez-vous : création, consultation, modification, suppression et filtre par statut.
- Interface d'administration Django.
- Validation des numéros, CIN et dates de naissance définie dans les modèles existants.

## Installation
Python 3.10+ recommandé. Dans le dossier qui contient `manage.py` :

```bash
python -m venv venv
# Windows : venv\Scripts\activate
# Linux/macOS : source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations RendezVous
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ouvrir http://127.0.0.1:8000/ puis se connecter avec le compte créé. Administration : http://127.0.0.1:8000/admin/ .

## Note sur les comptes
Les formulaires d'ajout de médecins et patients créent les comptes correspondants. Un mot de passe est nécessaire pour permettre leur connexion.
