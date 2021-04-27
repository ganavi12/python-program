# def decorator_exp(func):
#     def wrap(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res
#     return wrap


# @decorator_exp
# def add(*args):
#     return sum(args)


# print(add(10, 2, 3, 1, 22))


# nested decorators

def repeat(num=3):
    def decorate_repeat(func):
        def wrap(*args):
            for i in range(num):
                for name in args:
                    res = func(name)
            return res

        return wrap
    return decorate_repeat


@repeat(num=3)
def greet(name):
    print('welcome', name)


greet('ganavi', 'test', 'test2')
