# 📊 datasetManager

Application Python en ligne de commande pour gérer des métadonnées de datasets (nom, domaine, nombre de lignes/colonnes, taille, format, visibilité publique/privée).

Projet réalisé dans le cadre du module **P1 IA**.
**Auteure :** Fatou Fall

---

## 🧭 Sommaire

- [Aperçu](#-aperçu)
- [Fonctionnalités](#-fonctionnalités)
- [Structure du projet](#-structure-du-projet)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Progression du projet](#-progression-du-projet)

---

## 🔎 Aperçu

`datasetManager` est une application console permettant de cataloguer des jeux de données (datasets) : les ajouter, les afficher, les rechercher, les trier, les modifier, les supprimer, calculer des statistiques globales, et sauvegarder/recharger les données depuis des fichiers CSV ou JSON.

Le projet a été développé de façon progressive, en partant des bases du langage Python jusqu'à une architecture organisée en packages.

---

## ✨ Fonctionnalités

- ➕ Ajout d'un dataset (nom, domaine, lignes, colonnes, taille, format, visibilité)
- 📋 Affichage de la liste des datasets enregistrés
- 🔍 Recherche d'un dataset par nom
- ↕️ Tri des datasets
- ✏️ Modification d'un dataset existant
- 🗑️ Suppression d'un dataset
- 📈 Statistiques globales : nombre de datasets, total de lignes, moyenne de colonnes, répartition par domaine, nombre de datasets publics/privés, répartition par format (CSV/JSON)
- 💾 Sauvegarde et rechargement des données via un fichier `datasets.csv`
- 🎁 **Bonus :** export/import des datasets au format JSON
- ✅ Validation du domaine saisi par rapport à une liste de domaines autorisés (Santé, Finance, Agriculture, Transport, Éducation)
- 🛡️ Gestion des erreurs (saisie invalide, fichier introuvable, dataset introuvable) pour que l'application ne plante jamais


---

## 🗂️ Structure du projet

datasetManager/
├── main.py                  (Point d'entrée de l'application)
├── data/
│   ├── datasets.csv
│   └── datasets.json
├── datasets/
│   ├── __init__.py
│   ├── gestion.py            (Ajout, recherche, tri, modification, suppression)
│   └── statistiques.py       (Calcul des statistiques)
├── interface/
│   ├── __init__.py
│   └── menu.py                (Affichage du menu interactif)
└── stockage/
    ├── __init__.py
    ├── csv_manager.py         (Sauvegarde / rechargement CSV)
    └── json_manager.py        (Export / import JSON, bonus)

---

## ⚙️ Prérequis

- Python 3.10 ou version ultérieure

---

## 🚀 Installation

git clone https://github.com/fatoufall737/datasetManager.git
cd datasetManager
python main.py

---

## ▶️ Utilisation

Au lancement, un menu interactif s'affiche avec les options : Ajouter, Afficher, Rechercher, Trier, Modifier, Supprimer, Statistiques, Sauvegarder, Recharger, Quitter.

Il suffit de saisir le numéro correspondant à l'action souhaitée et de suivre les instructions à l'écran.

---

## 📚 Progression du projet

Le projet a été construit étape par étape, chaque partie correspondant à une notion Python :

| Partie | Notion | Description |
|--------|--------|-------------|
| 1 | Types de base, variables, E/S | Saisie des métadonnées et affichage d'un résumé formaté |
| 2 | Structures de contrôle | Menu interactif avec boucle while |
| 3 | Dictionnaires | Regroupement des métadonnées dans un dictionnaire |
| 4 | Tuples | Vérification du domaine par rapport à un tuple de domaines autorisés |
| 5 | Listes | Stockage des datasets et fonctionnalités CRUD |
| 6 | Compréhensions | Calcul de statistiques via des compréhensions |
| 7 | Fichiers | Sauvegarde et rechargement des datasets depuis datasets.csv |
| 8 | Exceptions | Gestion des erreurs de saisie, fichier introuvable, dataset introuvable |
| 9 | Fonctions | Refactorisation : chaque fonctionnalité isolée dans sa propre fonction |
| 10 | Modules | Découpage du code en plusieurs fichiers |
| 11 | Packages | Organisation en packages |
| 12 | Bonus | Export/import des datasets au format JSON |

---

## 📎 Livrable complet

Le document de présentation détaillé du projet, avec les captures d'écran de chaque partie, est disponible ici :

📄 [datasetManager_livrable.pdf](./datasetManager_livrable.pdf)

---

## 📄 Licence

Projet académique — libre d'utilisation à des fins pédagogiques.
