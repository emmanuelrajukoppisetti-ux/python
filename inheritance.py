#inheritance
#Single inheritance
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        print('available cash is',cls.cash)
        print('available cash is',RBI.cash)
class SBI(RBI):#child cl6958+ass-1
    pass
class HDFC(RBI):
    cash=50000
    def new_cash(cls):
        print('new cash is',cls.cash+cls.cash)
        print('new cash is',cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''


'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        print('available cash is',cls.cash)
        print('available cash is',RBI.cash)
class SBI(RBI):#child class-1
    cash=25000
    def balance_cash(cls):
        print('balance cash is',cls.cash)
        print('balance cash is',RBI.cash-cls.cash)
     
class HDFC(RBI):#child class-2
    cash=50000
    def new_cash(cls):
        print('new cash is',cls.cash+cls.cash)
        print('new cash is',cls.cash+RBI.cash)
a=HDFC()
b=SBI()
a.available_cash()
a.new_cash()
b.balance_cash()'''


#Multiple inheritance
'''class father():
    weight='80kgs'
    def father_weight(fam):
        print('father weight is',fam.weight)
class mother():
    height='5.5 feet'
    def mother_height(fam):
        print('mother height is',fam.height)
class kid(father,mother):
    dob='28-09'
    def kid_dob(fam):
        print('kid dob is',fam.dob)
        print('family details',fam.weight,fam.height,fam.dob)
a=kid()
a.father_weight()
a.mother_height()
a.kid_dob()'''

#Multi-level inheritance
'''class GrandParent():
    acres=20
    def grandparent_acress(self):
        print('grand parent land ',self.acres)
class Parent(GrandParent):
    house='1 house'
    def parent_house(self):
        print('parent house',self.house)
class child(Parent):
    car='1 car'
    def child_car(self):
        print('child car',self.car)
a=child()
a.grandparent_acress()
a.parent_house
a.child_car()'''



#Task
'''class Dog1():
    def golden_retever(self):
        print('golden retever')
class Dog2(Dog1):
    def lab(self):
        print('lab')
class Dog3(Dog2):
    def husky(self):
        print('husky')
a=Dog3()
a.husky()
a.lab()
a.golden_retever()'''
        
#super()
'''1.the super function is used to give access to methods and properties of a parent or sibbling class
2. the super function represent the object the represent the parent class
3. in python super function is used to call methods from methods (super class)inside a class (sub class).
it allows to extend or overide inherit method while still reused the parent functionality 
'''

#super()
'''
4class parent():
    def __init__(self,name):
        self.name=name
        print('parent class constructor')
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print('child class constructior')
c=child('emmanuel',10)
print(c.name)
print(c.age)'''

#encapsulation
'''combine multiple units into singe unit is known it as a encapulation
1.public data
2._protected data
3.__private data'''

#PUBLIC DATA
'''class parent():
    publicdata=10
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2() '''

#_protected data
'''class parent():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)
print(obj1._protecteddata)'''


#__privatedata()
'''class parent():
    __privatedata="raju"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()'''

#abstraction
'''the process of handling complexcity by hidding unnessery information from user is called abstraction'''
#abstract class
'''if a class contain one or more than abstract methods then the class is called abstract class'''
#abstract method
'''if the method is declared with out implementation is called abstract method'''

#abstraction
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()'''

#abstract method
'''from abc import ABC,abstractmethod
class A():
    @abstractmethod
    def method1(self):
        print('python')
obj1=A()
obj1.method1()'''

#abstract class
'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print('python')
obj1=A()
obj1.method1()'''#error


'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''


'''......................................'''
'''class Instructor:
    def __init__(self,name,address):
        self.name=name
        self.address=address
instructor_1=Instructor("emmanuel","mandapeta")
print(instructor_1.name)'''


'''class Instructor:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self,subject):
        print(f"hi, I am {self.name} and I learn {subject}")
    
instructor_1=Instructor("emmanuel","mandapeta")
print(instructor_1.name)
instructor_1.display("Python")'''

'''class Circle():
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=Circle.pi*radius*radius
    def get_circumference(self):
        return 2*self.pi*self.radius
c=Circle(int(input("enter radius")))
print(f"circumference {c.get_circumference()}")
print(f"area {c.area}")'''

class Human():
    def __init__
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Male(Human):
    def swim(self):
        print("i can swim")
    def work(self):
        super().work()
        print("i can learn")
m=Male()
m.eat()
m.work()        






































