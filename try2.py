try:
    n=int(input("enter no"))
    print(n**2)
    raise ValueError
except (KeyboardInterrupt,ValueError):
           print("bye")
else:
           print("tata")