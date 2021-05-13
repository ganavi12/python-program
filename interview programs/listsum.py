# a = [1, 2, 3, 4]
# print(sum(a))

def largest(a):
    max = a[0] 
    for i in range(0, len(a)):
        if a[i] > max:
            max = a[i]
    print(max) 
a = [3,55,6,1,2]
res = largest(a)
# print(res) 