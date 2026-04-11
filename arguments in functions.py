
 #keyword and positionl arguments
'''def Details(id,name,mailid):
    id=10
    name='emmanuel'
    mailid='emmanuel@gmail.com'
    print(id,name,mailid)
Details(id='id',name='name',mailid='mailid')'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id='id',name='name',mailid='mailid')
Details(id=20,name='kevin',mailid='k@gmail.com')
Details(id=30,name='sasi',mailid='s@gmail.com')
Details(40,'pavan','p@gmail.com')
Details('vinod','v@gmail.com',50)
Details(name='chaithu',mailid='c@gmail.com',id=60)'''

'''def Grocery(item,price):
    print('item is %s' %item)
    print('price is %f' %price)
Grocery('sugar',100)'''


'''def Grocery(item='rice',price=1500):
    print('item is %s' %item)
    print('price is %f' %price)
Grocery()'''


'''def Grocery(item,price=200):
    print('item is %s' %item)
    print('price is %f' %price)
Grocery('dal')'''

'''def Grocery(item='ghee',price):
    #non-def arg follows def arg(error)
    print('item is %s' %item)    
    print('price is %f' %price)
Grocery(400)'''#error

#task
#cake name,qty,price
'''def bakery(cakename,qty,price):
    print('cakename is %s' %cakename)
    print('qty is %s' %qty)
    print('price is %d' %price)
bakery('chocalate','2kg',1000)'''


'''def bakery(cakename='venala',qty='2kg',price=800):
    print('cakename is %s' %cakename)
    print('qty is %s' %qty)
    print('price is %d' %price)
bakery()'''


'''def bakery(cakename,qty='2kg',price=800):
    print('cakename is %s' %cakename)
    print('qty is %s' %qty)
    print('price is %d' %price)
bakery('chocalate')'''

'''def bakery(cakename='chocalate',qty='2kg',price):
    print('cakename is %s' %cakename)
    print('qty is %s' %qty)
    print('price is %d' %price)
bakery(800)'''#error

#arguments-> * is used to unpack the elements
'''a=[2,3,4,5,6,7,8,9]
print(a)
print(*a)'''

'''b=(2,3,4,5,6,7,8,9)
print(b)
print(*b)
print(type(b))'''


'''c={2,3,4,5,6,7,8,9}
print(c)
print(*c)
print(type(c))'''


'''d={'year':2026,'month':3}
print(d)
print(*d)
print(type(d))'''

'''a,b,c=2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)'''#error


'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8,9
print(a)
print(*b)
print(c)'''


'''a='codegnan'
print(a)
print(*a)'''


a,b,c='cod'
print(a)
print(b)
print(c)

'''sssa,*b,c='codegnan'
print(a)
print(*b)
print(c)'''


#varable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
d=[5,6,7,8,9,10]
check(d)
check(*d)
e={3,4,5,6,7,8}
check(*e)
f={'name':'emmanuel','city':'viy'}
check(f)
check(*f)'''

'''def check1(*a):
    d=2 #creating a varible
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
        #if type(i)==int or type(i)==float:
            d=d+i
            print(d)    
check1()
check1(2,3,4,5,6)
check1(2,3,4,3.5,6.2,4.3)
check1(1,3,5,6.2,3.2,'pooja',3+4j,True,False)'''


#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={'idnos':[10,20,30],
   'names':['naveen','raju','jaswanth'],
   'status':['p','f','p']}
details(**d)'''


'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={'idnos':[10,20,30],
   'names':['naveen','raju','jaswanth'],
   'status':['p','f','p']}
details(**d)'''


#both * and ** usage
'''def final(*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print('keys is',i)
        print('values is',j)
final()
data=(2,3,4,5.6,4.7,8.9)
final(*data)
details={'names':['sasi','kasi','pavan'],
       'marks':[50,80,70]}
final(**details)
final(*data,**details)'''


#max,min,sum
'''print(max(1,2,3,4,5,30))'''

'''print(min(2,1,3,4,5,6,7))'''

#print(sum(2,4)) error
'''a=2,3,4,5,6,7,8
print(sum(a))'''

#print(sum([2,3,4,5,6,7]))


#practice(varable-length argument,kwargs)
'''def total(*args):
    sum=0
    for i in args:
        sum+=i
        print(sum)
total(2,3,4,5,6,7,8)'''


'''def students(**kwargs):
    print(kwargs)
students()
students(name=['raju','emmanuel','sssvms'],
         age=[21,20,22],city=['vij','rjy','rcpm'])'''


#task
'''def markyoat():
    a=int(input("Numbe of students:"))
    l=[]
    i=1
    countp=0
    counta=0
    while i<=a:
        s=input(f"Student{i}(P/A)").upper() 
        l.append(s)
        i+=1
    for i in l:
        if i=="A":
            counta +=1
        elif i=="P":
            countp+=1
    print("Total no.of students:",len(l))
    print("Presentees:",countp)
    print("Absentees:",counta)

markyoat()'''
        

'''def attendance():
    num=int(input('enter no. of students'))
    l=[]
    i=1
    counta=0
    countp=0
    while i<=num:
        a=input(f'student{i}(A/P)')
        l.append(a)
        i+=1
    for i in l:
        if i=='a':
            counta+=1
        elif i=='p':
            countp+=1
    print('total no of students:',len(l))
    print('no. of students present:',countp)
    print('no. of students absent:',counta)
        
        
attendance()  '''          













