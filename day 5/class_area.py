
#calculate area of circle
import math
class cal2:
    def setdata(self,r):
        self.r=r
    def area(self):
        area=math.pi*self.r**2
        self.area=area
    def display(self):
        print("Area is",self.area)
myc=cal2()
myc.setdata(4.6)
myc.area()
myc.display()



