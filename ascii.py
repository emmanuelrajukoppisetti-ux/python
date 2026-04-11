Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#ASCII
>>> #chr()
>>> chr(90)
'Z'
>>> chr(20)
'\x14'
>>> chr(90)
'Z'
>>> chr(65)
'A'
>>> chr(90)
'Z'
>>> chr(91)
'['
>>> ord("a")
97
>>> ord("z")
122
>>> chr('a')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    chr('a')
TypeError: 'str' object cannot be interpreted as an integer
>>> chr(90)
'Z'
>>> ord("at")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ord("at")
TypeError: ord() expected a character, but string of length 2 found
>>> ord('9')
57
