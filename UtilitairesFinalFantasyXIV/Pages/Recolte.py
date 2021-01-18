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

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/playguide/db/gathering/%s/" % nom)

    def extraire(self):
        # TODO: Implémenter l'extraction d'une page de récolte
        self.element = Recolte()


class PageRecoltes(PageEnsemble):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/playguide/db/gathering/?page=%s" % nom)

    def extraire(self):
        self.ensemble = Recoltes()
        for item in self.soup.find_all("a", {"class": "db_popup db-table__txt--detail_link"}):
            page = PageRecolte(item.get("href").split("/")[5])
            self.ensemble.ajouter(page)
