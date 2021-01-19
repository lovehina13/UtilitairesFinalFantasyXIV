# coding: utf-8

# ==================================================================================================
# Name        : Recolte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'une récolte et d'un ensemble de récoltes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Lieu import Lieux
from UtilitairesFinalFantasyXIV.Structure.Element import Element
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Recolte(Element):

    def __init__(self, nom=str(), classe=str(), sousClasse=str(), niveau=int(), categorie=str(),
                 pointsRecolte=None):
        super().__init__(nom)
        self.nom = nom
        self.classe = classe
        self.sousClasse = sousClasse
        self.niveau = niveau
        self.categorie = categorie
        self.pointsRecolte = pointsRecolte if isinstance(pointsRecolte, Lieux) else Lieux()


class Recoltes(Ensemble):
    pass
