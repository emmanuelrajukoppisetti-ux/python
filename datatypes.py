Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#datatypes
a=4
type(a)
<class 'int'>
b=100
type(b)
<class 'int'>
c=8.9
type(c)
<class 'float'>
d='code'
type(d)
<class 'str'>
e="emmanuel"
type(e)
<class 'str'>
f='''raju'''
type(f)
<class 'str'>
g="p"
type(g)
<class 'str'>
>>> x=5+9j
>>> type(x)
<class 'complex'>
>>> y=3j+2
>>> type(y)
<class 'complex'>
>>> z=6j
>>> type(z)
<class 'complex'>
>>> a=3+5i
SyntaxError: invalid decimal literal
>>> b=j
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b=j
NameError: name 'j' is not defined
>>> b="j"
>>> type(b)
<class 'str'>
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
>>> a=true
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a="true"
>>> tupe(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tupe(a)
NameError: name 'tupe' is not defined. Did you mean: 'tuple'?
>>> type(a)
<class 'str'>
