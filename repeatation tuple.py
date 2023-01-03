Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(1,2,3)
t*2
(1, 2, 3, 1, 2, 3)
a=(1,2)
b=(3,4)
a+b
(1, 2, 3, 4)
t[0]=86
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t[0]=86
TypeError: 'tuple' object does not support item assignment
