from Case1 import case
from random import random


class grille():

    def __init__(self, taille, proba):
        self.taille = taille
        self.proba = proba
        self.perdu = False
        self.nClic = 0
        self.nSafe = 0
        self.typeGrille()

    def typeGrille(self):
        self.écran = []
        for rangée in range(self.taille[0]):
            rangée = []
            for colonne in range(self.taille[1]):
                bombe = random() < self.proba
                if not bombe:
                    self.nSafe += 1
                case1 = case(bombe)
                rangée.append(case1)
            self.écran.append(rangée)
        self.CasesVoisines()

    def CasesVoisines(self):
        for rangée in range(self.taille[0]):
            for colonne in range(self.taille[1]):
                case = self.typeCase((rangée, colonne))
                voisins = self.ListeCasesVoisines((rangée, colonne))
                case.QuelsVoisins(voisins)

    def ListeCasesVoisines(self, ref):
        voisins = []
        for rangée in range(ref[0] - 1, ref[0] + 2):
            for colonne in range(ref[1] - 1, ref[1] + 2):
                HorsDePortée = rangée < 0 or rangée >= self.taille[0] or colonne < 0 or colonne >= self.taille[1]
                idem = rangée == ref[0] and colonne == ref[1]
                if idem or HorsDePortée:
                    continue
                voisins.append(self.typeCase((rangée, colonne)))
        return voisins

    def getTaille(self):
        return self.taille

    def typeCase(self, ref):
        return self.écran[ref[0]][ref[1]]

    def infoClic(self, case, drapeau):
        if case.ClicOuPas() or (not drapeau and case.DrapeauOuPas()):
            return
        if drapeau:
            case.Drapeau()
            return
        case.Clic()
        if case.BombeOuPas():
            self.perdu = True
            return
        self.nClic += 1
        if case.combienAutour() != 0:
            return
        for voisins in case.Voisins():
            if not voisins.BombeOuPas() and not voisins.ClicOuPas():
                self.infoClic(voisins, False)

    def Défaite(self):
        return self.perdu

    def Victoire(self):
        return self.nClic == self.nSafe
