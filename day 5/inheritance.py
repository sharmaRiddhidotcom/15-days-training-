class Parent:
    def __init__(self):
        print("parent class constructor")
    def parentmethod(self,name,des):
        self.name=name
        self.des=des
        print(self.name,"is",self.des)
class Child(Parent):
    def __init__(self):
        print("child class constructor")
    def childmethod(self,salary):
        self.salary=salary
        print("salary is",self.salary)
c=Child()
c.childmethod(20000)
c.parentmethod("riddhi","computer Engineer")
