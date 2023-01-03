Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a={1,2,3}
b={4,5}
a.updata(b)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.updata(b)
AttributeError: 'set' object has no attribute 'updata'. Did you mean: 'update'?
a
{1, 2, 3}
a.update(b)
a
{1, 2, 3, 4, 5}
