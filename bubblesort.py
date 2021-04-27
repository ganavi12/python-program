def bubble(a):
    try:
        for i in range(0, len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i], ] = a[i+1], temp
        for i in range(len(a)):
            print(a[i], end=' ')
    except Exception as e:
        print(e)


a = [10, 3, 1, 5, 2, 8, 0, 7]
bubble(a)
