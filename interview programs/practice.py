# def deco(func):
#     def wrapper():
#         print("start")
#         func()
#         print("end")
#     return wrapper

# @deco
# def name():
#     print("alex")

# # name()


# def deco(func):
#     def wrapper(a,b):
#         print("start")
#         print(a*b) 
#         func(a,b)
#         print("end")
#     return wrapper

# @deco
# def name(a,b):
#     print(a+b)

# name(10, 20)


# def fib(n):
#     a, b = 0, 1
#     while n > a:
#         yield a
#         a, b = b, a + b
# res = fib(6)
# for i in res:
#     print(i)


# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# print(fact(5))


# def pal(a):
#     s = ''
#     for i in a[::-1]:
#         s += i
#     return s
   
# a = 'mam'
# r = pal(a)
# if r == a:
#     print("palidrome")
# else:
#     print("not palidrome")



# def pal(a):
#     s = ''
#     for i in a[::-1]:
#         s += i
#     return s
#     if s == a:
#         print("palidrome")
#     else:
#         print("not palidrome")
# a = 'mam'
# pal(a)



def bubble(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    # for i in range(len(a)):
    print(a)

a = [10, 3, 1, 5, 2, 8, 0, 7]
bubble(a) 