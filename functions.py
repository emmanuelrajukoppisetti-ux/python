#Functions

'''a=10
b=20
print('the sum is',a+b)
print('the diff is',a-b)
print('the product is',a*b)
a=100
b=200
print('the sum is',a+b)
print('the diff is',a-b)
print('the product is',a*b)
a=1000

b=2000
print('the sum is',a+b)
print('the diff is',a-b)
print('the product is',a*b)'''

#using functions
'''def calculator(a,b):
    print('the sum is',a+b)
    print('the diff is',a-b)
    print('the product is',a*b)
calculator(10,20)
calculator(100,200)
calculator(1000,2000)'''


'''def calculator(a,b):
    print('the power is',a**b)
    print('the modules is',a%b)
    print('the integer division is',a//b)
calculator(4,6)
calculator(20,10)'''

'''def add(a,b):
    print(a+b)
add(11,32)'''

'''def add():
    a=int(input('enter a value'))
    b=int(input('enter b value'))
    print(a+b)
add()'''

'''
def fullname():
    fname=input('enter first name')
    lname=input('enter last name')
    print(fname+lname)
fullname()'''

#print v/s return
'''def mul(a,b):
    print(a*b)
mul(2,3)'''


'''def mul(a,b):
    return(a*b)
print(mul(2,3)))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(3,5)'''


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return(c)
    #return(d)
    #return(e)
    return c,d,e
print(cal(3,5))'''

#calculartor using options
'''
while True:
    def cal():
        a=int(input('enter a value'))
        b=int(input('enter b value'))
        option=int(input('enter options\n1.add\n2.sub\n3.mul\n'))
        if option==1:
            print(a+b)
        elif option==2:  
            print(a-b)
        elif option==3:
            print(a*b)
        else:
            print('invalid option')
    cal()'''

#another method cal
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input('enter a value'))
    b=int(input('enter b value'))
    option=int(input('enter options\n1.add\n2.sub\n3.mul\n'))

    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()
    else:
         print('invalid option')'''


#Task
'''def bill():
    a=int(input('enter bill amount: '))
    b=int(input('number of members: '))
    print("split the bill per head is: {}".format(a/b))
bill()'''


'''def bill():
    a=int(input('enter bill amount: '))
    b=int(input('number of members: '))
    print("split the bill",a/b)
bill()'''


'''def bill():
    a=int(input('enter bill amount: '))
    b=int(input('number of members: '))
    print(f"split the bill {a/b}")
bill()'''


#PRACTICE
#1
'''def greet(name):
    print('hello',name)
greet('emmanuel')'''
#2
'''def sum(a,b):
    return a+b
print(sum(23,28))'''
#3
'''def student(name,age):
    print('name:',name)
    print('age:',age)
student('raju',21)'''
#4
'''def greet(name='emmanuel'):
    print('hello',name)
greet()
greet('raju')'''
#5 LOGIN SYSTEM
'''
while True:
    def login():
        username=input('enter username:')
        password=int(input('enter password:'))
        if username=="emmanuel" and password==1234:
            print('login successful')
        else:
            print('invalid password')
    login()'''
#6 student result system
'''
while True:
    def check_result():
        marks=int(input('enter marks:'))
        if marks>=90:
            print('grade A')
        elif marks >=75:
            print('grade B')
        elif marks>=50:
            print('grade C')
        elif marks<50:
            print('fail')
    check_result()'''

#PALINDROME

'''while True:
    def palindrome():    
        num=input('enter number')
        if num==num[::-1]:
            print('palindrome')
        else:
            print('not palindrom')
    palindrome()'''

def great(name):
    print("hellow",name)
great("emmanuel") 































