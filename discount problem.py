a=int(input("enter prchase amount:- "))
if a>=1000 and a<3000:
    b=a-(a/10)
elif a>=3000 and a<5000:
    b=a-(a*0.15)
elif a>=5000:
    b=a-(a/5)
elif a<1000:
    b=a
print("net payable:-",int(b))             
