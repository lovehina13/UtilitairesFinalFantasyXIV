# coding: utf-8

# ==================================================================================================
# Name        : Element.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'un élément et d'un sous-élément
# ==================================================================================================


class Element:

    def __init__(self, nom=str()):
        self.nom = nom

    def identifiant(self):
        return self.nom  # Note: Réimplémenter l'identifiant pour chaque élément si nécessaire

    def texte(self):
        # Note: Réimplémenter le format texte pour chaque élément si nécessaire
        return "|".join([item.texte() if hasattr(item, "texte") else str(item)
                         for _, item in self.__dict__.items()])

    @staticmethod
    def creer(texte):
        return Element(texte)  # Note: Implémenter la création pour chaque élément


class SousElement(Element):

    def texte(self):
        # Note: Réimplémenter le format texte pour chaque sous-élément si nécessaire
        return ":".join([item.texte() if hasattr(item, "texte") else str(item)
                         for _, item in self.__dict__.items()])

    @staticmethod
    def creer(texte):
        return SousElement(texte)  # Note: Implémenter la création pour chaque sous-élément
