# --------------------------------------
"""   Démineur """
# --------------------------------------

# --------------------------------------
"""   Tableau visible """
# --------------------------------------


hauteur = 5
largeur = 5

import random
def _init_(hauteur, largeur):

    listOflist=[]

    for i in range(hauteur):
        listRow=[]

        for j in range(largeur):
            listRow.append("x")
        listOflist.append(listRow)
        
    return listOflist

def modifyTableau(list):
    a = int(input("Choix de la colonne"))-1
    b = int(input("Choix de la ligne"))-1

    list[a][b]="0"

def affiche(tableau):
    for i in tableau:
        print(i)

def demineur():
    liste = _init_(hauteur,largeur)
    pasPerdu=True
    while (pasPerdu):
        modifyTableau(liste)
        affiche(liste)

demineur()
# --------------------------------------
"""   Nombre de mines """
# --------------------------------------

def mines(max):
    nMine = random.randint(2,max)
    return nMine
print(mines(5))




#   Position des mines (Tableau invisible)
"""
import random
def _init_(hauteur, largeur):

    listOflist=[]

    for i in range(hauteur):
        listRow=[]

        for j in range(largeur):
            listRow.append("x")
        listOflist.append(listRow)
        

    return listOflist

liste=_init_(5,5)

for i in liste:
    print(i)
"""
