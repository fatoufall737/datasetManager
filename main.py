"""
Application Python - datasetManager
Partie 11 : Packages (main.py = point d'entrée)
Partie 12 : Bonus - export/import JSON
"""

from interface import menu
from datasets import gestion
from datasets.statistiques import statistiques

while True:
    menu.afficher_menu()
    choix = input("Votre choix : ")

    if choix == "1":
        gestion.ajouter_dataset()
    elif choix == "2":
        gestion.afficher_datasets()
    elif choix == "3":
        gestion.rechercher_dataset()
    elif choix == "4":
        gestion.trier_dataset()
    elif choix == "5":
        gestion.modifier_dataset()
    elif choix == "6":
        gestion.supprimer_dataset()
    elif choix == "7":
        statistiques(gestion.liste_datasets)
    elif choix == "8":
        gestion.sauvegarder()
    elif choix == "9":
        gestion.recharger()
    elif choix == "10":
        gestion.exporter_json()
    elif choix == "11":
        gestion.importer_json()
    elif choix == "12":
        print("\nFermeture de l'application. À bientôt !")
        break
    else:
        print("\nChoix invalide, veuillez réessayer.\n")