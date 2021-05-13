import random
import secrets
import numpy as np


# a = random.random()
# a = random.uniform(1, 10)
# a = random.randint(1, 999999)
# a = random.randrange(10, 999999)

# mylist = list("ABCDEFGH")

# a = random.choice(mylist)
# c = random.choices(mylist, k=3)
# b = random.sample(mylist, 3)
# random.shuffle(mylist)
# print("input", mylist)
# print(a, b, c)
# print("after shuffle", mylist)

# a = secrets.randbelow(10)
# b = secrets.randbits(4)
# d = secrets.choice(mylist)
# print(d)

# a = np.random.rand(2, 2)
# b = np.random.randint(0, 10, (3, 4))
# np.random.shuffle(b)
# print(b)


# from random import numpy


# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)


# print(quicksort([3, 6, 8, 10, 1, 2, 1]))


# res = [[]] * 5


# def a():
#     return [lambda x: i * x for i in range(5)]


# for i in range(5):
#     for j, f in enumerate(a()):
#         res[j].append(f(i))
# print(res)

# a = [1, 2, 3, 5]


# def test(a):
#     try:
#         return a[1] + a[2] == a[0]
#     except (IndexError, TypeError):
#         return False
# def foo(a):
#     for i in a:
#         if i % 2 == 1:
#             print(i)
#         else:
#             break
#     else:
#         print(float('inf'))


# foo(a)


# class Foo():
#     def __init__(self):
#         pass


# f = Foo()
# print(f)


# import numpy as np
# x = np.matrix([[1,1,1],
#                [1,0,1],
#                [1,1,1]])
# # y = x.tolist()

# x[:, 0] = 0
# print(x)

for i in range(0, 3):
    field = []
    for j in range(0, 3):
        x = 1
        field.append(x)
    field.append(field) 