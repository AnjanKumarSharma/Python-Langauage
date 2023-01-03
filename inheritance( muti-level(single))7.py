class A:
    def show(self):
        print("hello")
class B(A):
    def disp(self):
        print("hai")
class C(B):
    def out(self):
        print("bye")
X=C()
X.show()
X.disp()
X.out()
