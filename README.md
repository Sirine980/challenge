# Recruitment Platform API

API REST développée avec Django et Django REST Framework pour une plateforme de recrutement.
L'application gère deux rôles : condidat et recructteur.

- Le candidat peut renseigner et consulter ses informations personnelles (profil, expériences).
- Le recruteur peut consulter les informations des candidats.

## Stack technique

- Python 3.14
- Django 6.0
- Django REST Framework
- PostgreSQL
- JWT
- OpenAPI / Swagger (drf-spectacular)

## Prérequis

- Python 3.10 
- PostgreSQL installé et lancé

## Installation

1. Cloner le repo :

```bash
git clone https://github.com/TON-USERNAME/recruitment-api.git
cd recruitment-api
```

2. Créer et activer l'environnement virtuel :

```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```

4. Créer un fichier `.env` à la racine en se basant sur `.env.example` :

```bash
SECRET_KEY=votre-cle-secrete
DEBUG=True
DB_NAME=recruitment
DB_USER=postgres
DB_PASSWORD=votre-mot-de-passe
DB_HOST=localhost
DB_PORT=5432
```

5. Créer la base de données PostgreSQL :

```sql
CREATE DATABASE recruitment;
```

6. Appliquer les migrations et créer un superutilisateur :

```bash
python manage.py migrate
python manage.py createsuperuser
```

7. Lancer le serveur :

```bash
python manage.py runserver
```

## Endpoints

### Authentification

| Méthode | URL | Description |
|---------|-----|-------------|
| POST | `/api/auth/register/` | Inscription (choix du rôle candidat/recruteur) |
| POST | `/api/auth/login/` | Connexion, renvoie un token JWT |
| POST | `/api/auth/refresh/` | Renouveler un token expiré |

### Candidat (nécessite un token avec rôle CANDIDATE)

| Méthode | URL | Description |
|---------|-----|-------------|
| GET / PUT / PATCH | `/api/me/profile/` | Consulter / modifier son profil |
| GET / POST | `/api/me/experiences/` | Lister / ajouter ses expériences |
| GET / PUT / PATCH / DELETE | `/api/me/experiences/{id}/` | Détail / modifier / supprimer une expérience |


### Recruteur (nécessite un token avec rôle RECRUITER)

| Méthode | URL | Description |
|---------|-----|-------------|
| GET | `/api/candidates/` | Liste de tous les candidats |
| GET | `/api/candidates/{id}/` | Détail d'un candidat precis |

## Documentation API

Swagger UI disponible sur : `http://localhost:8000/api/docs/`

## Diagrammes UML

Les diagrammes de classes et de cas d'utilisation sont disponibles dans le dossier `docs/`.

## Structure du projet

```
recruitment-api/
├── config/          # Configuration Django (settings, urls)
├── accounts/        # Modèle User, inscription, permissions
├── candidates/      # Modèles, serializers, vues candidat/recruteur
├── docs/            # Diagrammes UML
├── .env.example     # Modèle de variables d'environnement
├── requirements.txt # Dépendances Python
└── README.md
```