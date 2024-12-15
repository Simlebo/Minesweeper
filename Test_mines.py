from Time import temps_float

import pygame
import sys
import pygame_gui
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
import json
def level():
    return 1
#def temps ():
    #return 693

class App:
  def __init__(self):
    pygame.init()
    self.size = (800, 600)
    self.screen = pygame.display.set_mode(self.size)
    self.manager = pygame_gui.UIManager(self.size)
    calibri_font = pygame.font.SysFont("Calibri", 50)
    color = (230, 230, 230)
    minutes = 0
    temps_sec = temps_float() - minutes * 60
    if temps_sec == 60:
        minutes += 1
    self.timer_surface = calibri_font.render('Votre tems est de ' + str(minutes) + ':' + str(temps_sec), True, color)
    self.timer_rect = self.timer_surface.get_rect()
    self.timer_rect.centerx = 400  # en bas à droite
    self.timer_rect.centery = 60
    calibri_font = pygame.font.SysFont("Calibri", 50)
    self.score_surface = calibri_font.render('le meilleur temps est ' + self.open(), True, (250, 250, 250))
    self.score_rect = self.score_surface.get_rect()
    self.score_rect.centerx = 400
    self.score_rect.centery = 120


    self.hello_button = UIButton(
      relative_rect=pygame.Rect(350, 275, 150, 50),
      text='entrer mon nom',
      manager=self.manager
    )

    self.input = UITextEntryLine(
      relative_rect=pygame.Rect(350, 220, 150, 50),
      manager=self.manager
    )
    self.display = UILabel(
      relative_rect=pygame.Rect(350, 330, 150, 50),
      text='',
      manager=self.manager
    )

  def process_events(self, event: pygame.event.Event):
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element is self.hello_button:
        name = self.input.text
        self.fichier(name)



  def fichier(self, nom):
        self.nom = nom

        if self.nom != "":

            try:
                with open('scores.json', 'r', encoding="utf-8") as file:
                    data = file.read()

                    if data != "":
                        self.data2 = json.loads(data)

                    else:
                        self.data2 = {"Content": []}

            except:
                print("Ficher json non-existant ! Création d'un nouveau ficher: scores.json...")
                with open('scores.json', 'w', encoding="utf-8")as file:
                    self.data2 = {"Content": []}

            with open('scores.json', 'w', encoding="utf-8") as file:

                score = {"Nom": self.nom,"Temps": temps_float(), "Niveau": level()}

                self.data2["Content"].append(score)

                ready = json.dumps(self.data2, indent=4)
                file.write(ready)


  def open(self):

    with open("scores.json", 'r', encoding="utf-8") as file:
        contenu = file.read()
        trans = json.loads(contenu)

        if len(trans["Content"]) >= 2:
            self.a = trans['Content'][0]

            for i in range(len(trans['Content'])):

                if self.a["Temps"] < trans['Content'][i]['Temps']:
                    self.a = trans['Content'][i]
                    tempsdufichier = self.a["Temps"]
                    temps_complet = 0
                    while tempsdufichier > 60:
                        tempsdufichier -= 60
                        temps_complet += 1

                    return (str(temps_complet) +':'+ str(tempsdufichier) + ' par ' + str(self.a["Nom"]))







  def run(self):
    clock = pygame.time.Clock()
    while True:
      time_delta = clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if not self.manager.process_events(event):
          self.process_events(event)


      self.manager.update(time_delta/1000)
      pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((0, 0), self.size))
      self.manager.draw_ui(self.screen)
      self.screen.blit(self.timer_surface, self.timer_rect)
      self.screen.blit(self.score_surface, self.score_rect)
      pygame.display.flip()




