a = [2, 5, 4, 11, 7]
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
     
print(a[-1::-1])
print(a[-1:-3:-1])
print(a[-1:-3:-1])
print(a[-1:-2:-1])