Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#String methods
#len
a="codegnan"
len(a)
8
b=
SyntaxError: invalid syntax
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count
a="twinkle twinkle litter star"
count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
#find a string
a="code"
a.find("d")
2
a[2]
'd'
b="codegnan"
b.find("n")
5
b.find("r")
-1
c="hellow"
c.find("l")
2
c[2:4]
'll'
d="raju"
d.find("u")
3
#escape sequence
#\n ->new line
#\t ->tab space
a="name\nmobilenumber\tmailid\ncity"
print(a)
name
mobilenumber	mailid
city
a="name:emmanuel\nmobileno:9618978147\nemail:emmanuelrajukoppisetti@gmail.com\tcity:mandapeta"
print(a)
name:emmanuel
mobileno:9618978147
email:emmanuelrajukoppisetti@gmail.com	city:mandapeta
#replace()
a="wait untill you succeed"
a.replace("wait","work")
'work untill you succeed'
a="wait wait untill you succeed"
a.replace("wait","hard work")
'hard work hard work untill you succeed'
b.replace("wait","work",1)
'codegnan'
a.replace("wait","work",1)
'work wait untill you succeed'
#upper
a="emmanuel"
a.upper()
'EMMANUEL'
b="PYTHON"
b.lower()
'python'
c="raju"
c.capitalize()
'Raju'
d="python course"
d.title()
'Python Course'
e="my name is emmanuel"
e.title()
'My Name Is Emmanuel'
#isupper,islower,isdigit
a="python"
a.isupper()
False
a.islower()
True
a.isalpha()
True
b="python full stack"
b.isalpha()
False
b.isdigit()
False
c=5485
c.isdigit()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    c.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="3456"
d.isdigit()
True
e="codegnan"
e.startwith("c")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    e.startwith("c")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
e.startswith("c")
True
e.endswith("n")
True
e.endswith("r")
False
a="Apple"
a.isalnum()
True
b="Apple9"
a.isalnum()
True
#strip
#lstrip(),rstrip()
a="        raju       "
a.strip()
'raju'
a.lstrip()
'raju       '
a.rstrip()
'        raju'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i love python"
a.split()
['python', 'java', 'c', 'c++']
b.split()
['i', 'love', 'python']
c="emmanuel raju"
c.split()
['emmanuel', 'raju']
#join()
a="python","java","c","c++"
"".join(a)
'pythonjavacc++'
" ".join(a)
'python java c c++'
",".join(a)
'python,java,c,c++'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="emmanuel"
lname="raju"
print(fname+lname)
emmanuelraju
print(fname+" "+lname)
emmanuel raju
print((fname+lname).title())
Emmanuelraju
print((fname+" "+lname).title())
Emmanuel Raju
#formating
a=4
b=7
print(a+b)
11
print("the sum is",a+b)
the sum is 11
print("the sum is,a+b")
the sum is,a+b
x="emmanuel"
y="raju"
print("full name is",x+y)
full name is emmanuelraju
print("full name is",x+" "+y)
full name is emmanuel raju
print("full name is",(x+" "+y).title())
full name is Emmanuel Raju
city="vij"
print(city)
vij
print("city is",city)
city is vij
>>> #format method
>>> a="chota"
>>> b="bheem"
>>> print("hello {}{}".format(a,b))
hello chotabheem
>>> print("hello {} {}".format(a,b))
hello chota bheem
>>> print("hello {} {}".format(a,b).title())
Hello Chota Bheem
>>> print("hello {} hello{}".format(a,b))
hello chota hellobheem
>>> print("hello {} hello {}".format(a,b) .title())
Hello Chota Hello Bheem
>>> #formating string
>>> a="john"
>>> b="henry"
>>> print(f"hello {a} {b}")
hello john henry
>>> print(f"hello {a} {b}")
... 
hello john henry
>>> print(f"hello {a} hello {b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"hello {a} hello {b}")
...       
hello john hello henry
>>> print(f"hello {a} hello {b}".title())
...       
Hello John Hello Henry
