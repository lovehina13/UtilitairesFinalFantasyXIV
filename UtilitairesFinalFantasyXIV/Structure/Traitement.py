# coding: utf-8

# ==================================================================================================
# Name        : Traitement.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'un traitement
# ==================================================================================================

import sys
from UtilitairesFinalFantasyXIV.Structure.Element import Element


class Traitement(Element):

    def executer(self):
        pass  # Note: Implémenter l'exécution pour chaque traitement

    def afficher(self, texte):
        print(texte)
        sys.stdout.flush()
