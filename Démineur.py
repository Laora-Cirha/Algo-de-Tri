# --------------------------------------
"""   Démineur """
# --------------------------------------

# Variables
# Modifiez ces variables pour changer les settings du jeu

import random


hauteur = 5
largeur = 5
minesMax = 5

# --------------------------------------
"""   Nombre de mines """
# --------------------------------------

def mines(max):
    nMine = random.randint(2,minesMax)
    return nMine
print("Il y a |",mines(minesMax),"| mines.")

# --------------------------------------
"""   Position des mines """
# --------------------------------------
def _mines_(hauteur, largeur):

    listOflist=[]

    for i in range(hauteur):
        listRow=[]

        for j in range(largeur):
            listRow.append("1")
        listOflist.append(listRow)
        
    return listOflist

# Position aléatoire des mines

def minesPos(list):
    c = random.randint(2,hauteur)-1
    d = random.randint(2,largeur)-1

    list[c][d]="0"

# --------------------------------------
"""   Tableau visible """
# --------------------------------------

# Paramètre de la grille
def _init_(hauteur, largeur):

    listOflist=[]

    for i in range(hauteur):
        listRow=[]

        for j in range(largeur):
            listRow.append("x")
        listOflist.append(listRow)
        
    return listOflist

# Position du joueur
def modifyTableau(list):
    a = int(input("Choix de la ligne : "))-1
    b = int(input("Choix de la colonne : "))-1

    list[a][b]="0"

# Affichage 
def affiche(tableau):
    for i in tableau:
        print(i)

# Durée de jeu 
def demineur():
    liste = _init_(hauteur,largeur)
    pasPerdu=True
    while (pasPerdu):
        modifyTableau(liste)
        affiche(liste)

demineur()


#   Position des mines (Tableau invisible)
