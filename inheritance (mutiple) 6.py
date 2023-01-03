class B1:
    def show(self):
        print("hello")
class B2:
    def disp(self):
        print("hai")
class D(B1,B2):
    def out(self):
        print("bye")
x=D()
x.show()
x.disp()
x.out()
