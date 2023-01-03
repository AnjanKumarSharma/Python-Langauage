n=int(input('enter no'))
c=0
while n>0:
    r=n%10
    c=c*10+r
    n=n//10
print('rev of digits=',c)