#sys module
'''import sys
print(sys.path)


for i in sys.path:
    print(i)

print(sys.version)'''


#os module
'''import os'''
#print(os.path)

#print(os.getcwd())

#print(os.listdir())

#print("C:\\Users\\EMMANUEL\\OneDrive\\Desktop\\python codegnan")
#print(os.listdir())


#print(os.mkdir("april"))
#print(os.listdir())


#random module
'''
1.to generate random number in python,randint in function is used this function is used in random module
2.python defines a set of functions that are used to generate or manuplate random numders through the random module
'''
#sample
'''import random
a=random.sample(range(10,30),4)
print(a)'''

#randint()
'''import random
a=random.randint(40,60)
print(a)'''

#choice()
'''import random
a=[10.20,30,40,50,60,70]
b=random.choice(a)
print(b)'''

#Dice Code task
'''  
while True:
    import random
    dice=int(input("enter the roll of dice"))
    b=random.randint(1,7)
    print(b)
    option=input("enter YES or NO")
    if option=='yes':
        continue
    elif option=='no':
        print("exit")
        break
    else:
        print("invalid option")'''

#calendar
'''import calendar
year=2025
month=9
print(calendar.month(year,month))'''

'''import calendar
year=2026
print(calendar.calendar(year))'''
    
#task
'''import calendar
year=int(input("enter the year"))
month=int(input("enter the month"))
print(calendar.month(year,month))'''


'''import calendar
year=int(input("enter the year"))
print(calendar.calendar(year))'''


#date&time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

import time
a=time.time()
print(a)  #epoch time

b=time.localtime(a)
print(b)

print(f"Today time is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")


print(f"time {b.tm_hour}:{b.tm_min}:{b.tm_sec}")

print(f"day {b.tm_mday}:{b.tm_yday}:{b.tm_isdst}")





















