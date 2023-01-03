def hcf(a,b,c):
    m=min(a,b,c)
    while(a%m!=0 or b%m!=0 or c%m!=0):
        m-=1
    return m
x=int(input('enter 1st no'))
y=int(input('enter 2nd no'))
z=int(input('enter 3rd no'))

r=hcf(x,y,z)
print('HCF OR GCD=',r)