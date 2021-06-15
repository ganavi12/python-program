def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("start")
        res = func(*args, **kwargs)
        print(res)
        print("end")
    return wrapper

@start_end_decorator
def print_name(name):
    return name

print_name('ganavi')


def fact(n):
    if n == 0: 
        return 1
    else:
        return n * fact(n - 1)
print(fact(5))


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     while n > 1:
#         yield n
#         n = n*factorial(n-1)

# result = factorial(5)
# for a in result:
#     print("fact",a)

def fib(n):
    a, b = 0, 1
    while n > a:
        yield a
        a, b = b, a + b
        
res = fib(5)
for i in res:
    print(i)


def fibonacci(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
print(fibonacci(10))