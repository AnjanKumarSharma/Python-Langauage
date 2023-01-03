rev=0
n=int(input("enter no."))
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reverse of the digit=",rev)    