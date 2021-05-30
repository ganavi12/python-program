n = [2, 7, 5, 64, 14]
n = [12, 14, 95, 3]
a = []
for i in range(len(n)):
    if n[i] % 2 == 0:
        a.append(n[i])
print(a)