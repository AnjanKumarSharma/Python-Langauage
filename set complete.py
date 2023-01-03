Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a={1,2,3,4,5}
a.add(6)
a
{1, 2, 3, 4, 5, 6}
a.remove(3)
a
{1, 2, 4, 5, 6}
a.remove(9)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.remove(9)
KeyError: 9
a.discard(4)
a
{1, 2, 5, 6}
a.pop()
1
a
{2, 5, 6}
a.clear()
a
set()
a={1,2,3,4,5}
a={1,2,3,4,4}
a
{1, 2, 3, 4}
len(a)
4
max(a)
4
min(a)
1
3 in a
True
3 not in a
False
b={2,1,4,3}
b
{1, 2, 3, 4}
l=[2,3,1]
s=set(l)
all(s)
True
s={0,1,2}
s
{0, 1, 2}
all(s)
False
any(5)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    any(5)
TypeError: 'int' object is not iterable
a={1,2}
b={1,2}
a==b
True
a!=b
False
a={1,2,3}
b={3,4,5}
a|b
{1, 2, 3, 4, 5}
c=a.union(b)
c
{1, 2, 3, 4, 5}
a&b
{3}
print(a-b)
{1, 2}
print(a.difference(b))
{1, 2}
a is superset(b)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a is superset(b)
NameError: name 'superset' is not defined
b is superset(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    b is superset(a)
NameError: name 'superset' is not defined
a is subset (b)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a is subset (b)
NameError: name 'subset' is not defined
a={1,2,3,4}
b={3,4,5,6}
a.symmetric-difference(b)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.symmetric-difference(b)
AttributeError: 'set' object has no attribute 'symmetric'
z=a
print(z)
{1, 2, 3, 4}
prinr(a.copy())
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    prinr(a.copy())
NameError: name 'prinr' is not defined. Did you mean: 'print'?
a={1,2,3}
b={4,5}
print(a.isdisjoint (b))
True
b={3,4,5}
print(a.isdisjoint(b))
False
