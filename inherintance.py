class Employee:
    inc = 1.5

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.'+lname+'@mail.com'

    def list(self):
        return f'name of employe is {self.fname} {self.lname} and slaray is {self.pay} and mail id is {self.email}'

    def totalpay(self):
        self.pay = int(self.inc * self.pay)
        return self.pay

    @classmethod
    def inc_amount(cls, amount):
        cls.inc = amount
        return cls.inc


# e1 = Employee("ganavi", "gowda", 60000)
# e2 = Employee("sachin", 'krisha', 50000)

# print(e1.list())
# print(e1.totalpay())

class developer(Employee):
    inc = 2.1

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang = prog_lang


class manager(Employee):
    def __init__(self, fname, lname, pay, employess=None):
        super().__init__(fname, lname, pay)
        if employess is None:
            self.employess = []
        self.employess = employess

    def add_emp(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)

    def remove_emp(self, emp):
        if emp in self.employess:
            self.employess.remove(emp)

    def list_emp(self):
        # for emp in self.employess:
        #     print(emp)
        return len(self.employess)


d1 = developer("ganavi", "gowda", 60000, 'python')
d2 = developer("sachin", 'krisha', 50000, 'java')

m1 = manager("ganavi", "gowda", 60000, [d1])
# print(m1.email)
# m1.add_emp(d2)
# m1.remove_emp(d1)
# print(m1.list_emp())

print(isinstance(m1, Employee))
print(isinstance(m1, manager))
print(isinstance(m1, developer))
print(isinstance(d1, Employee))
print(isinstance(Employee, developer))

print(issubclass(Employee, developer))
print(issubclass(developer, Employee))
print(issubclass(developer, manager))
print(issubclass(manager, Employee))
print(issubclass(Employee, manager))

# print(d1.list())
# print(d1.pay)
# print(d1.totalpay())
# print(d1.inc_amount(3))

# print(help(developer))
# print(help(Employee))
