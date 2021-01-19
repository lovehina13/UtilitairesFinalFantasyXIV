# coding: utf-8

# ==================================================================================================
# Name        : Recolte.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition des traitements relatifs aux récoltes
# ==================================================================================================

import os
from UtilitairesFinalFantasyXIV.Pages.Recolte import PageRecolte, PageRecoltes
from UtilitairesFinalFantasyXIV.Structure.Traitement import Traitement


class TraitementPageRecolte(Traitement):

    def __init__(self, donnee=str(), compteur=int(), nombre=int(), fichier=str()):
        super().__init__(None)
        self.donnee = donnee
        self.compteur = compteur
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        self.afficher("Traitement de la récolte %d sur %d" % (self.compteur, self.nombre))
        open(self.fichier, "a", encoding="utf-8").write(PageRecolte(self.donnee).traiter().texte() + "\n")


class TraitementPageRecoltes(Traitement):

    def __init__(self, nombre=int(), fichier=str()):
        super().__init__(None)
        self.nombre = nombre
        self.fichier = fichier

    def executer(self):
        if os.path.exists(self.fichier):
            os.remove(self.fichier)
        pages = list()
        for item in range(self.nombre):
            self.afficher("Traitement de l'ensemble de récoltes %d sur %d" % (item + 1, self.nombre))
            pages += PageRecoltes(str("%d" % (item + 1))).traiter().lister()
        for item, page in enumerate(pages):
            TraitementPageRecolte(page.nom, item + 1, len(pages), self.fichier).executer()
            if item > 0: break  # TODO: Supprimer le break
