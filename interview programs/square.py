def square(n):
    sq = 0
    for i in range(1, n+1):
        sq = sq + i*i
    return sq


n = int(input("enter no"))
print(square(n))
