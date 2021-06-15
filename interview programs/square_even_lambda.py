a = [2,-5,3,-6,-8] 
# x = list(filter(lambda x: x*x if x>0 else 0, a)) 
# x = list(map(lambda x: x * x if x > 0 else None, a))
# y = [i for i in x if i != None]
# # or
y = [i*i  for i in a if i > 0]

print(y)


# a = [1, 3, 4, 5]
# b = []
# def sum_list(a, n):
#     for i in range(len(a)+1):
#         if a[i] + a[i+1] == n:
#             b.append((i,i+1))
#     return b
    
# print(sum_list(a, 7))



x = [11, 44, 12, 77, None, None, None]
y = [67, 14, 35]
z = x + y

from collections import Counter
a = [1, 2, 3, 4]
b = [3, 4, 7, 8]
print(Counter(a)+Counter(b))
z = "aaccddsdf"
print(Counter(z))
