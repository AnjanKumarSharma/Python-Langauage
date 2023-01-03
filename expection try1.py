a=0
b=0
try:
    a=int(input("enter first no"))
    b=int(input("enter 2nd no"))
    print('Div=',a/b)
except ZeroDivisionError:
    print('Error due to diving a no by 0')
    b=int(input('enter value of b'))
    print('Div=',a/b)