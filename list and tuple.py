Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list[]
a=[3,3.5,"raju",3+5j,True,False]
print(a)
[3, 3.5, 'raju', (3+5j), True, False]
type(a)
<class 'list'>
#append
a=["python","java","c","c++"]a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
#extend
a.extend('html','css')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.extend('html','css')
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(['html','css'])
a
['python', 'java', 'c', 'c++', ['ml', 'ai'], 'html', 'css']
#insert()
a=["bike","car","lorry","train"]
a.insert(1,"bus")
a
['bike', 'bus', 'car', 'lorry', 'train']
a.insert("aeroplain",2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.insert("aeroplain",2)
TypeError: 'str' object cannot be interpreted as an integer
#index and copy
a=['red','black','blue','green']
b=a.copy()
b
['red', 'black', 'blue', 'green']
b.index('blue')
2
a=['briyani','icecream','chocalates']
a.sort()
a
['briyani', 'chocalates', 'icecream']
b=[3,5,1,0,6,8,9]
b.sort()
b
[0, 1, 3, 5, 6, 8, 9]
a=[2,3,5,'hi','bye',8]
a.sort()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
b=[-8,-5,-28,-5,0,-1,-44,-13]
b.sort()
b
[-44, -28, -13, -8, -5, -5, -1, 0]
#reverse
x=['raju','emmanuel','python','course']
x.reverse()
x
['course', 'python', 'emmanuel', 'raju']
y=[9,5,6,4,3,2,1]
y.reverse()
y
[1, 2, 3, 4, 6, 5, 9]
#pop()
a=['html','css','js']
a.pop()
'js'
a
['html', 'css']
a.pop('css')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.pop('css')
TypeError: 'str' object cannot be interpreted as an integer
a.pop(0)
'html'
a
['css']
#remove()
a=['hi','emmanuel','you','are','deleted']
a.remove('hi')
a
['emmanuel', 'you', 'are', 'deleted']
#len
a='code'
len(a)
4
b=['code']
len(b)
1
c=['emmanuel','raju']
len(c)
2
#count
a=['sun','moon','sky','star']
a.count('sky')
1
#clear()
a=['water','drink']
a.clear()
a
[]
a.append("juice")
a
['juice']
#task
a=[9,1,5,2,8,4,6,3,7,0]
#op [7,6,4,3,0,9,8,5,2,1]
b=[9,1,5,2,8]
b.sort()
b
[1, 2, 5, 8, 9]
b.reverse()
b
[9, 8, 5, 2, 1]
c=[4,6,3,7,0]
c.sort()
c
[0, 3, 4, 6, 7]
c.reverse()
>>> c
[7, 6, 4, 3, 0]
>>> print(c+b)
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> #task
>>> 
>>> #tuple is imuatable
>>> a=(1,2.3,'raju',3+5j,True,False)
>>> print(a)
(1, 2.3, 'raju', (3+5j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index(True)
0
>>> a.index('True')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.index('True')
ValueError: tuple.index(x): x not in tuple
>>> a.index(2.3)
1
>>> a.len()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.len()
AttributeError: 'tuple' object has no attribute 'len'
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.count()
TypeError: tuple.count() takes exactly one argument (0 given)




























