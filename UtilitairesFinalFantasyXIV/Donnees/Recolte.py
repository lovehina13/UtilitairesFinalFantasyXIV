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

    @staticmethod
    def creer(texte):
        items = texte.split("|")
        return Recolte(items[0], items[1], items[2], int(items[3]), items[4], Lieux.creer(items[5]))


class Recoltes(Ensemble):

    @staticmethod
    def creer(texte):
        recoltes = Recoltes()
        for item in texte.split("\n"):
            recoltes.ajouter(Recolte.creer(item) if item else None)
        return recoltes
