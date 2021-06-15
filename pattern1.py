
n = int(input("enter number"))
for i in range(n):
    # print(i)
    for j in range(i):
        print('*', end=" ")
    print(" ")

# n = int(input(""))
# for i in range(n):
#     for j in range(n):
#         print(i,end=" ")
#     print(" ")

# n=int(input(""))

# for i in range(n):
#     for j in range(n):
#         if j<n:
#             print(i,end=' ')
#     n = n-1
#     print(" ")

# n=int(input(""))
# for i in range(n):
#     for j in range(i):
#         print(j,end=' ')
#     print(" ")

# n = int(input(""))
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print(i,end=' ')
#     print(" ")

# n=int(input(" "))
# for i in range(n,0,-1):
#     for j in range(n):
#         if i+j >= n:
#             print(n,end=' ')
#     print(" ")

# n=int(input(" "))
# for i in range(n):
#     for j in range(n):
#         if i+j >= n:
#             print(n,end=' ')
#     print(" ")


# n=int(input(" "))
# for i in range(n,0,-1):
#     for j in range(n):
#         if i+j >= n:
#             print(n,end=' ')
#     print(' ')

# n=int(input(" "))
# for i in range(n):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print(' ')

# n=int(input(" "))
# for i in range(n):
#     for j in range(n):
#         if i+j<n:
#             print(j,end=' ')
#     print(' ')


# n=int(input(" "))
# l = 1
# for i in range(0,n):
#     for j in range(i,n):
#         # print(i,j,n)
#         # print(i,end=' ')
#         if i == j:
#             print(i,end=' ')
#         i=i+1
#     print(' ')


# n=int(input(" "))
# l = 1
# for i in range(0,n):
#     for j in range(i,n):
#         # print(i,j,n)
#         # print(i,end=' ')
#         if i == j:
#             print(i,end=' ')
#             i=i+1
#     print(' ')


# def test(n):
#     for i in range(0,n+1):
#         for j in range(i):
#             print('*',end=' ')
#         print(" ")
# n=int(input(" "))
# test(n)


# def test(n):
#     a = []
#     for i in range(0,n+1):
#         a.append('*'*i)
#     print("\n".join(a))
# n=int(input(" "))
# test(n)


# def test(n):
#     for i in range(n):
#         for j in range(n):
#             # print(i,j,n)
#             if i == j or j>i:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print(" ")
# n=int(input(" "))
# test(n)


# def test(n):
#     for i in range(n):
#         for j in range(n):
#             if i + j >= n:
#                 print('*',end=' ')
#             else:
#                 print(' ',end=' ')
#         print(" ")
# n=int(input(" "))
# test(n)


# def test(n):
#     for i in range(n+1):
#         for j in range(n+1):
#             if i+j/2 == 0:
#                 print('*',end=' ')
#         print(" ")
# n=int(input(" "))
# test(n)

# n = int(input("please enter diamond's height:"))
# for i in range(n):
#     print(" "*(n-i), "*"*(i*2+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i), "*"*(i*2+1))
