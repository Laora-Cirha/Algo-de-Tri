# --------------------------------------
"""   Démineur """
# --------------------------------------

# --------------------------------------
"""   Tableau visible """
# --------------------------------------

import random
def _init_(hauteur, largeur):
    # Initialisation / position du joueur

    a = int(input("Choix de la colonne"))
    b = int(input("Choix de la ligne"))
    a -= 1
   
    largeur -= 1
    print(a)

    listOflist=[]

    for i in range(hauteur):
        listRow=[]

        for j in range(largeur):
            if j == a :
                listRow.append("0")
            
            listRow.append("x")
        listOflist.append(listRow)
        

    return listOflist

liste=_init_(5,5)

for i in liste:
    print(i)

# --------------------------------------
"""   Nombre de mines """
# --------------------------------------

def mines(max):
    nMine = random.randint(2,max)
    return nMine
print(mines(5))




#   Position des mines (Tableau invisible)
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

