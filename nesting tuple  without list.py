Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,2,(3,4),5]
l[0]
1
l[1]
2
l[2]
(3, 4)
l[3]
5
l[2][0]
3
l[2][1]
4
l
[1, 2, (3, 4), 5]
l[0]=86
l
[86, 2, (3, 4), 5]
l[2][0]=44
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    l[2][0]=44
TypeError: 'tuple' object does not support item assignment
