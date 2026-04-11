#Global and local variables
#first case of global variable
'''a=3
def check():
   print('inside value is',a)
check()
print('outside value is',a)'''

#second case of global variable
'''a=2
def check1():
    a=5
    a=a**2
    print('inside value is',a)
check1()
print('value of outside',a)'''


#third case of both global and local variables
'''a=4
b=3
def check2():
    a=7
    print('inside value is',a)
    a=10
    print('update value is',a+5)
    b=12#local variable
    b=b+a
    print('value of b is',b)
check2()
print('a value is',a)
print('b value is',b)'''



#usage of global keyword
'''a=5
def final():
    global a,b
    print('inside value is',a)
    a=10
    print('updated value is',a)
    #global b
    b=15
    b=b+a
    print('value of b is ',b)
final()
print('a value is ',a)
print('b value is',b)'''


#generators
#a=[expr for var in collection/range]
'''a=[i for i in range(21)]
print(a)
print(type(a))'''


'''a=(i for i in range(16))
print(*a)
print(type(a))'''


'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
print(set(a))'''

'''a,b=[int(x) for x in input('enter the value')
     .split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''


'''a,b=[int(x) for x in input('enter the value')
     .split(",")]
def check(a,b):
    while a<b:
        a=a+1
         return a
    #return a
print(check(a,b))'''

#yield v/s return
'''def mygen():
    #return "python"
    #return "dsa"
    #return "java"
    return "python","java","dsa"
print(*mygen())'''


'''def mygen():
    yield "vij"
    yield "hyd"
    yield "viz"
print(*mygen())
#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))'''


#example program of global and local variable
'''balance = 1000   # Global variable

def deposit(amount):
    global balance
    balance += amount   # updating global balance
    print("Deposited:", amount)
    print("balance",balance)
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient balance")

deposit(500)
withdraw(300)
print("Final Balance:", balance)'''










































