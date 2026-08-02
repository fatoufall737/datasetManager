"""
Module datasets/gestion.py
Partie 11 : gestion des datasets (CRUD)
"""

from stockage.csv_manager import sauvegarder_csv, charger_csv
from stockage.json_manager import sauvegarder_json, charger_json

domaines_autorises = ("Santé", "Finance", "Agriculture", "Transport", "Education")
liste_datasets = []


def ajouter_dataset():
    nom = input("Nom du dataset : ")
    domaine = input("Domaine : ")
    if domaine not in domaines_autorises:
        print(f"\nDomaine invalide ! Choisissez parmi : {domaines_autorises}\n")
        return

    try:
        lignes = int(input("Nombre de lignes : "))
        colonnes = int(input("Nombre de colonnes : "))
        taille = float(input("Taille en Mo : "))
    except ValueError:
        print("\nErreur : vous devez saisir un nombre valide. Ajout annulé.\n")
        return

    format_dataset = input("Format (csv ou json) : ")
    public_saisie = input("Public (true ou false) : ")
    public = public_saisie.strip().lower() == "true"

    dataset = {
        "nom": nom,
        "domaine": domaine,
        "lignes": lignes,
        "colonnes": colonnes,
        "taille": taille,
        "format": format_dataset,
        "public": public
    }
    liste_datasets.append(dataset)

    print("\n===== Résumé du dataset =====")
    print(f"Nom       : {dataset['nom']}")
    print(f"Domaine   : {dataset['domaine']}")
    print(f"Lignes    : {dataset['lignes']}")
    print(f"Colonnes  : {dataset['colonnes']}")
    print(f"Taille    : {dataset['taille']} Mo")
    print(f"Format    : {dataset['format'].upper()}")
    print(f"Public    : {dataset['public']}")
    print("==============================")


def afficher_datasets():
    if not liste_datasets:
        print("\nAucun dataset enregistré pour le moment.\n")
    else:
        print("\n===== Liste des datasets =====")
        for d in liste_datasets:
            print(f"- {d['nom']} | {d['domaine']} | {d['lignes']} lignes | {d['colonnes']} colonnes | {d['taille']} Mo | {d['format'].upper()} | Public: {d['public']}")
        print("==============================\n")


def rechercher_dataset():
    nom_recherche = input("\nNom du dataset à rechercher : ")
    for d in liste_datasets:
        if d['nom'].lower() == nom_recherche.lower():
            print(f"\nTrouvé : {d['nom']} | {d['domaine']} | {d['lignes']} lignes | {d['colonnes']} colonnes | {d['taille']} Mo | {d['format'].upper()} | Public: {d['public']}\n")
            return
    print(f"\nAucun dataset trouvé avec le nom '{nom_recherche}'.\n")


def trier_dataset():
    if not liste_datasets:
        print("\nAucun dataset à trier.\n")
    else:
        liste_datasets.sort(key=lambda d: d['nom'].lower())
        print("\n===== Datasets triés par nom =====")
        for d in liste_datasets:
            print(f"- {d['nom']} | {d['domaine']} | {d['lignes']} lignes")
        print("==============================\n")


def modifier_dataset():
    nom_modif = input("\nNom du dataset à modifier : ")
    for d in liste_datasets:
        if d['nom'].lower() == nom_modif.lower():
            print(f"Dataset actuel : {d}")
            nouveau_domaine = input("Nouveau domaine (laisser vide pour ne pas changer) : ")
            if nouveau_domaine.strip() != "":
                if nouveau_domaine not in domaines_autorises:
                    print(f"\nDomaine invalide ! Choisissez parmi : {domaines_autorises}\n")
                    return
                d['domaine'] = nouveau_domaine

            nouvelle_taille = input("Nouvelle taille en Mo (laisser vide pour ne pas changer) : ")
            if nouvelle_taille.strip() != "":
                try:
                    d['taille'] = float(nouvelle_taille)
                except ValueError:
                    print("\nErreur : la taille doit être un nombre. Modification de la taille annulée.\n")

            print(f"\nDataset modifié : {d}\n")
            return
    print(f"\nAucun dataset trouvé avec le nom '{nom_modif}'.\n")


def supprimer_dataset():
    nom_suppr = input("\nNom du dataset à supprimer : ")
    for d in liste_datasets:
        if d['nom'].lower() == nom_suppr.lower():
            liste_datasets.remove(d)
            print(f"\nDataset '{nom_suppr}' supprimé avec succès.\n")
            return
    print(f"\nAucun dataset trouvé avec le nom '{nom_suppr}'.\n")


def sauvegarder():
    sauvegarder_csv(liste_datasets)


def recharger():
    global liste_datasets
    resultat = charger_csv()
    if resultat is not None:
        liste_datasets = resultat


def exporter_json():
    sauvegarder_json(liste_datasets)


def importer_json():
    global liste_datasets
    resultat = charger_json()
    if resultat is not None:
        liste_datasets = resultat