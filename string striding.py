Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 #striding
a="cloud coumpting"
a[::]
'cloud coumpting'
a[::1]
'cloud coumpting'
a[::3]
'cucmi'
a="Data Science"
a[::4]
'D e'
a[::2]
'Dt cec'
 a[::5]
 
SyntaxError: unexpected indent
a[::5]
'DSc'
a[::8]
'De'
a[1:8]
'ata Sci'
a[5:]
'Science'
a[3:9]
'a Scie'
>>> a[4:10]
' Scien'
>>> a="python course"
>>> a[0:5:2]
'pto'
>>> a[2:12:3]
'tnos'
>>> a[5:12:4]
'nu'
>>> a[1:11:5]
'y '
>>> a[0:9:2]
'pto o'
>>> #negative striding
>>> a="machine learining"
>>> a[-1:-12:-4]
'gil'
>>> a="machine learning"
>>> a[-1:-12:-4]
'gr '
>>> a[-2:-16:-5]
'nei'
>>> a[-4:-15:-2]
'naleic'
>>> a[::-1]
'gninrael enihcam'
>>> a[7:5:2]
''
>>> a[5:7:2]
'n'
a[-1:-12:-4]
text = "Python"

print(text[1:5:-1])

