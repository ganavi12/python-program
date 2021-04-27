'''a = [i for i in range(10) if i%2==0]
b = [j for j in 'word']
print('the value of {} {}'.format(a,b))
for i in enumerate(range(0,10)):
    print(i)'''
'''def sum(a,b):
    return a+b,a-b,a*b,a/b;
a = int(input("enter a val"))
b = int(input("enter a val"))
print(sum(a,b))


for key,values in enumerate(range(10)):
    print(key,values)'''


'''class sample:
    x=10;
    y=20;
    def __init__(self,a,b):
        print("init",self)
        self.a = a
        self.b = b
        #print( a+b,a-b,a*b,a/b)
    def disp(self):
        print("disp",self)
s = sample(2,4)
s.disp()
s1 = sample(2,3)
s.disp()
#print(s.x,s.y)'''



'''n = int(input("enter value"))
a = []

for i in range (0,n):
    inp = int(input("enter element"))
    a.append(inp)
res = sum(a)/n
print("value is",res) '''

'''x = int(input("enter x "))
y = int(input("enter y"))
x = x + y
y = x - y
x = x- y
print("x",x,"y",y)'''


'''a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is:",new)'''

'''a = []
x = int(input("enter range"))
for i in range(0,x):
    val = int(input("enter elements to list"))
    a.append(val)
a.sort()
print(a[x-2])'''




    


