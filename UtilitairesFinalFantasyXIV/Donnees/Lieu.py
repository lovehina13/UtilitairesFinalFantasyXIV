# coding: utf-8

# ==================================================================================================
# Name        : Lieu.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'un lieu et d'un ensemble de lieux
# ==================================================================================================

import distutils.util
from UtilitairesFinalFantasyXIV.Structure.Element import SousElement
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Lieu(SousElement):

    def __init__(self, nom=str(), zone=str(), region=str(), niveau=int(), temporaire=bool()):
        super().__init__(nom)
        self.zone = zone
        self.region = region
        self.niveau = niveau
        self.temporaire = temporaire

    def identifiant(self):
        return str("%s:%s" % (self.nom, self.niveau))

    @staticmethod
    def creer(texte):
        items = texte.split(":")
        return Lieu(items[0], items[1], items[2], int(items[3]) if items[3].isdigit() else items[3],
                    bool(distutils.util.strtobool(items[4])))


class Lieux(Ensemble):

    @staticmethod
    def creer(texte):
        lieux = Lieux()
        for item in texte.split(","):
            lieux.ajouter(Lieu.creer(item) if item else None)
        return lieux
