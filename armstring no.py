n=int(input('enter no'))
num=n
c=0
while n>0:
    c+=1
    n=n//10
n=num
s=10

while n>0:
    r=n%10
    s=s+r**c
    n=n//10
if s==num:
    print('armstrong')
else:
    print('not armstrong')
