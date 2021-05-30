d1 = {'a':2,'b':4,'c':5}
d2 = {'a': 4, 'c': 5, 'd': 6}
d3 = {}
def add_dic(d1, d2):
    for k1, v1 in d1.items():
        for k2, v2 in d2.items():
            if k1 in k2 or k2 in k1:
                v1 = v1+v2
                d3[k1] = v1
            else:
                d3[k1] = v1
                d3[k2] = v2
            # elif k1 not in k2:
            #     d3[k2] = v2
            # elif k2 not in k1:
            #     d3[k1]=v1
            
add_dic(d1, d2)
print(d3)