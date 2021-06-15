a = [12, 35, 9, 56, 24]
#  putput [24,35,9,56,12]

def swap_last_first(a):
    n = a[0]
    a[0] = a[len(a) - 1]
    a[len(a) - 1] = n
    return a
print(swap_last_first(a))


    
# a = [12, 35, 9, 56, 24]
# b, a = a.index(a(len) - 1), a.index(0)
# a[0], a[len(a) - 1] = b, a
# print(a)
