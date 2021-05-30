l1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
l2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
l3 = []
for i in range(len(l1)):
    for j in range(len(l2)):
        if i == l2[j]:
            l3.append(l1[i])
print(l3)
# zipped_list = zip(l1 + l2)
# y = [x for _, x in sorted(zipped_list)]
# print(z)