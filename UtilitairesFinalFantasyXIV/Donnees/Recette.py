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


class Recettes(Ensemble):
    pass
