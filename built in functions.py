#Built-in-functions

#fromkeys()
'''a="codegnan"
print(a)

print(list(a))
print(tuple(a))
print(set(a))

#print(dict(a))

b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"raju")
print(b)'''

#eval() means it accept any datatype in run time
'''while True:
    a=int(input('a value:'))
    b=int(input('b value:'))
    print(a+b)'''

'''while True:
    a=float(input('a value:'))
    b=float(input('b value:'))
    print(a+b)'''

'''while True:
    a=input('a value:')
    b=input('b value:')
    print(a+b)'''

'''while True:
    a=eval(input('a value:'))
    b=eval(input('b value:'))
    print(a+b)
    print(type(a+b))'''

#zip() -> we can combine mulitple collectioons into one collections
'''a=[10,20,30,40,50,60]
names=['emmanuel','kevin','sasi','pavan','vinod']
print(a+names)

c=zip(a,names)
print(c)

b=list(zip(a,names))
print(b)

b=tuple(zip(a,names))
print(b)

b=set(zip(a,names))
print(b)

b=dict(zip(a,names))
print(b)'''


#enumarate() we can give counter to the collection
'''names=['emmanuel','mahesh','naveen','hitesh','mohith']
for i in range(len(names)):
    print(i,names[i])

b=dict(enumerate(names,11))
print(b)
    
b=list(enumerate(names,21))
print(b)  

b=tuple(enumerate(names,31))
print(b)

b=set(enumerate(names,41))
print(b)'''


#ASCII american

'''for i in range(65,90+1):
    a=chr(i)
    print(a,end=' ')'''

'''for i in range(97,122+1):
    a=chr(i)
    print(a,end=' ')'''

'''a='emmanuel'
for i in range(len(a)):
    b=ord(a[i])
    print(b)'''

#another method
'''name=input('enter the name')
for i in name:
    print(i,'-',ord(i))'''

#Annonymous functions are name less functions we use a keyword called as lambda to create annoymous functions
#write a function to calcualate 2*x+5 where x=5
'''def cal(x):
    b=2*x+5
    print(b)
cal(5)'''

'''def cal():
    x=int(input('enter value'))
    print(2*x+5)
cal()'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input('enter value'))
b=lambda x:2*x+5
print(b(a))'''

#task 1
'''a=lambda x,y:x*y
print(a(5,6))'''


'''x=int(input('enter x value'))
y=int(input('enter y value'))
a=lambda x,y:x*y
print(a(x,y))'''

#task 2
#"python" o/p PYTHON
'''a=lambda x:x.upper()
print(a('python'))'''

'''a=input("data")
b=lambda a:a.upper()
print(b(a))'''


#task 3
'''fname=input('enter fname')
lname=input('enter lname')
a=lambda fname,lname:fname+lname
print(a(fname,lname))'''


'''a,b=[x for x in input('enter the value').split(",")]
c=lambda a,b:(a+' '+b).title()
print(c(a,b))'''


#[],(),{},set()
'''a=[]
print(type(a))
b=()
print(type(b))
c={}
print(type(c))
d=set()
print(type(d))'''


#filter()
#a=[2,5,6,7,23,45,66,78,96,100]
'''if a%2==0:
    print(a)'''#error

'''for i in a:
    if i%2==0:
        print(i,end=' ')'''

'''d=list(filter(lambda x:x%2==0,a))
print(d)'''

'''a=[[],(),{},set(),None,3,3.4,'python',6+4j,True,False]
b=list(filter(None,a))
print(b)'''

#map() ->each object from a collection and form a new collection
a=[10,5,23,45,66,7,22,89,100]
b=[8,10,3,455,34,29,90,1]
c=list(map(max,a,b))
print(c)

c=list(map(min,a,b))
print(c)











