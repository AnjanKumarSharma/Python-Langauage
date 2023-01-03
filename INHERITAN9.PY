# MUTLTI LEVEL INHERITANCE
class A:
    def show(self):
        print("hello")
class B(A):
    def disp(self):
        print("hai")
class C:
    def out(self):
        print("bye")
class D(B,C):
    def printing (self):
        print("tata")
T=D()

T.show()
T.disp()

T.out()
T.printing()