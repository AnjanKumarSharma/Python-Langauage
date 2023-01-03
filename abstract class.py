class fruit:
    def taste(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
class   mango(fruit):
    def taste(self):
        print("Sweet")
    def color(self):
        print("yellow")
class   organe(fruit):
    def taste(self):
        print("Sweet & Sour")
    def color(self):
        print("organe")
m=mango()
m.taste()
m.color()
n=organe()
n.taste()
n.color()
