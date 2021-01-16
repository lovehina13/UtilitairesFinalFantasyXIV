# coding: utf-8

# ==================================================================================================
# Name        : Objet.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'un objet et d'un ensemble d'objets
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Structure.Element import Element
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Objet(Element):

    def __init__(self, nom=str(), quantite=int()):
        super().__init__(nom)
        self.quantite = quantite


class Objets(Ensemble):
    pass
