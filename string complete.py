Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n='RAVI'
r=12
print(" my name is%s and my rollis%d"%('RAVI',12))
 my name isRAVI and my rollis12
s='ANJAN'
s.capitalize()
'Anjan'
s.center(12,'*')
'***ANJAN****'
s='RAM IS A GOOD BOY. RAEDS A BOOK'
s.count('A',0,len(s))
4
s.count('RAM',0,len(s))
1
s.count('A',0,10)
2
s.endswith('BOOK',0,len(s))
True
s.endswith('K',0,len(s))
True
s.endswith('BOOK',0,17)
False
s.endswith('BOy',0,17)
False
S='RAM IS A GOOD BOY. RAM READS A BOOK'
S.startswith('RAM',0,len(s))
True
s.endswith('BOOK',0,len(s))

True
S.startswith('RAM',0,10))
SyntaxError: unmatched ')'
S.startswith('RAM',0,10)
True
S.startswith('RAM',10,len(s))
False
S.startswith('RAM',19,len(s))
True
S.find('GOOD',0,len(s))
9
S.find('BAD',0,len(s))
-1
S.index('GOOD',0,len(s))
9
S.index('BAD',0,len(s))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    S.index('BAD',0,len(s))
ValueError: substring not found
S.rfind('RAM',0,len(s))
19
S.find('RAM',0,len(s))
0
S.rindex('RAM',0,len(s))
19
S.index('RAM',0,len(s))
0
s='ANJAN'
S.ljust(10,'*')
'RAM IS A GOOD BOY. RAM READS A BOOK'
s.ljust(10,'*')
'ANJAN*****'
s.rjust(10,'*')
'*****ANJAN'
s='1234'
s.zfill(10)
'0000001234'
x='1234'
s.str(x)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.str(x)
AttributeError: 'str' object has no attribute 'str'
s.str(x)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s.str(x)
AttributeError: 'str' object has no attribute 'str'
s.zfill(10)
'0000001234'
s='ANJAN'
s.lower()
'anjan'
s
'ANJAN'
s.upper()
'ANJAN'
s
'ANJAN'
s.capitalize()
'Anjan'
s
'ANJAN'
s='anjan KUMAR SHARMA'
s.title()
'Anjan Kumar Sharma'
s.swapcase()
'ANJAN kumar sharma'
s
'anjan KUMAR SHARMA'
s='______ANJAN'
s.lstrip()
'______ANJAN'
s
'______ANJAN'
s='Anjan'
r='Sharma'
s+r
'AnjanSharma'
s+ ' '+r
'Anjan Sharma'
a='____KHUSHI___'
a.lstrip()
'____KHUSHI___'
a.rstrip()
'____KHUSHI___'
a
'____KHUSHI___'
'____KHUSHI___'
'____KHUSHI___'
a.strip()
'____KHUSHI___'
a
'____KHUSHI___'
a.strip()
'____KHUSHI___'
a
'____KHUSHI___'
a='ABC'
max(a)
'C'
min(a)
'A'
len(a)
3
s='Aba'
max(s)
'b'
min(s)
'A'
s='ANJAN ANJAN KHUSHI KHUSHI KHUSHBOO ANJAN KHUSHI SHARMA'
s.replace('anjan','KUNAL')
'ANJAN ANJAN KHUSHI KHUSHI KHUSHBOO ANJAN KHUSHI SHARMA'
s
'ANJAN ANJAN KHUSHI KHUSHI KHUSHBOO ANJAN KHUSHI SHARMA'
s.replace('ANJAN','KUNAL')
'KUNAL KUNAL KHUSHI KHUSHI KHUSHBOO KUNAL KHUSHI SHARMA'
S='ANJAN,KUMAR,SHARMA'
print(S.split(','))
['ANJAN', 'KUMAR', 'SHARMA']
l=['ANJAN','KUMAR','SHARMA']
print(','.join(l))
ANJAN,KUMAR,SHARMA
