def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print('factorial of',n,'is',f)
num=int(input('enter no'))
fact(num)