class Test:
    company = 'google'
    def __init__(self,efirst,elast):
        self.first = efirst
        self.last = elast
        self.mail = efirst +'.'+elast+'@'+self.company+'com'
    def display(self):
        return f'email = {self.mail} and name = {self.first} {self.last}'
n = int(input("enter no of emp"))
for i in range(0,n):
    efirst = input("enter firstname")
    elast = input("enter lastname")      
t1 = Test(efirst,elast)
t2 = Test("test","user")
#print(t1.display());
print(t1.__dict__)
