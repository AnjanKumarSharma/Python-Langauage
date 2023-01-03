try:
    n=int(input("enter no"))
    if n>10 or n<1:
        raise ValueError
except (KeyboardInterrupt,ValueError):
    print("bye")
else:
   print("tata")