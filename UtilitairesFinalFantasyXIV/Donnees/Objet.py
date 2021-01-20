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

    @staticmethod
    def creer(texte):
        items = texte.split(":")
        return Objet(items[0], int(items[1]))


class Objets(Ensemble):

    @staticmethod
    def creer(texte):
        objets = Objets()
        for item in texte.split(","):
            objets.ajouter(Objet.creer(item) if item else None)
        return objets
