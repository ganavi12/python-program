l = [1,2.3,55,'iuwer',[1,'234','serqewr',45.9]]
print(l)
m=[]
for i in l:
    if type(i) == list:
        m.append(i[::-1])
print(m)


# n = [1, 2, 3, 4, 5]
# s = 0
# for i in n:
#     s = s + i
# print(s)

def fib(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(5))

def fib_gen(n):
    a, b = 0, 1
    while n > a:
        yield a
        a, b = b, a + b
r = fib_gen(5)
for i in r:
    print(i)

def fact(n):
    if n == 0 or n <= 1:
        return n
    else:
        return n * fact(n - 1)
print(fact(5))