def factorial(n):

    f=1
    if (n==1):
        return 1
    else:
        f=n*factorial(n-1)
        return f
num=int(input('enter no'))
z=factorial(num)
print('factorial of',num,"is",z)