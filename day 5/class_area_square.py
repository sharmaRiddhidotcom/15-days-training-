#calculate area of square
class cal6:
    def setdata(self,s):
        self.s=s
    def area(self):
        area=self.s**2
        self.area=area
    def declare(self):
        print("Area of sqaure is",self.area)
c=cal6()
c.setdata(15)
c.area()
c.declare()

