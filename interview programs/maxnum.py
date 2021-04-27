def max(a, b):
    if a > b:
        return "a is greater"+a
    else:
        return "b is  greater "+b


a, b = input("Enter a two value: ").split()
print(max(a, b))
