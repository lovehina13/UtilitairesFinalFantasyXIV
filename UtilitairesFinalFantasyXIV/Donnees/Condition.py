# coding: utf-8

# ==================================================================================================
# Name        : Condition.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'une condition et d'un ensemble de conditions
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Structure.Element import SousElement
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Condition(SousElement):

    @staticmethod
    def creer(texte):
        return Condition(texte)


class Conditions(Ensemble):

    @staticmethod
    def creer(texte):
        conditions = Conditions()
        for item in texte.split(","):
            conditions.ajouter(Condition.creer(item) if item else None)
        return conditions
