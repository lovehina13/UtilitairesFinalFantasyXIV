# coding: utf-8

# ==================================================================================================
# Name        : Recette.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition des pages relatives aux recettes
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
        self.element.nom = self.soup.find("h2", {"class": "db-view__item__text__name"}).contents[0].strip()


class PageRecettes(PageEnsemble):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/playguide/db/recipe/?page=%s" % nom)

    def extraire(self):
        self.ensemble = Recettes()
        for item in self.soup.find_all("a", {"class": "db_popup db-table__txt--detail_link"}):
            page = PageRecette(item.get("href").split("/")[5])
            self.ensemble.ajouter(page)
