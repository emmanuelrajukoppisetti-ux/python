Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#int
int(7)
7
int(4.7)
4
int("raju")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("raju")
ValueError: invalid literal for int() with base 10: 'raju'
int(7+9j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(7+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(4)
4.0

float(7.9)
7.9
float("raju")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("raju")
ValueError: could not convert string to float: 'raju'
float(3+7j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(3+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> #str
>>> str(2)
'2'
>>> str(9.8)
'9.8'
>>> str("raju")
'raju'
>>> str(3+8j)
'(3+8j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(2)
(2+0j)
>>> complex(3.9)
(3.9+0j)
>>> complex(3+8j)
(3+8j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool
>>> bool(9)
True
>>> bool(6.9)
True
>>> bool("raju")
True
>>> bool(6+9j)
True
>>> bool(True)
True
