# coding: utf-8

# ==================================================================================================
# Name        : Recette.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'une recette et d'un ensemble de recettes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Condition import Conditions
from UtilitairesFinalFantasyXIV.Donnees.Objet import Objets
from UtilitairesFinalFantasyXIV.Structure.Element import Element
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Recette(Element):

    def __init__(self, nom=str(), classe=str(), niveau=int(), livre=str(), categorie=str(),
                 materiaux=None, cristaux=None, totalFabrique=int(), difficulte=int(),
                 solidite=int(), qualiteMaximum=int(), qualite=str(), conditions=None, degre=int()):
        super().__init__(nom)
        self.classe = classe
        self.niveau = niveau
        self.livre = livre
        self.categorie = categorie
        self.materiaux = materiaux if isinstance(materiaux, Objets) else Objets()
        self.cristaux = cristaux if isinstance(cristaux, Objets) else Objets()
        self.totalFabrique = totalFabrique
        self.difficulte = difficulte
        self.solidite = solidite
        self.qualiteMaximum = qualiteMaximum
        self.qualite = qualite
        self.conditions = conditions if isinstance(conditions, Conditions) else Conditions()
        self.degre = degre

    def identifiant(self):
        return str("%s:%s" % (self.nom, self.classe))

    @staticmethod
    def creer(texte):
        items = texte.split("|")
        return Recette(items[0], items[1], int(items[2]), items[3], items[4],
                       Objets.creer(items[5]), Objets.creer(items[6]), int(items[7]), int(items[8]),
                       int(items[9]), int(items[10]), items[11], Conditions.creer(items[12]),
                       int(items[13]))


class Recettes(Ensemble):

    @staticmethod
    def creer(texte):
        recette = Recettes()
        for item in texte.split("\n"):
            recette.ajouter(Recette.creer(item) if item else None)
        return recette
