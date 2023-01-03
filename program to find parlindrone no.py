n=int(input('enter no'))
num=n
c=0
while n>0:
    r=n%10
    c=c*10+r
    n=n//10
if c==num:
    print('palindrome no')
else:
    print('not palindrome no')