class cal5:
    l=0
    w=0
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def calarea(self):
        area=self.l*self.w
        self.area=area
    def display(self):
        print("Area of rectangle is",self.area)
c=cal5(25,40)
c.calarea()
c.display()
