# coding: utf-8

# ==================================================================================================
# Name        : Personnage.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'une page de personnage et d'une page d'un ensemble de personnages
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Personnage import Personnage, Personnages
from UtilitairesFinalFantasyXIV.Structure.Page import PageElement, PageEnsemble


class PagePersonnage(PageElement):

    def extraire(self):
        # TODO: Implémenter l'extraction d'une page de personnage
        self.element = Personnage()


class PagePersonnages(PageEnsemble):

    def extraire(self):
        # TODO: Implémenter l'extraction d'une page d'un ensemble de personnages
        self.ensemble = Personnages()
