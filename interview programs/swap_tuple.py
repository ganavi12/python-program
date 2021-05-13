a = [1, 2, 3, 5, 7]
x = 8
res = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == x:
            res.append((a[i], a[j]))
print(res) 
        