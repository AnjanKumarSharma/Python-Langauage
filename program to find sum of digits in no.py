n=int(input('enter no'))
c=0
while n>0:
    r=n%10
    c=c+r
    n=n//10
print('sum of digits=',c)