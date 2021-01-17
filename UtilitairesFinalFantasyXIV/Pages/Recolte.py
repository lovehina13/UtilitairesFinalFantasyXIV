# coding: utf-8

# ==================================================================================================
# Name        : Recolte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'une page de récolte et d'une page d'un ensemble de récoltes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Donnees.Recolte import Recolte, Recoltes
from UtilitairesFinalFantasyXIV.Structure.Page import PageElement, PageEnsemble


class PageRecolte(PageElement):

    def extraire(self):
        # TODO: Implémenter l'extraction d'une page de récolte
        self.element = Recolte()


class PageRecoltes(PageEnsemble):

    def extraire(self):
        # TODO: Implémenter l'extraction d'une page d'un ensemble de récoltes
        self.ensemble = Recoltes()
