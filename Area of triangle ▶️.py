import math
a=float(input('enter 1st side of triangele'))
b=float(input('enter 2nd side of triangele'))
c=float(input('enter 3rd side of triangele'))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle=",area)


