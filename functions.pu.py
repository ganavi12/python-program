def func1(n):
    a = []
    for i in range(1,n):
        if i%2 == 0:
            a.append(i**2)
        
        else:
             a.append(i) 
    # print(a)
    return a 
n = int(input("enter num"))
print(func1(n))   
# print(func1)   return address of func1
