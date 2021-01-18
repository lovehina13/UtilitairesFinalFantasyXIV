# coding: utf-8

# ==================================================================================================
# Name        : Personnage.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition des traitements relatifs aux personnages
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Pages.Personnage import PagePersonnage, PagePersonnages
from UtilitairesFinalFantasyXIV.Structure.Traitement import Traitement


class TraitementPagePersonnage(Traitement):

    def __init__(self, donnee=str(), compteur=int(), nombre=int()):
        super().__init__(None)
        self.donnee = donnee
        self.compteur = compteur
        self.nombre = nombre

    def executer(self):
        self.afficher("Traitement du personnage %d sur %d" % (self.compteur, self.nombre))
        personnage = PagePersonnage(self.donnee).traiter()
        self.afficher(personnage.nom)  # TODO: Supprimer la trace


class TraitementPagePersonnages(Traitement):

    def __init__(self, donnee=str(), nombre=int()):
        super().__init__(None)
        self.donnee = donnee
        self.nombre = nombre

    def executer(self):
        pages = list()
        for item in range(self.nombre):
            self.afficher("Traitement de l'ensemble de personnages %d sur %d" % (item + 1, self.nombre))
            pages += PagePersonnages(str("%s:%d" % (self.donnee, item + 1))).traiter().lister()
        for item, page in enumerate(pages):
            TraitementPagePersonnage(page.nom, item + 1, len(pages)).executer()
            if item > 0: break  # TODO: Supprimer le break
