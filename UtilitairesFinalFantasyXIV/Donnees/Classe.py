# coding: utf-8

# ==================================================================================================
# Name        : Classe.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 3.0.0 (DD/MM/YYYY)
# Description : Définition d'une classe et d'un ensemble de classes
# ==================================================================================================

from UtilitairesFinalFantasyXIV.Structure.Element import Element
from UtilitairesFinalFantasyXIV.Structure.Ensemble import Ensemble


class Classe(Element):

    def __init__(self, nom=str(), categorie=str(), niveau=int()):
        super().__init__(nom)
        self.categorie = categorie
        self.niveau = niveau

    # Noms des classes
    PLD = str("Paladin")
    GUE = str("Guerrier")
    CHN = str("Chevalier noir")
    PSB = str("Pistosabreur")
    MBL = str("Mage blanc")
    ERU = str("Érudit")
    AST = str("Astromancien")
    MOI = str("Moine")
    DRG = str("Chevalier dragon")
    NIN = str("Ninja")
    SAM = str("Samouraï")
    BRD = str("Barde")
    MCH = str("Machiniste")
    DNS = str("Danseur")
    MNO = str("Mage noir")
    INV = str("Invocateur")
    MRG = str("Mage rouge")
    MBU = str("Mage bleu")
    MEN = str("Menuisier")
    FRG = str("Forgeron")
    ARM = str("Armurier")
    ORF = str("Orfèvre")
    TAN = str("Tanneur")
    COU = str("Couturier")
    ALC = str("Alchimiste")
    CUI = str("Cuisinier")
    MIN = str("Mineur")
    BOT = str("Botaniste")
    PEC = str("Pêcheur")

    # Catégories des classes
    tank = str("Tank")
    soigneur = str("Soigneur")
    dpsMelee = str("DPS de mêlée")
    dpsPhysiqueDistance = str("DPS physique à distance")
    dpsMagiqueDistance = str("DPS magique à distance")
    artisan = str("Artisan")
    recolteur = str("Récolteur")


class Classes(Ensemble):

    # Classes de base
    classesBase = {Classe.PLD: Classe(Classe.PLD, Classe.tank, 0),
                   Classe.GUE: Classe(Classe.GUE, Classe.tank, 0),
                   Classe.CHN: Classe(Classe.CHN, Classe.tank, 0),
                   Classe.PSB: Classe(Classe.PSB, Classe.tank, 0),
                   Classe.MBL: Classe(Classe.MBL, Classe.soigneur, 0),
                   Classe.ERU: Classe(Classe.ERU, Classe.soigneur, 0),
                   Classe.AST: Classe(Classe.AST, Classe.soigneur, 0),
                   Classe.MOI: Classe(Classe.MOI, Classe.dpsMelee, 0),
                   Classe.DRG: Classe(Classe.DRG, Classe.dpsMelee, 0),
                   Classe.NIN: Classe(Classe.NIN, Classe.dpsMelee, 0),
                   Classe.SAM: Classe(Classe.SAM, Classe.dpsMelee, 0),
                   Classe.BRD: Classe(Classe.BRD, Classe.dpsPhysiqueDistance, 0),
                   Classe.MCH: Classe(Classe.MCH, Classe.dpsPhysiqueDistance, 0),
                   Classe.DNS: Classe(Classe.DNS, Classe.dpsPhysiqueDistance, 0),
                   Classe.MNO: Classe(Classe.MNO, Classe.dpsMagiqueDistance, 0),
                   Classe.INV: Classe(Classe.INV, Classe.dpsMagiqueDistance, 0),
                   Classe.MRG: Classe(Classe.MRG, Classe.dpsMagiqueDistance, 0),
                   Classe.MBU: Classe(Classe.MBU, Classe.dpsMagiqueDistance, 0),
                   Classe.MEN: Classe(Classe.MEN, Classe.artisan, 0),
                   Classe.FRG: Classe(Classe.FRG, Classe.artisan, 0),
                   Classe.ARM: Classe(Classe.ARM, Classe.artisan, 0),
                   Classe.ORF: Classe(Classe.ORF, Classe.artisan, 0),
                   Classe.TAN: Classe(Classe.TAN, Classe.artisan, 0),
                   Classe.COU: Classe(Classe.COU, Classe.artisan, 0),
                   Classe.ALC: Classe(Classe.ALC, Classe.artisan, 0),
                   Classe.CUI: Classe(Classe.CUI, Classe.artisan, 0),
                   Classe.MIN: Classe(Classe.MIN, Classe.recolteur, 0),
                   Classe.BOT: Classe(Classe.BOT, Classe.recolteur, 0),
                   Classe.PEC: Classe(Classe.PEC, Classe.recolteur, 0)}
