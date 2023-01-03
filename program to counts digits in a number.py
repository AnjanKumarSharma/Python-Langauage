n=int(input('enter no')) 
if n==0:
    c=1
else:
    c=0
    while n>0:
        c=c+1
        n=n//10
    print('total digits=',c)