#oops syntax
'''class classname():
    name='codegnan'
    age=2018
    place='vij'
    def fname(method):
        print('statements......')
a=classname()
print(dir(a))
a.fname()'''

#class declaration
'''class Details():
    name='emmanuel'
    age='21'
    place='mandapeta'
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#object instantiation
'''class Details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data('naveen',23,'vij')
a.display()
b=Details()
b.Data('emmanuel',22,'mdp')
b.display()'''


'''class Details():
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(shelf):
        print(shelf.name,shelf.age,shelf.place)
a=Details()
print(dir(a))
a.Data('koshik',23,'vij')
a.display()
b=Details()
b.Data('emmanuel',22,'mdp')
b.display()'''


#object initialization
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def Display(self):
        print(self.name,self.age,self.place)
a=Details('sasi',22,'mdp')
a.Display()
b=Details('kevin',21,'rjy')
b.Display()'''

#task run time
#method 1
'''class Details():
    #creating a constructor
    def __init__(self):
        self.name=input('name')
        self.age=int(input('age'))
        self.place=input('place')
    def Display(self):
        print(self.name,self.age,self.place)
a=Details()
a.Display()'''

#method 2
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def Display(self):
        print(self.name,self.age,self.place)
a=Details(input('name'),int(input('age')),input('place'))
a.Display()'''


#difference b/w _ and __
''''_'we generaly use it for primary varables,that means whenever we use
'__'for a variable our python interpriter treats it as a special varable in
order to avoid main conflicts which methods in inner class '''

'''class Employee():
    def __init__(self):
        self.name='emmanuel'
        self._mailid='emmanuel@123gmail.com'
        self.__salary=10000 #private variable
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary) Error
print(a._Employee__salary)'''


#task
'''class Employee1():
    def __init__(self):
        self.name='emmanuel'
        self._mailid='emmanuel123@gmail.com'
        self.__salary=10000 #private variable
class Employee2():
    def __init__(self):
        self._name='raju'
        self.mailid='raju@gmail.com'
        self.__salary=20000
a=Employee1()
b=Employee2()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._Employee1__salary)
print(dir(b))
print(b._name)
print(b.mailid)
print(b._Employee2__salary)'''



































