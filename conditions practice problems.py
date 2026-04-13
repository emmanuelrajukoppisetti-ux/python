#check positive ,negative or zero
'''num=int(input('enter number'))
if num>0:
    print('positive')
elif num<0:
    print('negative')
else:
    print('zero')'''
    

#grade calculation
'''marks=int(input('enter marks'))
if marks>=90:
    print('grade A')
elif marks>=75:
    print('grade B')
elif marks>=50:
    print('grade C')
else:
    print('fail')'''


#ATM withdraw
'''balance=10000
withdraw=int(input('enter amount'))
if withdraw<=balance:
    print('transaction successful')
    balance=balance-withdraw
    print('remaining balance',balance)
else:
    print('insufficient balance')'''


#Loginsystem
'''username=input('enter username')
password=int(input('enter password'))

if username=='emmanuel':
    if password==9999:
        print('login succesfull')
    else:
        print('incorrect password')
else:
    print('invalid username')'''

#Driving licence eligibility
'''age=int(input('enter age'))
if age>=18:
    print('eligible for licence')
else:
    print('not eligible')'''

#scholarship Eligibility
'''marks=int(input('enter marks'))
income=int(input('enter family income'))

if marks>=70:
    if income<=200000:
        print('eligible for scholarship')
    else:
        print('income is high')
else:
    print('insufficient marks')'''


#movie tickets pricing

'''age=int(input('enter age'))

if age<=5:
    print('free ticket')
elif age<=18:
    print('child ticket -100/-')
elif age<=60:
    print('adult ticket -200/-')
else:
    print('senior citizen -150/-')'''

#check character type
'''ch=input('enter character')
if ch.isalpha():
    print('it is alphabet')
elif ch.isdigit():
    print('it is digit')
else:
    print('special character')'''


#simple calculator
'''a=int(input('enter a value'))
b=int(input('enter b value'))
op=input('enter options(+,-,*,/):')

if op== '+' :
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    if b!=0:
        print(a/b)
    else:
        print('division by zero is not allowed')
else:
    print('invalid operator')'''






#pratice
'''num=[1,2,3,4,2,3,4,5,6]
dup=[]
for i in num:
  if num.count(i)>1 and i not in dup:
    dup.append(i)
print(dup)'''

#for loop
#triangle*
'''for i in range(1,6):
    for j in range(i):
        print('*',end='')
    print()'''
#reverse triangle*
'''for i in range(5,0,-1):
    for j in range(i):
        print('*',end='')
    print()'''


#list comperhension
'''print([i for i in range(21) if i%2==0])'''

'''print([i for i in range(21) if i%2!=0])'''

'''print([pow(i,2) for i in range(21) if i%2==0])'''

'''print([pow(i,2) if i%2==0 else i*10 for i in range(21)])'''

#find largest element in list
'''l=[10,23,12,45,78,21,6,19]
largest=l[0]
for i in l:
    if i>largest:
        largest=i
print(largest)'''

#sum of elements in a list
'''l=[10,20,30,40,50]
total=0
for i in l:
    total=total+i
print(total)'''


#print keys and values
'''d={'a':10,'b':13,'c':16}
for k,v in d.items():
    print(k,v)'''

#FIZZBUZZ
num=int(input("enter number"))
for i in range(1,num+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)














































