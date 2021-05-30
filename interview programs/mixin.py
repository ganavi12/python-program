
class A:
    total = 10
class B(A):
    pass
class C(A):
    pass
class M:
    def get_data(self):
        return self.total
class D(B, M):
    pass
class E(C, M):
    pass 
e1 = E()
print(e1.get_data()) 

m1 = M()
print(m1.get_data())