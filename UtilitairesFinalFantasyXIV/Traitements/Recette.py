# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Traitements/Recette.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition des traitements relatifs aux recettes
# ==================================================================================================

import os
from UtilitairesFinalFantasyXIV.Pages.Recette import PageRecette, PageRecettes
from UtilitairesFinalFantasyXIV.Structure.Traitement import Traitement


class TraitementPageRecette(Traitement):

    def __init__(self, donnee=str(), compteur=int(), nombre=int(), fichier=str()):
        super().__init__(None)
        self.donnee = donnee
        self.compteur = compteur
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        self.afficher("Traitement de la recette %d sur %d" % (self.compteur, self.nombre))
        open(self.fichier, "a", encoding="utf-8").write(PageRecette(self.donnee).executer().texte() + "\n")


class TraitementPageRecettes(Traitement):

    def __init__(self, nombre=int(), fichier=str()):
        super().__init__(None)
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        if os.path.exists(self.fichier):
            os.remove(self.fichier)
        pages = list()
        for item in range(self.nombre):
            self.afficher("Traitement de l'ensemble de recettes %d sur %d" % (item + 1, self.nombre))
            pages += PageRecettes(str("%d" % (item + 1))).executer().lister()
        for item, page in enumerate(pages):
            TraitementPageRecette(page.nom, item + 1, len(pages), self.fichier).executer()
