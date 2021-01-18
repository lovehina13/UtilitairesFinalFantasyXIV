# coding: utf-8

# ==================================================================================================
# Name        : Recolte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition des pages relatives aux récoltes
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
        self.element.nom = self.soup.find("h2", {"class": "db-view__item__text__name"}).contents[0].strip()


class PageRecoltes(PageEnsemble):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/playguide/db/gathering/?page=%s" % nom)

    def extraire(self):
        self.ensemble = Recoltes()
        for item in self.soup.find_all("a", {"class": "db_popup db-table__txt--detail_link"}):
            page = PageRecolte(item.get("href").split("/")[5])
            self.ensemble.ajouter(page)
