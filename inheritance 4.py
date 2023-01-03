#method overriding of init 
class B:
    def __init__(self):
        print("hello")
class D(B):
    def __init__(self):
        super().__init__()
        print("bye")

x=D()