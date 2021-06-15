def f1():
    print("this is f1")

def f2():
    print("this is f2")

f1()
f2()
f1 = f2
f1()
f2()


def sum_func(*args):
    return sum(args)
print(sum_func(1,2,3,4,5))