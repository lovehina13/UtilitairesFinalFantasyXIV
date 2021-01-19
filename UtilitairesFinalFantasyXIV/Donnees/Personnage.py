# coding: utf-8

# ==================================================================================================
# Name        : Personnage.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'un personnage et d'un ensemble de personnages
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Classe import Classes
from UtilitairesFinalFantasyXIV.Structure.Element import Element
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Personnage(Element):

    def __init__(self, nom=str(), titre=str(), serveur=str(), race=str(), ethnie=str(), sexe=str(),
                 dateNaissance=str(), divinite=str(), citeDepart=str(), grandeCompagnie=str(),
                 rang=str(), compagnieLibre=str(), classes=None):
        super().__init__(nom)
        self.titre = titre
        self.serveur = serveur
        self.race = race
        self.ethnie = ethnie
        self.sexe = sexe
        self.dateNaissance = dateNaissance
        self.divinite = divinite
        self.citeDepart = citeDepart
        self.grandeCompagnie = grandeCompagnie
        self.rang = rang
        self.compagnieLibre = compagnieLibre
        self.classes = classes if isinstance(classes, Classes) else Classes()


class Personnages(Ensemble):
    pass
