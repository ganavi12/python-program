a = [1, 2, 3, 4, 5, 6, 7]
b = []
c = []
final = []
def rotate(a, r):
    for i in range(0, len(a)):
        print(r,i)
        if r <= i:
            b.append(a[i])
        else:
           c.append(a[i]) 
    
    final.extend(b) 
    final.extend(c)
    return final 
res = rotate(a, 2) 
print(res)