def interest(p, r, t):
    print(
        "priciple is {0}, rate of interest {1} and time period id {2}".format(p, r, t))
    result = (p*r*t)/100
    print(result)


interest(1000, 5, 5)
