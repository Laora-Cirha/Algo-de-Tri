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