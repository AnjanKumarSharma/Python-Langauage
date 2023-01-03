class test:
    num=0
    def input(self,h):
        self.num=h
    def output(self):
        print(self.num)
    def __add__(self,t):
        z=test()
        z.num=self.num
        t.num
        return z
a=test()
a.input(20)
a.output()
b=test()
b=input(30)
b.output()
c=test()
c=a+b
c.output()