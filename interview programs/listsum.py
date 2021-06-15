# a = [1, 2, 3, 4]
# print(sum(a))

def largest(a):
    max = a[0] 
    for i in range(0, len(a)):
        if a[i] > max:
            max = a[i]
    print(max) 
a = [3,55,6,1,2]
res = largest(a)
# print(res)

from collections import Counter
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 7, 8, 9]

print(Counter(l1),Counter(l2))