class publisher:
    def __init__(self) -> None:
        print("This is Parent class constructor")

    def title(self, t):
        self.t = t
        print("The title of book is", self.t)


class book(publisher):
    def bookmethod(self, page_no):
        self.page_no = page_no
        print("Member data is in page no", self.page_no)


class tape(publisher):
    def __init__(self) -> None:
        print("This is child2 class constructor")

    def fun1(self, time):
        self.time = time
        print("Timing is", self.time)


p = tape()
t = book()
p.title("Ikigai")
t.bookmethod(44)
p.fun1("1 hour")
