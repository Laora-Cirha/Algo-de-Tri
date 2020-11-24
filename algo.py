# ---------------------------------------
#   Tri par selection
# ---------------------------------------


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
#   Fusion
# ---------------------------------------

def triFusion (list):
    if len(list)>0:
        milieu = len//2
        #   A compléter
        list[0]=list[:milieu]
        list[1]=list[milieu:]

        list0Trie= triFusion(list0)
        list1Trie= triFusion(list1)
        #

        return fusion(list0Trie,list1Trie)

    else:
        return list


#   A compléter