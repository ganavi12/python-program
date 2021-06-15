n = [15, 6, 7, 10, 12, 20, 10, 28, 10,20]
c = 0
x = []
# for i in n:
#     if i  == 10:
#         c = c+1
# print(c)
 

# for i in range(len(n)):
#     for j in range(i + 1, len(n)):
#         if n[i] == n[j]:
#             if n[i] in x:
#                 x.remove(n[i])
#             else:
#                 x.append(n[i])


print(x)

y = []
for i in n:
    if i in y:
        y.remove(i)
    else:
        y.append(i)
   
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] == n[j]:
            if n[i] in y:
                y.remove(n[i])
            else:
                y.append(n[i])
print(y)
