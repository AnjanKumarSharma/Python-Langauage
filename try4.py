try:
    n=int(input("enter no"))
    print(n**2)
        
except (KeyboardInterrupt,ValueError):
         print("bye")
finally:
   print("tata")
   # it will be  no matter exception occured or not ,defined or not defined.
