
def roundoff(n, x):
    x = str(pow(10, -x))
    return Decimal(str(n)).quantize(Decimal(x), rounding=ROUND_HALF_UP)


n = 12.32461
x = 3
print(roundoff(n, x))
