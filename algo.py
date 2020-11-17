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

# ---------------------------------------
# ---------------------------------------

"""def triFusion(list):
    len(list)
    if len(list)>0:
        list[/2]
        
        
       
        
        liste0 = partie gauche de la liste
        list1 = partie droite de la liste

        list0Trie = triFusion(list0)
        list1Trie = triFusion(list1)
        return fusion (list0trie,list1trie)
        
    else return list
"""
# --------------------------------------
#   Démineur
# --------------------------------------



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
