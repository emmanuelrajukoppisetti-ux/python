Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=6
>>> print(a)
6
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> Name="emmanuel"
>>> print(name)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined. Did you mean: 'Name'?
>>> print(Name)
emmanuel
>>> Age=21
>>> print(Age)
21
>>> AGE=21
>>> print(AGE)
21
