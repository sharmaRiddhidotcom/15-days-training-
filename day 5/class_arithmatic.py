#perform the aerithmetic operations
class aerith:
    m=0
    n=0
    def __init__(self,m,n) -> None:
        self.m=m
        self.n=n
    def sum(self):
        ans=self.m+self.n
        print("Sum of",self.m,"&",self.n,"is",ans)
    def sub(self):
        ans=self.m-self.n
        print("Substraction of",self.m,"&",self.n,"is",ans)
    def mul(self):
        ans=self.m*self.n
        print("Multiplication of",self.m,"&",self.n,"is",ans)
    def div(self):
        ans=self.m/self.n
        print(self.m,"divide",self.n,"is",ans)
a=aerith(6,9)
a.sum()
a.sub()
a.mul()
a.div()

