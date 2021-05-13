# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# a, b = (input("enter two numbers").split())
# print(max(int(a), int(b)))


# another way
# a, b = (input("enter two numbers").split())
# print(max((int(a), int(b))))


# find first non repeating interger in a list
a = [9, 2, 3, 2, 6, 6]
b = []
for i in a:
    if i in b:
        b.remove(i)
    else:
        b.append(i)
       
print(b) 
    
# find two largest number in list
# mylist = []
# a = [6, 2, 3, 2, 9]
# max = 0
# for i in a:
#     if i > max:
#         max = i
#         mylist.append(max)


# print('The largest number in list is', mylist)