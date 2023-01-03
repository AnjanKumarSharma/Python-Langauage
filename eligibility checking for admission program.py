marks=int(input("enter total marks"))
if marks>=300 and marks<=500:
    print("eligible")
else:
   p=int(input("enter mark of physics"))
   c=int(input("enter mark of chemistry"))
   m=int(input("enter mark of mathematics"))
   if  (p+c+m)>=210: 
      print("eligible")
   else:
     print("not eligible for admission")   
