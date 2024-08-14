# Application de Gestion de Tâches Django

## 🚀 Aperçu

Ce projet présente une application web robuste et élégante de gestion de tâches, construite avec Django et déployée sur Azure. Elle démontre l'utilisation des meilleures pratiques en matière de développement web, d'intégration continue et de déploiement continu (CI/CD).

## 🌟 Caractéristiques Principales

- 👤 Authentification utilisateur sécurisée
- ✅ Création, lecture, mise à jour et suppression (CRUD) des tâches
- 🔢 Système de priorité pour les tâches
- 🔍 Filtrage avancé des tâches
- 📱 Interface responsive avec Bootstrap
- 🔒 Sécurité renforcée avec Django
- 🚀 Pipeline CI/CD avec Azure DevOps

## 🛠 Technologies Utilisées

- **Backend**: Django 3.2 (LTS)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Base de données**: PostgreSQL
- **Déploiement**: Azure App Service
- **CI/CD**: Azure Pipelines
- **Contrôle de version**: Git

## 🏗 Architecture

L'application suit une architecture MVC (Model-View-Controller) avec Django :

- **Models**: Définition des structures de données pour les tâches
- **Views**: Logique de traitement des requêtes HTTP
- **Templates**: Rendu de l'interface utilisateur
- **Forms**: Gestion de la validation des données utilisateur

## 🔧 Installation et Configuration

1. Clonez le repository
   ```bash
   git clone https://github.com/votre-username/taskmaster-pro.git
   ```

2. Installez les dépendances
   ```bash
   pip install -r requirements.txt
   ```

3. Configurez la base de données dans `settings.py`

4. Appliquez les migrations
   ```bash
   python manage.py migrate
   ```

5. Lancez le serveur de développement
   ```bash
   python manage.py runserver
   ```

## 🚀 Déploiement

L'application est configurée pour un déploiement automatique sur Azure App Service via Azure Pipelines. Chaque push sur la branche principale déclenche :

1. L'exécution des tests unitaires
2. L'analyse de la couverture de code
3. Le linting du code avec Flake8
4. Le déploiement sur Azure si tous les tests passent

## 🧪 Tests

Le projet inclut une suite de tests unitaires et d'intégration. Pour exécuter les tests :

```bash
python manage.py test
```

Pour générer un rapport de couverture :

```bash
coverage run manage.py test
coverage report
```

## 📈 Améliorations Futures

- Intégration de rappels par email pour les tâches en retard
- Ajout de tags pour une meilleure organisation des tâches
- Implémentation d'une API RESTful pour l'intégration avec des applications mobiles
- Intégration avec des services de calendrier externes
