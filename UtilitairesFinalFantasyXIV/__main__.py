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

    from UtilitairesFinalFantasyXIV.Collections.Personnage import CollectionPersonnages
    x1 = CollectionPersonnages(None, "Personnages.csv")
    x1.charger()
    x1.sauver()
    from UtilitairesFinalFantasyXIV.Collections.Recette import CollectionRecettes
    x2 = CollectionRecettes(None, "Recettes.csv")
    x2.charger()
    x2.sauver()
    from UtilitairesFinalFantasyXIV.Collections.Recolte import CollectionRecoltes
    x3 = CollectionRecoltes(None, "Recoltes.csv")
    x3.charger()
    x3.sauver()
