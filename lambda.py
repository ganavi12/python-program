
from functools import reduce
# add = lambda x:x*10
# print(add(2))

# multi = lambda x,y : x*y
# print(multi(2,10))

# x = [(lambda i:i*i)(i) for i in range(10)]
# print(x)

# y = [(lambda x, y: x*y)(x, y) for x in range(5) for y in range(5)]
# print(y)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*x, a)
print(list(b))

# list_com = [i for i in a if i % 2 == 0]
# print(list_com)

# red = reduce(lambda x, y: x*y, a)
# print(red)

print(2**-1)
