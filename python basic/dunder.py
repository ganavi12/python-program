class Employee:
    bonus = 1.2

    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def __repr__(self):
        return f'{self.name},{self.pay}'
    def __str__(self):
        return f'val is {self.name},{self.pay}'
    
    def __add__(self,other):
        return self.pay + other.pay
e1 = Employee('test',40000)
e2 = Employee('test1',40000)
print(e1.__repr__())
print(e1,e2)
print(e1 + e2)
print(int.__add__(4,2) , int.__sub__(4,2),int.__mul__(4,2),str.__add__('a','b'))
