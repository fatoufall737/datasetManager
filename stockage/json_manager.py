"""
Module stockage/json_manager.py
Partie 12 : Bonus - export/import au format JSON
"""

import json


def sauvegarder_json(liste_datasets, chemin="data/datasets.json"):
    try:
        with open(chemin, "w", encoding="utf-8") as fichier:
            json.dump(liste_datasets, fichier, indent=4, ensure_ascii=False)
        print(f"\nDonnées exportées dans {chemin}\n")
    except OSError:
        print(f"\nErreur : impossible d'écrire dans le fichier {chemin}.\n")


def charger_json(chemin="data/datasets.json"):
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            nouvelle_liste = json.load(fichier)

        if not nouvelle_liste:
            print(f"\nLe fichier {chemin} est vide, aucun dataset à importer.\n")
            return None
        else:
            print(f"\n{len(nouvelle_liste)} dataset(s) importé(s) depuis {chemin}\n")
            return nouvelle_liste

    except FileNotFoundError:
        print(f"\nLe fichier {chemin} n'existe pas encore. Exportez d'abord.\n")
        return None
    except json.JSONDecodeError:
        print(f"\nErreur : le fichier {chemin} est mal formé (JSON invalide).\n")
        return None