class b: #method overriding
    def show(self):
        print("hello")
class d(b):
    def show(self):
        print("bye")
x=d()
x.show()
y=b()
y.show()