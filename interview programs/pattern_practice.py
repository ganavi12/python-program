# for i in range(0,5):
#     for j in range(i):
#         print("*", end=' ')
#     print(' ')


# n = 5
# for i in range(n):
#     for j in range(i):
#         if i >= j:
#             print('*',end=" ")
#     print(" ")





n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>= j:
            print('*', end=" ")
        else:
            print(" ", end=' ')
    print("")

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i +j >= n+1:
            print('*', end=" ")
        else:
            print(" ", end=' ')
    print("")



n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print('*', end=" ")
        else:
            print(" ", end=' ')
    print("")



n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i + j <= n+1:
            print('*', end=" ")
        else:
            print(" ", end=' ')
    print("")




