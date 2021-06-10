# calculate square of number
class cal4:
    def setdata(self, x):
        self.x = x

    def display(self):
        sq = self.x ** 2
        print("square of", self.x, "is", sq)


c = cal4()
c.setdata(10)
c.display()


