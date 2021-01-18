# coding: utf-8

# ==================================================================================================
# Name        : Recette.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition des traitements relatifs aux recettes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Pages.Recette import PageRecette, PageRecettes
from UtilitairesFinalFantasyXIV.Structure.Traitement import Traitement


class TraitementPageRecette(Traitement):

    def __init__(self, donnee=str(), compteur=int(), nombre=int()):
        super().__init__(None)
        self.donnee = donnee
        self.compteur = compteur
        self.nombre = nombre

    def executer(self):
        self.afficher("Traitement de la recette %d sur %d" % (self.compteur, self.nombre))
        recette = PageRecette(self.donnee).traiter()
        self.afficher(recette.nom)  # TODO: Supprimer la trace


class TraitementPageRecettes(Traitement):

    def __init__(self, nombre=int()):
        super().__init__(None)
        self.nombre = nombre

    def executer(self):
        pages = list()
        for item in range(self.nombre):
            self.afficher("Traitement de l'ensemble de recettes %d sur %d" % (item + 1, self.nombre))
            pages += PageRecettes(str("%d" % (item + 1))).traiter().lister()
        for item, page in enumerate(pages):
            TraitementPageRecette(page.nom, item + 1, len(pages)).executer()
            if item > 0: break  # TODO: Supprimer le break
