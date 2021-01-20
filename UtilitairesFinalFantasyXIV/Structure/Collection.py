# coding: utf-8

# ==================================================================================================
# Name        : Collection.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'une collection
# ==================================================================================================

import sys
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Collection(Ensemble):

    def __init__(self, elements=None, fichier=str()):
        super().__init__(elements)
        self.fichier = fichier

    def charger(self):
        pass  # Note: Implémenter le chargement pour chaque collection

    def sauver(self):
        pass  # Note: Implémenter la sauvegarde pour chaque collection

    def afficher(self):
        for _, element in self.elements:
            print(element.texte())
        sys.stdout.flush()
