import math
a=eval(input("enter first coefficient:-"))
b=eval(input("enter second coefficient:-"))
c=eval(input("enter third coefficient:-"))
d=(b**2)-(4*a*c)
if d>=0:
    v1=(-b+math.sqrt(d))/(2*a)
    v2=(-b-math.sqrt(d))/(2*a)
    print("value=",v1, "value=",v2)
else:
    print("value not possible")