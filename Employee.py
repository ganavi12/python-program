import datetime


class Employee:
    increment = 1.5

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self. mail = fname + '.' + lname + '@test.com'

    def display(self):
        return self.fname + '.' + self.lname

    def salaryinc(self):
        # return int(int(self.pay) * Employee.increment)
        return int(int(self.pay) * self.increment)

    @classmethod
    def set_newinc(cls, amount):
        cls.increment = amount
        return cls.increment

    @classmethod
    def getsplitdata(cls, str_data):
        first, last = str_data.split('-')
        return first, last

    @staticmethod
    def weekoffcheck(x):
        if x.weekday() == 5 or x.weekday() == 6:
            return False
        return True


        # num = int(input("enter number of employye"))
        # for i in range(num):
        # fname = input("enter employee first name")
        # lname = input("enter employee last name")
        # pay = int(input("enter salary"))
fname, lname, pay = 'ganavi', 'gowda', '60000'
e1 = Employee(fname, lname, pay)
e2 = Employee(fname, lname, pay)
# e1.display()
# print(e1)
# print(e1.mail)
# print(e1.display)
# e1.increment = 1.7
# print(e1.__dict__, "\n")
# print(Employee.__dict__)
# print(Employee.increment, e1.increment, e2.increment)
# print(e2.salaryinc())
# print(Employee.salaryinc(e1))
# print(e1.salaryinc())

# print(Employee.set_newinc(10))
# print(e1.set_newinc(11))
# print(Employee.getsplitdata("ganavi-gowda"))

x = datetime.date(2021, 2, 15)
print(Employee.weekoffcheck(x))
