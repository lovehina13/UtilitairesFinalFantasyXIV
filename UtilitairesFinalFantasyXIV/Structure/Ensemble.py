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
            self.elements[element.nom] = element

    def recuperer(self, nom):
        return self.elements[nom] if nom in self.elements else None

    # Note: Obligatoire de définir un import local pour contourner un import cyclique
    def lister(self, filtres=None):
        from UtilitairesFinalFantasyXIV.Structure.Filtre import Filtres
        filtres = filtres if isinstance(filtres, Filtres) else Filtres()
        return [element for _, element in self.elements.items() if filtres.valider(element)]
