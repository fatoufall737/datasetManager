"""
Module datasets/statistiques.py
Partie 11 : calcul et affichage des statistiques
"""


def statistiques(liste_datasets):
    if not liste_datasets:
        print("\nAucun dataset pour calculer des statistiques.\n")
        return

    nb_datasets = len(liste_datasets)
    total_lignes = sum(d['lignes'] for d in liste_datasets)
    moyenne_colonnes = sum(d['colonnes'] for d in liste_datasets) / nb_datasets
    nb_publics = sum(1 for d in liste_datasets if d['public'])
    nb_prives = nb_datasets - nb_publics
    nb_csv = sum(1 for d in liste_datasets if d['format'].lower() == "csv")
    nb_json = sum(1 for d in liste_datasets if d['format'].lower() == "json")

    repartition = {}
    for d in liste_datasets:
        dom = d['domaine']
        repartition[dom] = repartition.get(dom, 0) + 1

    print("\n===== Statistiques =====")
    print(f"Nombre de datasets : {nb_datasets}")
    print(f"Nombre total de lignes : {total_lignes}")
    print(f"Nombre moyen de colonnes : {moyenne_colonnes:.0f}")
    print(f"Datasets publics : {nb_publics}")
    print(f"Datasets privés : {nb_prives}")
    print(f"Nombre de datasets au format CSV : {nb_csv}")
    print(f"Nombre de datasets au format JSON : {nb_json}")
    print("Répartition par domaine :")
    for dom, count in repartition.items():
        print(f"  {dom} : {count}")
    print("==========================\n")