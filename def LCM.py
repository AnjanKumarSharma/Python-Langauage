def lcm(a,b,c):
    m=max(a,b,c)
    while(m%a!=0 or m%b!=0 or m%c!=0):
        m+=1
    return m
x=int(input('enter 1st no'))
y=int(input('enter 2nd no'))
z=int(input('enter 3rd no'))

r=lcm(x,y,z)
print('LCM=',r)