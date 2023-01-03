sum=0
n=int(input('enter no'))
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print("sum of digits of that no.",sum)    