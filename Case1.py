class case():

    def __init__(self, bombe):
        self.bombe = bombe
        self.clic = False
        self.drapeau = False

    def BombeOuPas(self):
        return self.bombe

    def ClicOuPas(self):
        return self.clic

    def DrapeauOuPas(self):
        return self.drapeau

    def Drapeau(self):
        self.drapeau = not self.drapeau

    def Clic(self):
        self.clic = True

    def QuelsVoisins(self, voisins):
        self.voisins = voisins
        self.nombreAutour()

    def nombreAutour(self):
        self.nombre = 0
        for case in self.voisins:
            if case.BombeOuPas():
                self.nombre += 1

    def combienAutour(self):
        return self.nombre

    def Voisins(self):
        return self.voisins