from Systeme1 import système
from Grille1 import grille
from Case1 import case
from Titre1 import titre

Titre = titre()
Titre.Bienvenue()

a = 0
b = input('Veuillez choisir la difficulté (numéro): ')
def level():
    return b


if b == '1':
    a = 9
else:
    if b == '2':
        a = 16
    else:
        if b == '3':
            a = 50
        else:
            print('Désolé, veuillez relancer le programme!')
            quit()

taille = (a, a)
proba = 0.1
Grille = grille(taille, proba)
écranT = (800,800)
jouer = système(Grille, écranT)
jouer.jouer()