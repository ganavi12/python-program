import re
import random
from collections import OrderedDict

a = [1, 2, 3, 8, 7, 6, 'hello']
# random.shuffle(a)
# b = random.randint(0,100)
# print(a,b)

# x = [i for i in "word"]
# print(x)

# y = [i**2 for i in range(10)]
# print(y)

# if
# z = [i*2 for i in range(10) if i%2 == 0]
# print(z)

#  else if
# c = [i if i%2 != 0 else 'odd' for i in range(10)]
# print(c)

# mylist = []
# for x in [2,4,6]:
#     for y in [100,200,300]:
#         mylist.append(x*y)
# print(mylist)

# d = [i*j for i in [2,4,6] for j in [1,3,5]]
# print(d)

# if
# d = [i for i in a if i == 'hello']
# print(d)

#  nested if
# e = [i for i in range(100) if i%2 == 0  if i%5 == 0 ]
# print(e)

# dictionary comprehension

# if
# x = {i:i for i in range(10)}
# print(x)

# x = {i:i*i for i in range(10)}
# print(x)

# xx = {}
# for i in range(10):
#     xx[i] = i*i
# print(xx)

prod = {'a': 22, 'b': 33, 'c': 44}
calc = 2
data = {k: v*2 for (k, v) in prod.items()}
print(data)


# prod = {'a' : 22,'b' : 33,'c' : 44}
# calc = 2
# data = {k : v*2 for (k,v) in prod.items() if v%2 ==0}
# print(data)

# data1 = {k1 : {k2 : k1* k2 for k2 in range(1,6)} for k1 in range(1,5)}
# print(data1)


# data2 = {k1 : [k1* k2 for k2 in range(1,6)] for k1 in range(1,5)}
# print(data2)

# ordered_dictionary = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# ordered_dictionary = OrderedDict(ordered_dictionary)
# print(ordered_dictionary)

# data = input("enter value")
# data = 'BANANA FRIES 12 POTATO CHIPS 30 APPLE JUICE 10 CANDY 5 APPLE JUICE 10 CANDY 5 CANDY 5 CANDY 5 POTATO CHIPS 30'
# rep = data.replace(' ','')
# split = data.split(' ')
# joined = "_".join(data)
# print([char for char in split])

# res = re.search(r'\[\[\[[^\]]+\]\]\]', data).group()
# print(data)
# print(split)
# num = []
# # string = set()
# string = {}
# print(len(split))
# for k in split:
#     if k.isdigit():
#         num.append(k)
#     elif k.isalpha():
#         string[k] = k
# string.pop('FRIES')
# string.pop('CHIPS')
# string.pop('JUICE')
# print(num,string)
# for m in num:
#     string['BANANA'] = m


tupledata = 1, 2, 3, 4, 5
print(type(tupledata))

a, *b, c = tupledata
print(a, b, c)
