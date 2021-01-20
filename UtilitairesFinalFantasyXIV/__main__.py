# coding: utf-8

# ==================================================================================================
# Name        : __main__.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition du programme principal
# ==================================================================================================

if __name__ == '__main__':

#     from UtilitairesFinalFantasyXIV.Traitements.Personnage import TraitementPagePersonnages
#     TraitementPagePersonnages("9233364398528028107", 1, "Personnages.csv").executer()
#     from UtilitairesFinalFantasyXIV.Traitements.Recette import TraitementPageRecettes
#     TraitementPageRecettes(182, "Recettes.csv").executer()
#     from UtilitairesFinalFantasyXIV.Traitements.Recolte import TraitementPageRecoltes
#     TraitementPageRecoltes(18, "Recoltes.csv").executer()

    from UtilitairesFinalFantasyXIV.Collections.Personnage import CollectionPersonnages
    x = CollectionPersonnages(None, "Personnages.csv")
    x.charger()
    x.sauver()
    from UtilitairesFinalFantasyXIV.Collections.Recette import CollectionRecettes
    y = CollectionRecettes(None, "Recettes.csv")
    y.charger()
    y.sauver()
    from UtilitairesFinalFantasyXIV.Collections.Recolte import CollectionRecoltes
    z = CollectionRecoltes(None, "Recoltes.csv")
    z.charger()
    z.sauver()
