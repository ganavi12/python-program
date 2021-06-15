# multiple


# class A:
#     def __init__(self):
#         self.str1 = "test1"
#         print("base class 1")
# class B:
#     def __init__(self):
#         self.str2 = "test2"
#         print("base class 2")

# class C(A, B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print("class c")
    
#     def display_str(self):
#         return f"{self.str1}, {self.str2}"

# c1 = C()
# print(c1.display_str())

# hierarchical

# class Employee:
#     inc = 1
#     def __init__(self, name, pay):
#         self.name = name
#         self.pay = pay
    
#     def display(self):
#         print(self.name, self.pay)

#     def increment(self, amount):
#         self.pay = int(self.pay * amount)
#         print(self.pay)

# class Developer(Employee):
#     inc = 2
#     def __init__(self, name, pay,prg_language):
#         super().__init__(name, pay)
#         self.prg_language = prg_language


# d1 = Developer("ganavi", 70000, 'python')
# print(d1.inc)
# class Manager(Employee):
#     def __init__(self, name, pay,employees = None):
#         super().__init__(name, pay)
#         if self.employees is None:
#             self.employees = []
#         self.employees = employees


#     def add_emp(self, emp):
#         if emp not in Employee:
#             self.employees.append(emp)

#     def remove_emp(self, emp):
#         if emp in Employee:
#             self.employees.remove(emp)
#     def list(self):
#         print(self.employees)

# m1 = Manager('savitha', 100000)
# m1.add_emp("test")
# print(m1.list()) 
        
class A:
    def __init__(self, name):
        self.name = name
    def display_a(self):
        print(self.name)
class B(A):
    def __init__(self, name, age):
        A.__init__(self,name)
        self.age = age

    def display_b(self):
        print(self.age)


class C(A):
    def __init__(self, name,city):
        super().__init__(name)
        self.city = city

    def display_c(self):
        super().display_a()
        print(self.city)

c1 = C("ganavi", 'mysore')
c1.display_c()
print(isinstance(c1, A))
print(isinstance(c1, B))
print(issubclass(C, B))
print(issubclass(C, A))
print(issubclass(A, B))
print(issubclass(B,A))







        
    


