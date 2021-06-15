def remove(a, n):
    s = ''
    for i in range(len(a)):
        if i != n:
            s = s + a[i]
    return s

print(remove('GeeksForGeeks',2))


            