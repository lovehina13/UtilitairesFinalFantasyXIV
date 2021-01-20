# coding: utf-8

# ==================================================================================================
# Name        : Recette.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'une collection de recettes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Recette import Recettes
from UtilitairesFinalFantasyXIV.Structure.Collection import Collection


class CollectionRecettes(Collection):

    def charger(self):
        self.elements = Recettes.creer(open(self.fichier, "r", encoding="utf-8").read()).elements

    def sauver(self):
        fichier = open(self.fichier, "w", encoding="utf-8")
        for _, element in self.elements.items():
            fichier.write(element.texte() + "\n")
