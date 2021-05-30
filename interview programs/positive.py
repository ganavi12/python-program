a = [12, -7, 5, 64, -14]
b = []
c = []
for i in range(len(a)):
    if a[i] > 0 and a[i] % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])
print(b,c)
