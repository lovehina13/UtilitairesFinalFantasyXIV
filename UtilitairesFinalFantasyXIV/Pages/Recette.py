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

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/playguide/db/recipe/%s/" % nom)

    def extraire(self):
        # TODO: Implémenter l'extraction d'une page de recette
        self.element = Recette()


class PageRecettes(PageEnsemble):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/playguide/db/recipe/?page=%s" % nom)

    def extraire(self):
        self.ensemble = Recettes()
        for item in self.soup.find_all("a", {"class": "db_popup db-table__txt--detail_link"}):
            page = PageRecette(item.get("href").split("/")[5])
            self.ensemble.ajouter(page)
