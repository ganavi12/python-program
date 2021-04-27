class Employee:
    def __init__(self):
        self.empdata = {}
    def add(self):
        name = input("enter name")
        pay = int(input("enter sal"))
        self.empdata['name'] = name
        self.empdata['pay'] = pay
    def display(self):
        for i in self.empdata:
            print(i,'is',self.empdata.get(i))
    def delete(self):
        name = input("enter delete key")
        if name in self.empdata:
            self.empdata.pop(name)
        else:
            print("key not present ")
        print("updates detail is ",self.empdata)
        

e = Employee()
while True:
    print ('''
        enter 1 to add emp details
        enter 2 to dislpay emp details
        enter 3 to delete emp
        enter 4 to exit 
        
''')

    choice = int(input("enter the choice :\n"))
    if choice == 1:
        e.add()
    elif choice == 2:
        e.display()
    elif choice ==3 :
        e.delete()
    elif choice == 4 :
        print("exit")
        break
    else:
        print("invalid choice")
