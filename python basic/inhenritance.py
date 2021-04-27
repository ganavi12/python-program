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
    @classmethod
    def increaseBonus(cls,inc):
        cls.bonus = inc
        return cls.bonus
    @staticmethod
    def amount(empname):
        emp = empname.replace(empname,"xxx")
        return f' emp name {emp}'
class Developer(Employee):
    pass
e1 = Employee('ganavi',60000)
#d1 = Developer('test',30000)
e1.increaseBonus(10)
print(e1.amount("ganavi"))
print(e1.bonus)
#print(help(Developer))
