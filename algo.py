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

