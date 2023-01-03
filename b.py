l=[]
for i in range(1,11):
    n=int(input('enter value'))
    l.append(n)
l.sort()
s=int(input("enter search value"))
min=0
max=9
while min<=max:
    mid=int((min+ max)/2)
    if l[mid]==s:
        print('found')
        break
    if s>l[mid]:
        min=mid+1
    if s<l[min]:
        max=min-1
if min>max:
    print('not found')

