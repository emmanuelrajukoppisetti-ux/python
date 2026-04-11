Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 #slicing
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
b="simple is better than complex"
b[10:16]
'better'
b[22:29]
'complex'
b[0:7]
'simple '
b[0:6]
'simple'
c="beautiful is better than ugly"
>>> c[0:9]
'beautiful'
>>> c[13:19]
'better'
>>> c[25:29]
'ugly'
>>> #negative slicing
>>> a="work hard until you succeed"
>>> a[-24:-28]
''
>>> a[-24]
'k'
>>> a[-23:]
' hard until you succeed'
>>> a[:-23]
'work'
>>> a[-27:-23]
'work'
>>> a[-17:-12]
'until'
>>> a[-22:-18]
'hard'
>>> a[-7:]
'succeed'
>>> b="vijayawada is a royal city"
>>> b[-10:-5]
'royal'
>>> b[:-17]
'vijayawad'
>>> b[-4:]
'city'
