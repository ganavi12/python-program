class Employee:
    no_of_emp =0
    bonus = 1.5

    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
        Employee.no_of_emp + = 1

    def payAmount(self):
        return int(self.pay * self.bonus)
e1 = Employee('test',2000)
print(e1.payAmount())
        
