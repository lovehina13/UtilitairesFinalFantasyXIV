# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/__main__.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition du programme principal
# ==================================================================================================

if __name__ == "__main__":

#     from UtilitairesFinalFantasyXIV.Traitements.Personnage import TraitementPagePersonnages
#     TraitementPagePersonnages("9233364398528028107", 1, "Personnages.csv").executer()
#     from UtilitairesFinalFantasyXIV.Traitements.Recette import TraitementPageRecettes
#     TraitementPageRecettes(182, "Recettes.csv").executer()
#     from UtilitairesFinalFantasyXIV.Traitements.Recolte import TraitementPageRecoltes
#     TraitementPageRecoltes(18, "Recoltes.csv").executer()
#
#     from UtilitairesFinalFantasyXIV.Collections.Personnage import CollectionPersonnages
#     c1 = CollectionPersonnages(None, "Personnages.csv")
#     c1.charger()
#     c1.sauver()
#     from UtilitairesFinalFantasyXIV.Collections.Recette import CollectionRecettes
#     c2 = CollectionRecettes(None, "Recettes.csv")
#     c2.charger()
#     c2.sauver()
#     from UtilitairesFinalFantasyXIV.Collections.Recolte import CollectionRecoltes
#     c3 = CollectionRecoltes(None, "Recoltes.csv")
#     c3.charger()
#     c3.sauver()

    from UtilitairesFinalFantasyXIV.Structure.Filtre import Filtre, Filtres
    f1 = Filtres()
    f1.ajouter(Filtre("nom", ["Virbyker Tinkle", "Cerillyanne Tinkle"]))
    f2 = Filtres()
    f2.ajouter(Filtre("classe", ["Couturier"]))
    f2.ajouter(Filtre("niveau", [1, 2, 3, 4, 5]))
    f3 = Filtres()
    f3.ajouter(Filtre("classe", ["Botaniste"]))
    f3.ajouter(Filtre("niveau", [1, 2, 3, 4, 5]))
    from UtilitairesFinalFantasyXIV.Traitements.Personnage import TraitementGestionPersonnages
    t11 = TraitementGestionPersonnages("Personnages.csv", "Personnages_out.csv", f1, False)
    t12 = TraitementGestionPersonnages("Personnages.csv", "Personnages_out.txt", f1, True)
    t11.executer()
    # t12.executer()
    from UtilitairesFinalFantasyXIV.Traitements.Recette import TraitementGestionRecettes
    t21 = TraitementGestionRecettes("Recettes.csv", "Recettes_out.csv", f2, False)
    t22 = TraitementGestionRecettes("Recettes.csv", "Recettes_out.txt", f2, True)
    t21.executer()
    # t22.executer()
    from UtilitairesFinalFantasyXIV.Traitements.Recolte import TraitementGestionRecoltes
    t31 = TraitementGestionRecoltes("Recoltes.csv", "Recoltes_out.csv", f3, False)
    t32 = TraitementGestionRecoltes("Recoltes.csv", "Recoltes_out.txt", f3, True)
    t31.executer()
    # t32.executer()
