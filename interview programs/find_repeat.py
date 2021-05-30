list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# list = [-1, 1, -1, 8]
l2 = []
a = 0
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] and list[j] >= 0:
            if list[i] == list[j]:
                if list[i] in l2:
                    l2.remove(list[i])
                else:
                    l2.append(list[i]) 
print(l2) 
            
