Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={1,2,3}
type(s)
<class 'set'>
s
{1, 2, 3}
s[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s(0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s(0)
TypeError: 'set' object is not callable
