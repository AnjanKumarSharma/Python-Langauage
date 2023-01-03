class A:
    def show(self):
        print("hello")
class B(A):
    def disp(self):
        print("hai")
class C(A):
    def out(self):
        print("bye")
class D(B):
    def printing (self):
        print("tata")
T=D()
P=C()
T.show()
T.disp()
T.printing()
P.show()
T.out()
