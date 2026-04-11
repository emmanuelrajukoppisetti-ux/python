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
