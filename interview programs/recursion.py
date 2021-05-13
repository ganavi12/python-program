# def s1(a, b):
#     if len(b) > a:
#         s1(a + 1, b)
#         print(b[a], end='')
# s1(0,'karma')


# a = 2

# print(id(2))
# print(id(a))


# Note: You may get different values for the id

# a = 2
# print('id(a) =', id(a))
# print('id(2) =', id(2))

# a = a+1
# print('id(a) =', id(a))

# print('id(3) =', id(3))

# b = 2
# print('id(b) =', id(b))
# print('id(2) =', id(2))


# a = 10
# def outside():
#     print(id(a), a)
#     def inside():
#         a=2
#         print("inside function",a)

 # var1 is in the global namespace
# var1 = 5
# def some_func():
 
#     # var2 is in the local namespace
#     var2 = 6
#     def some_inner_func():
 
#         # var3 is in the nested local
#         # namespace
#         var3 = 7

# count = 5
# def some_method():
#     global count
#     # count =2
#     count = count + 1
#     print(count)
# some_method() 


class Test:
    x = 1
    def calc(self):
        y=2
        return self.x + 10
    # print(x+y) //can not access y ,it can use only inside calc function 
d1 = Test()
print(d1.calc())