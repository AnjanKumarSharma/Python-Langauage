class test:
      def __init__(self,n):
            self.num=n
      def __del__(self):
            print(self.num)
a=test(10)
b=test(20)
c=test(30)
del a
del b
del c