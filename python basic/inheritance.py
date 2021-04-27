class Employee:
    bonus = 2
    emp_count = 10
    cname = 'google'

    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
        self.mail = name+'@'+self.cname+'.com'
    def display(self):
        return f'employee name is {self.name} and salary is {self.pay} and mail-id is {self.mail}'
class Developer(Employee):
    bonus = 10
    def __init__(self,name,pay,prog_lang):
        super().__init__(name,pay)
        self.prog_lang = prog_lang
class Manager(Employee):
    def __init__(self,name,pay,emp = None):
        super().__init__(name,pay)
        if emp is None:
            self.emp = []
        else:
            self.emp = emp
    def addemp(self,employ):
        if employ not in self.emp:
            self.emp.append(employ)
    def removemp(self,employ):
        if employ in self.emp:
            self.emp.remove(employ)
    def listemp(self):
        return f'{self.emp}'
        
e1 = Employee('ganavi',60000)
d1 = Developer('test',30000,'python')

m1 = Manager('test',30000,[])
print(m1.listemp())
m1.addemp("new")
m1.addemp("john")
print(m1.listemp())
m1.removemp("new")
print(m1.listemp())
#print(help(Developer)
