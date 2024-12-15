import pygame
from pygame.locals import *
import pygame
import pygame_gui
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel
import sys
from dataclasses import dataclass


TpsZero = pygame.time.get_ticks()

def temps():
    seconds = (pygame.time.get_ticks() - TpsZero) / 1000
    secondes = int (seconds)
    return (secondes)

def temps_float():
    seconds = (pygame.time.get_ticks() - TpsZero) / 1000
    return (seconds)


