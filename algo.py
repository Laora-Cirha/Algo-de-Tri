# ---------------------------------------
#   Tri par selection
# ---------------------------------------

"""
list=[4,2,7,8]
def selectMin(list):
    var=list[0]
    for i in list:
        if var>i:
            var=i
    return var
print ("liste de base :")
print(list)

def triSelect (list):
    result=[]
    while len(list)>0:
        var=selectMin(list)
        list.remove(var)
        result.append(var)        
    return result
print("list trié :")
print(triSelect(list))
"""

# ---------------------------------------
#   Fusion
# ---------------------------------------

"""
def fusion(list1, list2):
    result=[]
    j=0
    for i in list1:
        while j<len(list2)-1 and i <list2[j]:
            result.append(list2[j])
        result.append(i)
    result.extend(list2[j:])

print(fusion([2,3,7],[4,5,8]))
"""

# --------------------------------------
#   Démineur
# --------------------------------------

#   Tableau

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

#   Nombre de mines

def mines(max):
    nMine = random.randint(2,max)
    return nMine
print(mines(5))

#   Position des mines

import random
def _init_(hauteur, largeur):

    listOflist=[]

    for i in range(hauteur):
        listRow=[]

        for j in range(largeur):
            listRow.append("x")
        listOflist.append(listRow)
        
    max=mines(hauteur*largeur//10)
    nbreMines=0
    while nbreMines<max:
        x=random.randint

    return listOflist

liste=_init_(5,5)

for i in liste:
    print(i)