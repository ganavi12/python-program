def test(*argv):
    print(sum(argv))


test(1, 2, 3, 4, 5)

def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Potato', 'Lemon', 'Tomato', 'Pear')


# def test_args(*args):
#     for i in args:

#         if type(i) == int:
#         #    print(sum(i))
#             i += i
#     print(i)

# test_args(1,2,3,'a','b')


def argsKwargs(*args, **kwargs):
    print(args)
    print(kwargs)


argsKwargs('1', 1, 'slgotting.com', upvote='yes',
           is_true=True, test=1, sufficient_example=True)
