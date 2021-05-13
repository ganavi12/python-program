def generator_fib(n):
    a ,b=0,1
    while n > a:
        yield a
        a, b = b,a+ b
res = generator_fib(5)
for i in res:
    print(i)