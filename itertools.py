from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
import operator
from itertools import count, cycle, repeat

a = [1, 2]
b = [3, 4]

# print(list(product(a, b)))
c = [1, 2, 3, 5]
# print(list(permutations(c)))
# print(list(combinations(c, 2)))
# print(list(combinations_with_replacement(c, 2)))

# print(c)
# print(list(accumulate(c)))
# acc = accumulate(c, func=operator.mul)
# print(list(acc))

# grp = groupby(c, key=lambda x: x < 3)
# for k, v in grp:
# print(k, list(v))

# for i in count(10):
#     print(i)
#     if i == 15:
#         break

# for i in cycle(c):
#     print(i)
#     if i == 5:
#         break

for i in repeat(c, 4):
    print(i)

for i in repeat(1, 4):
    print(i)
