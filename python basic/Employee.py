class Employee:
    no_of_emp =0
    bonus = 2.5

    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
        Employee.no_of_emp +=1

    def payAmount(self):
        return int(self.pay * self.bonus) # Employee.bonus gives class var values
    
e1 = Employee('test',2000)
e2= Employee('test1',3000)
e2.bonus = 2
print(e2.payAmount())
print(Employee.no_of_emp)
        z
