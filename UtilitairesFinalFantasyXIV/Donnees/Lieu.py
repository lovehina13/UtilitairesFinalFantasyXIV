# coding: utf-8

# ==================================================================================================
# Name        : Lieu.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'un lieu et d'un ensemble de lieux
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Structure.Element import Element
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Lieu(Element):

    def __init__(self, nom=str(), zone=str(), region=str(), niveau=int(), temporaire=bool()):
        super().__init__(nom)
        self.zone = zone
        self.region = region
        self.niveau = niveau
        self.temporaire = temporaire


class Lieux(Ensemble):
    pass
