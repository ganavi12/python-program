a = [1, 2, 3, 5, 7]
x = 8
res = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == x:
            res.append((a[i], a[j]))
print(res)



a = [1, 2, 2, 3, 4, 5, 6, 6]
b = []
for i in range(len(a)):
    c = a.count(a[i])
    if c > 0:
        b.append((a[i], c)) 
print(b, c)


# a = [1, 2, 2, 3, 4, 5, 6, 6]
# b = []
# c = 0
# for i in range(len(a)):
#     c = a.count(a[i])
#     if c > 0:
#         b.append((a[i], c)) 
# print(b,c)