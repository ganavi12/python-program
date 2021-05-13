# def arr_remainder(a, n):
#     mul = 1
#     for i in a:
#         mul = mul * (i % n)
#     return mul % n
# a = [100, 10, 5, 25, 35, 14]
# print(arr_remainder(a,11))

# import re

# res = re.search('a', 'abcdef')
# print(res)


# import subprocess

# r = subprocess.run(['ls', '-l', '/dev/null'], capture_output=True)
# print(r)


# import os

# print(list(next(os.walk(".."))))

arr = ['a', 'b', 'c']

res = [i + 'a' for i in arr]
print(res)