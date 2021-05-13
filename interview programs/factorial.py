def factorial(n):
    # return 1 if n == 0 or n == 1 else n * factorial(n-1)
    if n == 0 or n == 1:
        return 1
    else:
        a = n * factorial(n - 1)
        return a
        # return n*factorial(n-1)


n = int(input("enter number"))
print("facorial number of {0} is {1} ".format(n, factorial(n)))
