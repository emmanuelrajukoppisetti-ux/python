Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]
' '
a[4]
' '
a[7]
' '
a[1]+a[4]+a[7]
'   '
a="I love python"
a[2]+a[3]+a[4]+a[5]
'love'
a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'python'
b="Time is very precious"
>>> a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
IndexError: string index out of range
>>> b="Time is very precious"
>>> b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'precious'
>>> 
>>> 
>>> b[8]+b[9]+b[10]+b[11]
'very'
>>> a="work hard"
>>> a[5]+a[6]+a[7]+a[8]
'hard'
>>> a[-4]+a[-3]+a[-2]+a[-1]
'hard'
>>> a[-9]+a[-8]+a[-7]+[-6]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[-9]+a[-8]+a[-7]+[-6]
TypeError: can only concatenate str (not "list") to str
>>> a[-9]+a[-8]+a[-7]+a[-6]
'work'
>>> b="i am learning python"
>>> b[-15]+b[-14]+b[-13]+b[-12]+b[-11]+b[-10]+b[-9]+b[-8]
'learning'
>>> b[-18]+b[-17]
'am'
>>> b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'python'
