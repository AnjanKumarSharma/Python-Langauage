pr=int(input("previous month reading"))
cr=int(input("current month reading"))
tu=cr-pr 
if tu>0 and tu<=100:
    amt=tu*5
elif tu>100 and tu<=200:
    amt=(100*5)+(tu-100)*6
elif tu>200 and tu<=400:
    amt=(100*5)+(100)*6+(tu-200)*7
elif tu>400:
    amt=(100*5)+(100*6)+(200*7)+(tu-400)*8
print("amount",amt)
