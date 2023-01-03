try:
    n=int(input("enter no"))
    print(n**2)
except (KeyboardInterrupt,ValueError):
           print("bye")
else:
           print("tata")