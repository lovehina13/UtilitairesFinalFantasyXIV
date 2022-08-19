# coding: utf-8

# ==================================================================================================
# Name        : UtilitairesFinalFantasyXIV/Traitements/Inventaire.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (05/12/2021)
# Description : Définition des traitements relatifs aux inventaires
# ==================================================================================================

import math
from UtilitairesFinalFantasyXIV.Collections.Recette import CollectionRecettes
from UtilitairesFinalFantasyXIV.Collections.Recolte import CollectionRecoltes
from UtilitairesFinalFantasyXIV.Donnees.Objet import Objet, Objets
from UtilitairesFinalFantasyXIV.Donnees.Recolte import Recolte
from UtilitairesFinalFantasyXIV.Structure.Filtre import Filtres
from UtilitairesFinalFantasyXIV.Structure.Traitement import Traitement


class TraitementCollectionInventaire(Traitement):

    def __init__(self, fichierRecettes=str(), fichierRecoltes=str()):
        super().__init__(None)
        self.fichierRecettes = fichierRecettes
        self.fichierRecoltes = fichierRecoltes
        self.collectionRecettes = None
        self.collectionRecoltes = None

    def executer(self):
        self.collectionRecettes = CollectionRecettes(None, self.fichierRecettes)
        self.collectionRecoltes = CollectionRecoltes(None, self.fichierRecoltes)
        self.collectionRecettes.charger()
        self.collectionRecoltes.charger()


class TraitementGestionInventaire(TraitementCollectionInventaire):

    def __init__(self, fichierRecettesIn=str(), fichierRecoltesIn=str(), fichierOut=str(),
                 filtres=None):
        super().__init__(fichierRecettesIn, fichierRecoltesIn)
        self.fichierOut = fichierOut
        self.filtres = filtres if isinstance(filtres, Filtres) else Filtres()

    def executer(self):

        def _recupererObjets(recettes, collectionRecettes):
            objets = Objets()
            degreMax = max(recette.degre for recette in recettes)
            degresRecettes = {degre: dict() for degre in range(1, degreMax + 1)}
            for recette in recettes:
                degreRecette = recette.degre
                if recette not in degresRecettes[degreRecette]:
                    degresRecettes[degreRecette][recette] = 0
                degresRecettes[degreRecette][recette] += 1.0 / recette.totalFabrique
            for _, degreRecettes in sorted(degresRecettes.items(), reverse=True):
                for recette, quantiteRecette in degreRecettes.items():
                    quantiteRecette = math.ceil(quantiteRecette)
                    for materiau in recette.materiaux.lister():
                        nomMateriau = materiau.nom
                        if nomMateriau in collectionRecettes.elements:
                            sousRecette = collectionRecettes.recuperer(nomMateriau)
                            sousDegreRecette = sousRecette.degre
                            if sousRecette not in degresRecettes[sousDegreRecette]:
                                degresRecettes[sousDegreRecette][sousRecette] = 0
                            degresRecettes[sousDegreRecette][sousRecette] += materiau.quantite * quantiteRecette / sousRecette.totalFabrique
                            continue
                        if nomMateriau not in objets.elements:
                            objets.ajouter(Objet(nomMateriau))
                        objets.recuperer(nomMateriau).quantite += materiau.quantite * quantiteRecette
                    for cristal in recette.cristaux.lister():
                        nomCristal = cristal.nom
                        if nomCristal not in objets.elements:
                            objets.ajouter(Objet(nomCristal))
                        objets.recuperer(nomCristal).quantite += cristal.quantite * quantiteRecette
            return objets, degresRecettes

        def _recupererRecolte(objet, collectionRecoltes):
            return collectionRecoltes.recuperer(objet.nom) if objet.nom in collectionRecoltes.elements else None

        def _recolte(recolte):
            return str("%s: %s" % (recolte.classe, recolte.pointsRecolte.lister()[0].texteUtilisateur()) if isinstance(recolte, Recolte) and len(recolte.pointsRecolte.lister()) else "???")

        super().executer()
        texte = list()
        recettes = self.collectionRecettes.lister(self.filtres)
        collectionRecettes = self.collectionRecettes.unicite()
        collectionRecoltes = self.collectionRecoltes.unicite()
        objets, degresRecettes = _recupererObjets(recettes, collectionRecettes)
        recoltes = {objet.nom: _recupererRecolte(objet, collectionRecoltes) for objet in objets.lister()}
        for objet in sorted(objets.lister(), key=lambda item: item.nom):
            texte.append(str("%s: %d (%s)" % (objet.nom, objet.quantite, _recolte(recoltes[objet.nom]))))
        for _, degreRecettes in sorted(degresRecettes.items()):
            texte.append("==================================================")
            for recette, quantiteRecette in sorted(degreRecettes.items(), key=lambda item: item[0].nom):
                quantiteRecette = math.ceil(quantiteRecette)
                texte.append(str("%s: %d" % (recette.nom, quantiteRecette)))
        self.afficher("\n".join(texte))
        open(self.fichierOut, "w", encoding="utf-8").write("\n".join(texte) + "\n")
