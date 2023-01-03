a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)