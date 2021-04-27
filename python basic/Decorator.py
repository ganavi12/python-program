class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
    @property
    def fullname(self):
        return '{}{}'.format(self.fname,self.lname)
    @email.setter
    def email(self,name):
        fname,lname = name.split(' ')
        self.fname = fname
        self.lname = lname
    @email.deleter
    def email(self):
        print("here")
        fname = None
        lname = None
        
e1 = Employee("ganavi","gowda")
e1.email = 'ranjitha gowda'
print(e1.email)
print(e1.fullname)
del e1.email

