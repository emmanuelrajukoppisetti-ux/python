#if-else conditions by using comparision oprerator
'''a=6
b=8
if a<b:
    print('less')'''


'''a=6
b=8
if a>b:
    print('less')
else:
    print('true')'''


'''a=6
b=8
if a<b:
    print('less')
else:
    print('false')'''


'''a=3
b=9
if a!=b:
    print('not equal')
else:
    print('equal')'''


'''a=3
b=9
if a==b:
    print('not equal')
else:
    print('equal')'''

 
'''a=int(input())
b=int(input())
if a>b:
    print('greater')
else:
    print('true')'''

 
#if-elsencondition by using logical operators
'''a=6
b=12
if a<b and b>a:
     print('true')
else:
    print('false')'''
    

'''a=3
b=7
if a!=b or a==b:
    print('equal')
else:
    print('false')'''

'''a=9
b=10
if not b>a:
    print('false')
else:
    print('true')'''


#if-else conditions by using identify operator
'''a=[9,8,7,6,5]
b=5
if a is b:
    print('true')
else:
    print('not')'''


'''a='emmanuel'
b=5
if a is not b:
    print('true')
else:
    print('false')'''

'''a=int(input('enter any number:'))
if type(a)is float:
    print('true')
else:
    print('false')'''

#if-else condition by using membership operator
'''a=[4,5,6,7,8,9,10]
b=int(input('a value'))
if b in a:
    print('the value is',b)
else:
    print('false')'''

'''a=[4,5,6,7,8,9,10]
b=int(input('a value'))
if b not in a:
    print('the value is',b)
else:
    print('false')'''

#if-elif-else
'''a=8
b=20
if a<b:
    print('less')
elif b>a:
    print('greater')
else:
    print('equal')'''

'''a=8
b=20
if a>b:
    print('less')
elif b>a:
    print('greater')
else:
    print('true')'''

'''a=8
b=20
if a==b:
    print('less')
elif b<a:
    print('greater')
else:
    print('true')'''


'''a=8
b=20
if a==b:
    print('less')
elif b<a:
    print('greater')
elif a<b:
    print('false')
else:
    print('true')'''

#if-elif-else using logical
'''a=10
b=20
if a<b and a>b:
    print('b is small')
elif a<b or a>b:
    print('a is small')
elif  not a==b: 
    print('both are not equal')
else:
    print('equal')'''

#membership
'''a=[1,2,3,4,5,6,7]
b=20
if b in a:
    print('b value is in a')
elif b not in a:
    print('b is not in a')
else:
    print('no number')'''

#identify

'''a=input('enter any number:')
if type(a)is float:
    print('float')
elif type(a) is int:
    print('integer')
else:
    print('not a number')'''


#multiple if-conditionds
'''a=5
b=10
if a<b:
    print('less')
if b>a:
    print('greater')
if a!=b:
    print('not equal')'''


'''a=5
b=10
if a<b:
    print('less')
elif b>a:
    print('greater')
elif a!=b:
    print('not equal')'''

'''a=5
b=10
if a==b:
    print('less')
if b>a:
    print('greater')
if a!=b:
    print('not equal')'''


'''a=5
b=10
if a<b:
    print('less')
if b>a:
    print('greater')
if a==b:
    print('not equal')
elif a!=b:
    print('true')'''


#multiple if-condition using logical operator
'''a=3
b=6
if a<b and b>a:
    print('true')
if a!=b or a==b:
    print('false')
if not a<=b:
    print('less')'''

#multiple if-condition using identify operator
'''a=6
if type(a) is int:
    print('it is integer')
if type(a) is not float:
    print('true')'''

#multiple if-conditon using membership operator
'''a=[2,3,4,5,6,7,8,9,10]
if 3 in a:
    print('true')
if 10 not in a:
    print('false')'''


#Nested-if condition
'''a=10
b=20
if a<b:
    print('less')
    if b>a:
        print('greater')'''

'''a=10
b=20
if a==b:
    print('less')
    if b>a:
        print('greater')'''

'''a=10
b=20
if a==b:
    print('less')
if b>a:
    print('greater')'''

        
'''a=10
b=20
if a<=b:
    print('less')
    if b==a:
        print('greater')
    else:
        print('true')'''
        
    
'''a=10
b=20
if a==b:
    print('less')
    if b==a:
        print('greater')
else:
    print('true')'''

'''a=10
b=20
if a<=b:
    print('less')
    if b==a:
        print('greater')
    else:
        print('true')
else:
    print('false')'''


'''a=10
b=20
if a<=b:
    print('less')
    if b==a:
        print('greater')
    elif a==b:
        print('not equal')
    else:
        print('false')'''


'''num=int(input("enter a number"))
if num>=0:
    if num%2==0:
        print("positive even")
    else:
        print("positive odd")
else:
    print("negative")'''
