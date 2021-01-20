# coding: utf-8

# ==================================================================================================
# Name        : Ensemble.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'un ensemble
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Structure.Element import Element


class Ensemble:

    def __init__(self, elements=None):
        self.elements = dict()
        if isinstance(elements, dict):
            for _, element in elements.items():
                self.ajouter(element)

    def ajouter(self, element):
        if isinstance(element, Element):
            self.elements[element.identifiant()] = element

    def recuperer(self, identifiant):
        return self.elements[identifiant] if identifiant in self.elements else None

    # Note: Obligatoire de définir un import local pour contourner un import cyclique
    def lister(self, filtres=None):
        from UtilitairesFinalFantasyXIV.Structure.Filtre import Filtres
        filtres = filtres if isinstance(filtres, Filtres) else Filtres()
        return [element for _, element in self.elements.items() if filtres.valider(element)]

    def texte(self):
        # Note: Réimplémenter le format texte pour chaque ensemble si nécessaire
        return ",".join([element.texte() for _, element in self.elements.items()])

    @staticmethod
    def creer(texte):
        return Ensemble(texte)  # Note: Implémenter la création pour chaque ensemble
