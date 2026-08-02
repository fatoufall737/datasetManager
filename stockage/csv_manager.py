"""
Module stockage/csv_manager.py
Partie 11 : lecture/écriture du fichier CSV
"""

import csv


def sauvegarder_csv(liste_datasets, chemin="data/datasets.csv"):
    try:
        with open(chemin, "w", newline="", encoding="utf-8") as fichier:
            ecrivain = csv.DictWriter(fichier, fieldnames=["nom", "domaine", "lignes", "colonnes", "taille", "format", "public"])
            ecrivain.writeheader()
            for d in liste_datasets:
                ecrivain.writerow(d)
        print(f"\nDonnées sauvegardées dans {chemin}\n")
    except OSError:
        print(f"\nErreur : impossible d'écrire dans le fichier {chemin}.\n")


def charger_csv(chemin="data/datasets.csv"):
    try:
        with open(chemin, "r", newline="", encoding="utf-8") as fichier:
            lecteur = csv.DictReader(fichier)
            nouvelle_liste = []
            for ligne in lecteur:
                ligne["lignes"] = int(ligne["lignes"])
                ligne["colonnes"] = int(ligne["colonnes"])
                ligne["taille"] = float(ligne["taille"])
                ligne["public"] = ligne["public"] == "True"
                nouvelle_liste.append(ligne)

        if not nouvelle_liste:
            print(f"\nLe fichier {chemin} est vide, aucun dataset à recharger.\n")
            return None
        else:
            print(f"\n{len(nouvelle_liste)} dataset(s) rechargé(s) depuis {chemin}\n")
            return nouvelle_liste

    except FileNotFoundError:
        print(f"\nLe fichier {chemin} n'existe pas encore. Sauvegardez d'abord.\n")
        return None