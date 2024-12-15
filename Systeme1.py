import pygame
import sys
import os
from time import sleep
from Minesweeper.Time import temps_float
from Time import temps
from Grille1 import grille
from Case1 import case
from  Test_mines import App

class système():

    def __init__(self, écran, écranT):
        self.écranT = écranT
        self.écran = écran
        self.caseTaille = self.écranT[0] // self.écran.getTaille()[1], self.écranT[1] // self.écran.getTaille()[0]
        self.loadImages()

    def jouer(self):
        pygame.init()
        self. display= pygame.display.set_mode((800,850))
        pygame.display.set_caption('Minesweeper')

        self.JeuAllumé = True
        while self.JeuAllumé:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    clicDroit = pygame.mouse.get_pressed()[2]
                    self.infoClic(position, clicDroit)
            self.afficher()
            pygame.display.flip()
            if self.écran.Victoire():
                #son = pygame.mixer.Sound("win.wav")
                #son.play()
                sleep(3)
                App().run()
                self.JeuAllumé = False

        pygame.quit()

    def afficher(self):
        hautGauche = (0, 0)
        calibri_font = pygame.font.SysFont("Arial", 50)
        color=(230,230,230)
        minutes = 0
        temps_sec = temps() - minutes *60
        if temps_sec == 60:
            minutes += 1
        timer_surface = calibri_font.render(str(minutes)+':'+str(temps_sec), True, color)
        timer_rect = timer_surface.get_rect()
        timer_rect.centerx = 400
        timer_rect.centery = 825
        self.display.blit(timer_surface, timer_rect)
        timing = temps_float() - temps()
        if timing < 0.05 :
            pygame.draw.rect(self.display, (0,0,0),(0,0,800,900) )


        for rangée in range(self.écran.getTaille()[0]):
            for colonne in range(self.écran.getTaille()[1]):
                case = self.écran.typeCase((rangée, colonne))
                image = self.valeurImage(case)
                self.display.blit(image, hautGauche)
                hautGauche = hautGauche[0] + self.caseTaille[0], hautGauche[1]
            hautGauche = 0, hautGauche[1] + self.caseTaille[1]

    def loadImages(self):
        self.images = {}
        for fichier in os.listdir("C:/Ecam/PythonImages/PythonImages"):
            if (not fichier.endswith(".png")):
                continue
            image = pygame.image.load(r"C:/Ecam/PythonImages/PythonImages/" + fichier)
            image = pygame.transform.scale(image, self.caseTaille)
            self.images[fichier.split(".")[0]] = image

    def valeurImage(self, case):
        valeur = None
        if case.ClicOuPas():
            valeur = "Mine" if case.BombeOuPas() else str(case.combienAutour())
        else:
            valeur = "DrapeauPasMal" if case.DrapeauOuPas() else "CaseVide"
        return self.images[valeur]

    def infoClic(self, position, clicDroit):
        if self.écran.Défaite():
            return
        info = position[1] // self.caseTaille[1], position[0] // self.caseTaille[0]
        case = self.écran.typeCase(info)
        self.écran.infoClic(case, clicDroit)
