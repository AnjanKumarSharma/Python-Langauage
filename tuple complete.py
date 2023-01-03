Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(1,2,3)
del t[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    del t[0]
TypeError: 'tuple' object doesn't support item deletion
t
(1, 2, 3)
det t[0]
SyntaxError: invalid syntax
t=(1,2,3)
5 in t
False
2 in t
True
5 not in t
True
2 not in t
False
len(t)
3
for i in[1,2,3]
SyntaxError: expected ':'
for i in [1,2,3]
SyntaxError: expected ':'
for i in [1,2,3]:
    print(i)

    
1
2
3
for i in (1,2,3):
    print(i)

    
1
2
3
a=(1,2,3)
b=(1,2,3)
a==b
True
c=(4,5)
a==c
False
t=(1,2,3,4)
max(t)
4
min(t)
1
l=[1,2,3]
t=tuple(l)
l
[1, 2, 3]
t
(1, 2, 3)
t=(1,2,3)
l=list(t)
l
[1, 2, 3]
t=(1,2,3,4)
t.index(3)
2
t=(1,2,1,2,3,2)
t.count(2)
3
