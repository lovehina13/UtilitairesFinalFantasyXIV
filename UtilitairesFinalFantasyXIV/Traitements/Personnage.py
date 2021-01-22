# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Traitements/Personnage.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition des traitements relatifs aux personnages
# ==================================================================================================

import os
from UtilitairesFinalFantasyXIV.Pages.Personnage import PagePersonnage, PagePersonnages
from UtilitairesFinalFantasyXIV.Structure.Traitement import Traitement


class TraitementPagePersonnage(Traitement):

    def __init__(self, donnee=str(), compteur=int(), nombre=int(), fichier=str()):
        super().__init__(None)
        self.donnee = donnee
        self.compteur = compteur
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        self.afficher("Traitement du personnage %d sur %d" % (self.compteur, self.nombre))
        open(self.fichier, "a", encoding="utf-8").write(PagePersonnage(self.donnee).executer().texte() + "\n")


class TraitementPagePersonnages(Traitement):

    def __init__(self, donnee=str(), nombre=int(), fichier=str()):
        super().__init__(None)
        self.donnee = donnee
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        if os.path.exists(self.fichier):
            os.remove(self.fichier)
        pages = list()
        for item in range(self.nombre):
            self.afficher("Traitement de l'ensemble de personnages %d sur %d" % (item + 1, self.nombre))
            pages += PagePersonnages(str("%s:%d" % (self.donnee, item + 1))).executer().lister()
        for item, page in enumerate(pages):
            TraitementPagePersonnage(page.nom, item + 1, len(pages), self.fichier).executer()
