

#loops
#for(),while(),range(),break,continue,pass
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''
    
'''a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''
    
'''a=(10,20,30,40,50)
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={2,3,4,5,6,7,8}
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={'name':'emmanuel','year':2026,'month':3}
for i in a:
    print(i)
for i in a.keys():
    print(i)   
    print(type(a))
    print(type(i))
for i in a.values():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

'''a='codegnan'
for i in  a:
    print(i,end=" ")
    print(type(a))
    print(type(i))'''


a=['code','python','course']
#print(a.upper())

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=" ")'''


#WHILE LOOP(contineous iteration)
'''a=10
while a>1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''


'''a=10
while a>=1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    a=a-1
    print(a)'''

'''a=20
while a>1:
    a=a-1
print(a)'''

'''a=15
while a>2:
    print(a)
    a+=1'''
'''a=3
while a<18:
    print(a)
    a-=1'''

#tasks while
#voting
'''while True:
    age=int(input('Enter the age'))
    if age>=18 :
        print('eligible for vote')
    else:
        print('not eligible for vote')'''

#even or odd
'''while True:
    num=int(input('enter a numder'))
    if num%2==0 :
        print('it is even')
    else:
        print('it is odd')'''

#Range()
#start-stop-step
'''for i in range(10):
    print(i)'''

'''for i in range(5,15):
    print(i)'''
    

#tasks
'''for i in range(1,50,5):
    print(i,end=',')'''

'''for i in range(2,20,2):
    print(i,end=',')'''
    
'''for i in range(3,30,3):
    print(i,end=',')'''


'''while True:
    marks=int(input('enter marks'))
    if marks in range(91,101):
        print('grade A')
    elif marks in range(81,91):
        print('grade B')
    elif marks in range(71,81):
        print('grade C')
    elif marks in range(50,71):
        print('grade D')
    else:
        print('fail')'''


#break
'''a=10
while a<1:
    print(a)'''

'''a=10
while a>1:
    print(a)'''


'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)'''

'''for i in range(20):
    print(i)'''


'''for i in range(20):
    if i==11:
        break
    print(i)'''

'''a='python'
for i in a:
    if i=='o':
        continue
    print(i)'''


#continue
'''a=30
while a>5:
    print(a)
    a=a-1'''

'''a=30
while a>5:
    a=a-1
    print(a)'''
    
'''a=30
while a>5:
    a=a-1
    print(a)
    if a==15:
        continue'''

'''a=30  
while a>5:
    a=a-1
    if a==15:
        continue
    print(a)'''

'''for i in range(25):
    print(i)'''
   
'''for i in range(25):
    if i==20:
        continue
    print(i)'''

'''a='course'
for i in a:
    if i=='s':
        continue
    print(i)'''


#pass
'''a=30
while a>20:
    print(a)
    a=a-1'''

'''a=30
while a>20:
    print(a)
    a=a-1
    if a==15:
        pass'''

'''for i in range(8):
    if i==4:
        pass
    print(i)'''


#tasks on loops 

#table
'''a=int(input('enter number'))
for i in range(1,21):
    print(f'{a}*{i}={a*i}')'''

#task student profil
'''print('student details')
name=input('name:')
mobile_no=int(input('mobile:'))
email=input('email:')
collage=input('collage:')
branch=input('branch:')
print(f'name is :{name}\nmobile no is :{mobile_no}\nemail is :{email}\ncollage name is :{collage}\nbranch is:{branch}')
'''


#marks analyser
'''n=int(input('enter student count'))
marks=[]
for i in range(n):
    list=int(input('enter marks'))
    marks.append(list)

for j in marks:
    print(j)
high_marks=max(marks)
lowest_marks=min(marks)
total_marks=sum(marks)
average=total_marks/n
print('high_marks',high_marks)
print('lowest_marks',lowest_marks)
print('total_marks',total_marks)
print('average',average)'''


#tables
'''table=int(input('enter table number'))
for i in range(1,21):
    print(f'{table}x{i}={table*i}')'''


#hostal fee+course fee
'''hostal_fee=int(input('enter hostal fee:'))
course_fee=int(input('enter course fee:'))
print(f'hostal fee :{hostal_fee}\ncourse fee:{course_fee}')
print(f'total={hostal_fee+course_fee}')'''




#triangle stars
'''a=int(input('enter number'))
for i in range(1,a+1):
    print('*'*i)'''

#triangle star in reverse
'''a=int(input('enter number'))
for i in range(a,0,-1):
    print('*'*i)'''


#factorial
'''a=int(input('enter number'))
fact=1

for i in range(1,a+1):
    fact*=i
print(fact)'''

#sum of even numbers
'''a=int(input('enter number'))
sum=0
for i in range(1,a+1):
    if i%2==0:
        sum+=i
        print(sum)'''


#count of numbers
'''a=int(input('enter a number'))
count=0
for i in range(1,a+1):
    count=count+1
    print(count)'''


#reverse numbers

'''a=int(input('enter number'))
for i in range(a,0,-1):
    print(i,end=",")'''


#repeating numbers
'''a=int(input('enter number'))

for i in range(1,a+1):
    print(str(i)*i)'''
'''o/p
1
22
333'''


#prime number check
'''a=int(input('enter number'))
count=0

for i in range(1,a+1):
    if a%i==0:
        count+=1
if count==2:
    print('prime')
else:
    print('not prime')'''
    

#tasks on loops 

#table
'''a=int(input('enter number'))
for i in range(1,21):
    print(f'{a}*{i}={a*i}')'''

#nested for loop
'''for i in range(1,4):
    print('Day',i,':',end='')
    for j in range(1,4):
        print('hour',j,end='')
    print()'''





    
