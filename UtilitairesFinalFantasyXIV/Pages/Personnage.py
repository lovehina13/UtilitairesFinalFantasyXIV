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

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/character/%s/" % nom)

    def extraire(self):
        # TODO: Implémenter l'extraction d'une page de personnage
        self.element = Personnage()


class PagePersonnages(PageEnsemble):

    def __init__(self, nom=str()):
        super().__init__(nom, None)
        self.adresse = str("https://fr.finalfantasyxiv.com/lodestone/freecompany/%s/member/?page=%s" % (nom.split(":")[0], nom.split(":")[1]))

    def extraire(self):
        self.ensemble = Personnages()
        for item in self.soup.find_all("a", {"class": "entry__bg"}):
            page = PagePersonnage(item.get("href").split("/")[3])
            self.ensemble.ajouter(page)
