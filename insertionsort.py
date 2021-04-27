def insertion_sort(a):
    # for index in range(len(a)-(len(a)-1),len(a)):
    for index in range(1,len(a)):
        value = a[index]
        i = index-1
        while i>=0 and value < a[i]:
            a[i+1]  = a[i]
            i = i - 1
        a[i+1] = value
    for i in range(len(a)): 
        print (a[i],end=' ')

a=[10,8,1,5,6,78]
insertion_sort(a)


# def insertion_sort(a):
#     for i in range(len(a)-(len(a) -1),len(a)):
#         value = a[i]
#         j = i-1
#         while j>=0:
#             if value < a[j]:
#                 a[j+1] = a[j]
#                 a[j] = value
#                 j = j- 1
#                 return a
#             else:
#                 break
# a=[4,5,1,2,8,9,0,3,7]
# res = insertion_sort(a)
# print(res)

        


