
#  pos1,pos3   o/p [19,65,23,90]

def swap_list(a, pos1=0, pos2=3-1): 
    a[pos1], a[pos2] = a[pos2], a[pos1]
    return a
a = [23, 65, 19, 90]
print(swap_list(a)) 
    