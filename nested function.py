def small(x,y):
    if x>y:
        return x
    else:
        return y
add=lambda x,y:x+y
sub=lambda x,y:x-y
print(small(add(2,3),sub(2,3)))