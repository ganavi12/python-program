# try:
#     a = 5/1
#     b = 'd' * 10
# except Exception as e:
#     print(e)
# finally:
#     print("finally")


def test_exception(x):
    if x > 100:
        raise CheckError('value is high', x)
    else:
        raise CheckError('value is small', x)


try:
    test_exception(1)
except CheckError as e:
    print(e.message, e.value)


class CheckError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
