a = [4, 5, 1, 2, 9] 
N = 2
res = []
def larget_second(a):
    for i in range(len(a)): 
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                
    return a
x = larget_second(a)
print(x[-1:-1-2:-1])

            