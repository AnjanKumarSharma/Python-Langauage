#method overriding of init 
class B:
    def __init__(self):
        print("hello")
class D(B):
    def __init__(self):
        
        print("bye")

x=D()