# coding: utf-8

# ==================================================================================================
# Name        : Recette.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'une page de recette et d'une page d'un ensemble de recettes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Recette import Recette, Recettes
from UtilitairesFinalFantasyXIV.Structure.Page import PageElement, PageEnsemble


class PageRecette(PageElement):

    def extraire(self):
        # TODO: Implémenter l'extraction d'une page de recette
        self.element = Recette()


class PageRecettes(PageEnsemble):

    def extraire(self):
        # TODO: Implémenter l'extraction d'une page d'un ensemble de recettes
        self.ensemble = Recettes()
