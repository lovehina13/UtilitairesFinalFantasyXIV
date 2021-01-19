# coding: utf-8

# ==================================================================================================
# Name        : Objet.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'un objet et d'un ensemble d'objets
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Structure.Element import SousElement
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Objet(SousElement):

    def __init__(self, nom=str(), quantite=int()):
        super().__init__(nom)
        self.quantite = quantite


class Objets(Ensemble):
    pass
