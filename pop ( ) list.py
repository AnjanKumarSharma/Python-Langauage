Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,2,3]
l.pop()
3
l
[1, 2]
m=[1,2,3]
m=pop(1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    m=pop(1)
NameError: name 'pop' is not defined. Did you mean: 'pow'?
m.pop(1)
2

m
[1, 3]
