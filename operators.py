Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#arthematic
#+,-,*,//,/,**,%
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
print(a%b)
2
#assignment
a=5
b=7
print(a+=)
SyntaxError: invalid syntax
a+=b
a
12
a-=3
a
9
a*=3
a
27
a//=2
a
13
a/=2
a
6.5
a**=2
a
42.25
a%=2
a
0.25
#comparision
a=5
d=9
a<b
True
a>b
False
a<=b
True
a>=b
False
a!=b
True
a==b
False
a=5
b=5
a==b
True
#logical
a=6
b=12
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<=b and b<=a
False
a>=b or b>=a
True
a<=b 0r b<=a
SyntaxError: invalid decimal literal
not true
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
#identify
a=4
if type(a) is int:
    print("it is int")

    
it is int
if type(a) is not int:
    print("its not int")

    

>>> 
>>> 
>>> #membership
...     
>>> a=2,3,4,5,6,7,8,9,10
>>> if 10 in a:
...     print(10)
... 
...     
10
>>> if 10 not in a:
...     print(10)
... 
...     
>>> 
>>> 
>>> 
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> 
>>> #bitwise
>>> a=6
>>> b=8
>>> a&b
0
>>> bin(6)
'0b110'
>>> bin(8)
'0b1000'
>>> a|b
14
>>> a~b
SyntaxError: invalid syntax
>>> a=2
>>> b=4
>>> a^b
6
>>> a=4
>>> a<<3
32
>>> a=5
>>> a>>2
1
