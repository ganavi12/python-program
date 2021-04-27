# def max(n):
#     i = 0
#     if i < n:
#         res = i**2
#         i += 1
#         yield res


# result = max(10)
# for n in result:
#     print(n)

# m = iter(result)
# for a in range(10):
#     print(next(m))


# def list(num):
#     for i in num:
#         yield(i*i)


# n = list([1, 2, 3, 4, 5])
# print(sum(n))
# print(sorted(n))
# for num in n:
#     print(num)


# num = {i: i*i for i in [1, 2, 3, 4, 5]}
# print(num)


# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         yield a
#         a, b = b, a+b


# m = fib(10)
# for i in m:
#     print(i)

# def fibonacci(n):
#     if n < 0:
#         return "invalid"
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# fib = fibonacci(10)
# print(fib)


# n = int(input("enter number"))
# a = 0
# b = 1

# if n <= 0:
#     print(a, end='')
# else:
#     print(a, b, end=' ')
#     for i in range(2, n):
#         next = a+b
#         print(next, end=' ')
#         a = b
#         b = next

# import copy
# a = [1, 2, 44]
# b = a
# print(a, b)
# b[1] = 10
# print(a, b)
# c = a.copy()
# print(a, c)
# c[1] = 0
# # print(a, c)
# d = copy.deepcopy(a)
# print(a, d)
# d[2] = "ab"
# print(a, d)


# rows = [[f'{(n+1) + (i*10):4}' for n in range(10)] for i in range(10)]
# rows = reversed([reversed(rows[i]) if i % 2 else rows[i]
#                  for i in range(len(rows))])

# for row in rows:
#     print(' | '.join(row))


# t = 10,
# print(t)
# print(type(t))

# t = 10
# print(t)
# print(type(t))


# s = input('enter the string: ')
# l = s.split()
# d = {}
# for x in l:
#     if x in d.keys():
#         d[x] = d[x]+1
#     else:
#         d[x] = 1
# for k, v in d.items():
#     print("{} = {} times".format(k, v))


# s = input('enter the String: ')
# output = ''
# for x in s:
#     if x.isalpha():
#         output = output+x
#         previous = x
#     else:
#         output = output+chr(ord(previous)+int(x))
# print(output)


# n = input("enter the string")
# n = 'ganavi'
# print(n[::-1])
# print(''.join(reversed(n)))
# a = len(n)-1
# # print(n[a])
# target = ''
# while a >= 0:
#     target = target+n[a]
#     a = a-1
# print(target)
# res = ''
# for i in range(0, len(n)):
#     res = n[i] + res
# print(res)

# n = 'ganavi'
# split = n.split()
# l = []
# for i in n:
#     l.append(i[::-1])
#     print(' '.join(l))

# n = 'ganavi'
# split = n.split()
# # print(split)
# l = []
# for i in split:
#     l.append(i[::-1])
#     print(' '.join(l))


# a = input('Enter the string: ')
# l = a.split()
# l1 = []
# for i in reversed(l):
#     l1.append(i)
# print(' '.join(l1))

# a = 'ganavi123'
# for i in reversed(a):
#     print(i, end='')
# s1 = s2 = ''
# for i in a:
#     if i.isalpha():
#         s1 = s1+i
#     else:
#         s2 = s2+i
# # print(s2)
# print(''.join(s1)+''.join(s2))
# print(sorted(s2))
# print(''.join(sorted(s1))+''.join(sorted(s2)))


s = 'Learning python is very easy!!!'
# print(s[5:7])
# print(s[5:7:1])
# print(s[:7])
# print(s[1:])
# print(s[::])    # complete String
# print(s[0:])    # complete String
# print(s[::1])  # forword
# print(s[::-1])  # reverse
# print(s[5:0:1])  # end is '0' then reulst will be empty[forword]
# print(s[-1:5:1])  # begin is '-1' then reulst will be empty[forword]
# print(s[0:5:-1])  # begin is '0' then reulst will be empty[reverse]
# print(s[5:-1:-2])  # end is '-1' then reulst will be empty[reverse]

# print(s+s)


# a, b, c = [int(i) for i in input("enter 3 no").split()]
# print('biggest no is {}'.format(a if a > b and a > c else b if b > c else c))


# n = int(input('Enter the no of rows'))
# for i in range(1, n+1):
#     print(" "*(n-i), end=' ')
#     print("* "*i)

def updateList(list1):
    list1[1] = 10


n = [5, 6]
print(id(n))
print(n)
updateList(n)
print(n)
print(id(n))
