
# python & c++ will work without oops
# java needed oops

# oops mainly used in java 
# rarely used in python and C++


# Inheritance: 

#  Inheritance allows a class (child or subclass) to inherit the properties and behaviors (methods and attributes)
# of another class (parent or superclass).. It helps in code reuse and establishing a relationship between classes.


#  class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#     def move(self):
#         print(f"{self.brand} is moving at {self.speed} mph")
# class Car(Vehicle):
#     def __init__(self, brand, speed, wheels):
#         super().__init__(brand, speed)
#         self.wheels = wheels
# my_car = Car("Toyota", 80, 4)
# my_car.move()  # Output: Toyota is moving at 80 mph



# Abstraction

# Definition: Abstraction hides the complex implementation details and shows only the essential functionalities
# of an object or system. It provides a simple interface for the user to interact with the object.
# EX--we want to complete the final year project ,how it works we don't no

# Abstraction is the process of hiding the implementation details and showing only 
# the functionality to the user. It involves creating simple interfaces that represent complex 
# underlying code, allowing the programmer to focus on interaction at a high level without needing
# to understand all the details.

# from abc import ABC, abstractmethod
# class mobile(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
# my_dog = Dog()
# print(my_dog.sound())  # Output: Bark



# Encapsulation: Encapsulation is the bundling of data (attributes) and methods (functions) 
# that operate on that data within a single class. 
# It restricts direct access to some of the object's components, providing controlled access through methods.
# It is used to restrict access to methods and variables.

# (class,methods,attributes)protect the data or hide the data ex:WATER BOTTLE(inside the water is protected)

# public(Access all file)  , Private(access only file)  , Protected (access folder) Ex tablate


# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # private variable
    
#     def deposit(self, amount):
#         self.__balance += amount
    
#     def get_balance(self):
#         return self.__balance


# Polymorphism:
# two words "poly" and "morphs". Poly means many, and morph means shape.

# Polymorphism allows different classes to respond to the same method call in different ways
# One person have many faces,home,college,friends

# Polymorphism means "many forms." In OOP, it allows objects of different classes to be treated as 
# objects of a common superclass. It also allows methods to be overridden 
# or have multiple forms (like method overloading or method overriding).u
# different forms in same method  or function or class

#overloading:
# In a two class have a same methods in the same class but different parameters 

# def add(a, b=0, c=0):
#     return a + b + c
# print(add(2))        # Outputs 2
# print(add(2, 3))     # Outputs 5
# print(add(2, 3, 4))  # Outputs 9


# overriding:
# In class A and B have a same method  with the same parameters is called overriding

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):  # This method overrides Animal's speak()
#         print("Dog barks")
# d = Dog()
# d.speak()  # Outputs: "Dog barks"







# Inheritence


# 1. Single Inheritance

# Description: In single inheritance, a subclass inherits from a single superclass. 
# This is the most basic form of inheritance.

# class Animal:
#     def eat(self):
#         print("Eating...")

# class Dog(Animal):
#     def bark(self):
#         print("Barking...")

# d = Dog()
# d.eat()  # Inherited from Animal
# d.bark()  # Defined in Dog



# 2. Multiple Inheritance

# Description: In multiple inheritance, a subclass can inherit from more than one superclass. 
# This allows the subclass to combine the behavior and attributes of multiple parent classes.

# class Engine:
#     def start(self):
#         print("Engine started")

# class Body:
#     def protect(self):
#         print("Body protected")

# class Car(Engine, Body):
#     pass

# c = Car()
# c.start()    # Inherited from Engine
# c.protect()  # Inherited from Body




# 3 .Multilevel Inheritance

# Description: In multilevel inheritance, a subclass is derived from a class which is also a derived class. 
# In other words, there is a chain of inheritance.

# class Animal:
#     def eat(self):
#         print("Eating...")

# class Mammal(Animal):
#     def walk(self):
#         print("Walking...")

# class Dog(Mammal):
#     def bark(self):
#         print("Barking...")

# d = Dog()
# d.eat()   # Inherited from Animal
# d.walk()  # Inherited from Mammal
# d.bark()  # Defined in Dog



# 4 . Hierarchical Inheritance
# Description: In hierarchical inheritance, multiple subclasses inherit from a single superclass.
# This is useful for modeling different types of objects that share some common behavior.

# class Animal:
#     def eat(self):
#         print("Eating...")

# class Dog(Animal):
#     def bark(self):
#         print("Barking...")

# class Cat(Animal):
#     def meow(self):
#         print("Meowing...")

# d = Dog()
# d.eat()  # Inherited from Animal
# d.bark()  # Defined in Dog

# c = Cat()
# c.eat()  # Inherited from Animal
# c.meow()  # Defined in Cat





# 5. Hybrid Inheritance

# Description: Hybrid inheritance is a combination of two or more types of inheritance. 
# It is a complex form of inheritance and typically involves multiple inheritance and multilevel inheritance.

# class Animal:
#     def eat(self):
#         print("Eating...")

# class Mammal(Animal):
#     def walk(self):
#         print("Walking...")

# class Bird(Animal):
#     def fly(self):
#         print("Flying...")

# class Bat(Mammal, Bird):
#     def sleep(self):
#         print("Sleeping...")

# b = Bat()
# b.eat()   # Inherited from Animal
# b.walk()  # Inherited from Mammal
# b.fly()   # Inherited from Bird
# b.sleep() # Defined in Bat








# oops(Object Oriented Programming)

# # constructor is a init function
# # method 
# # variable

# global=declared outside the function

# # This function uses global variable s

# # a=10
# def f():
#     print("Inside Function", s)
# # Global scope
# s = "I love Geeksforgeeks"
# f()
# print("Outside Function", s)


# Local=declared inside the function

# def f():
#     # local variable
#     # a=10
#     s = "I love Geeksforgeeks"
#     print("Inside Function:", s)
# # Driver code
# f()


# no=int(input("Enter the no :"))
# if no%2==0:
#     print("even")
# else:
#     print("odd")
# print(no)


# # Recursive
# recursion is to break a problem down into smaller,
# function call itself is recursive 



# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *=i
#     return result
# n=5
# print(factorial(n))



# factorial(n)=n*(n-1)*(n-2)...
# factorial(n)=n*factorial(n-1)

# import sys
# print(sys.getrecursionlimit())
# def dffs():
#    print("Inside Function")
#    dffs()

# import sys
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
# i=0
# def dffs():
#    global i
#    i+=1
#    print("Inside Function",i)
#    dffs()
# dffs()







# Lambda / Anonymous Function
# Nameless function is ANONYMOUS
# Reduce the lines of code 
# we don't need a function ,if we have a lambda


# s=lambda n:n*n                        #  n is argument
# print("The square of 4 is ",s(4))
# print(4*4)


# s=lambda a,b,c : a if a>b and a>c else b  if  b>c else c
# print("Biggest of three i : ",s(10,20,30))

# x = lambda a : a + 10
# print(x(5))

# l=[0,5,10,15,20,25,30]
# e=list(filter(lambda n:n%2==0,l))         # Filter function to check inside the function             
# o=list(filter(lambda n:n%2!=0,l))          # filter is like a inbuilt function like modules etc 
# print(e)
# print(o)

# t=('a','AA','AAA','AAAAA','khhbvyk')
# output=tuple(filter(lambda s:len(s)>=3,t))
# print(output) 


# class Employee:
#     def __init__(self,name,sal,age,has_gt):
#         self.name=name
#         self.sal=sal
#         self.age=age
#         self.has_gt=has_gt
#     def display(self):
#         return (self.name)
 
# e1=Employee('kavin',50000,23,True)
# e2=Employee('nivi',5000,25,True)
# e3=Employee('pravin',11000,45,True)
# e4=Employee('nithish',500,42,True)
# e5=Employee('nivash',12000,80,True)

# l=[e1,e2,e3,e4,e5]
# output=filter(lambda s:s.sal>10000 and s.age>21 and s.has_gt,l)

# for x in output:
#     # x.display()
#     print(x.name)


# # Map () Function
# it will use to double the numbers

# l=[2,3,4,5,6,]
# output=list(map(lambda e:e*e,l))
# print(output)
# for i in output:
#    print(i)


# class Employee:
#     def __init__(self,name,sal,age,has_gt):
#         self.name=name
#         self.sal=sal
#         self.age=age
#         self.has_gt=has_gt

#     def display(self):
#         return (self.name)
 
# e1=Employee('kavin',50000,23,True)
# e2=Employee('nivi',5000,25,True)
# e3=Employee('pravin',11000,45,True)
# e4=Employee('nithish',500,42,True)
# e5=Employee('nivash',12000,80,True)

# l=[e1,e2,e3,e4,e5]
# output=map(lambda s:Employee(s.name,s.sal+10000,s.age,s.has_gt),l)
# for s in output:
#     print(s.name,'.........',s.sal)


# l1=[1,2,3,4,]
# l2=[10,20,30,40,50,60]
# output=list(map(lambda x,y:x*y,l1,l2))
# print(output)


# Reduce 
# it as import function
# it will reduce the numbers like we can add all the numbers in the list


# from functools import*
# l=[10,20,30,40,50,60]                 # Reduce function will add one by one
# result=reduce(lambda x,y:x+y,l)
# print(result)


# from functools import*
# l1=[10,20,30,40]
# result=reduce(lambda x,y:x*y,l1)
# print(result)


# from functools import*
# result=reduce(lambda x,y:x+y,range(1,101))
# print(result)



# from functools import*
# def multiple(x,y):
#     return x*y
# result=reduce(multiple,range(1,4))
# print(result)



# # Module Alising
# # Create a new file and import the file

# x=2123
# name='kavin'
# def add(a,b):
#     print('The sum is:',a+b)

# def Product(a,b):
#     print("The product is :",a*b)   

# import basic           #  * it will run all the variable ,function, class        
# print(basic.x)
# print(basic.name)
# basic.add(10,20)
# basic.prduct(100,200)


# import durga as dm
# print(dm.x)
# print(dm.name)
# dm.add(10,20)
# dm.prduct(100,200)
# once we use alias name , we can't use original name 

# module naming conflict

# # Create a new file1 
# x=20
# def Add(a,b):
#     print("Module 2")
#     print("The value is:",a+b)
# # Create a new file2
# y=20
# def Add(a,b):
#     print("Module 1")
#     print("The value is:",a+b)

# import basic
# import kavin
# add(10,20)

# 1way
# import module1
# import module2
# module1.add(10,20)
# module2.add(10,20)
 
 
# 2way
# import module1,module2,module3
# from module1 import add as a1
# from module2 import add as a2
# a1(10,20)
# a2(10,20)


# Reloading of module
# If u import the module in my times , The Ans is same

# reload module

# imp module want to use    
# If the file is running and sleep for some socond that time if we change the values 
# use imp.reload for update process


# dir()  -- TO list out number of current module
# Finding member of module by using dir() function

# dir()  just to list out member of current module

# def add(a,b):
#     print('The sum is:',a+b)

# def Product(a,b):
#     print("The product is :",a*b)
# print(dir())

# print(__annotations__)
# print(__builtins__)
# print(__cached__)
# print(__doc__)
# print(__file__)
# print(__loader__)
# print(__name__)
# print(__package__)
# print(__spec__)


# Help will give detailed information

# import math
# help(math)


# __doc__

# The variable holds documentation string

# "File handling is an important part of any web application"
# "Python has several functions for creating, reading, updating, and deleting files."
# print(__doc__)           #  It will print first line , other will ignore           

# import math
# print(math.__doc__)
# import random
# print(random.__doc__)


# # __file__
# import os
# print('file.name',__file__)
# print('Absolute path:',os.path.abspath(__file__))         # abspath means obsolute path of the file 


# __name__       We can find the direct or indirect execution
# print(__name__)
# py module1.py    == Direct execution of module
# py test.py       == IN this module inside test file import  means,Indirect execution

# __name__  ===__main__   (DE)
         #   === import module1  (IE)

# if __name__=='__main__':
#     print("durga is direct execution")

# else:
#     print("basic is indirect execution")
# # inside indirect use import for bacic file 



# Working of Random Module

# Random Password 
# OTP
# Developing Games



# Random()
# Uniform()
# randint
# Randrange()
# choice


# 1 Random
# generate some float value between 0 and 1 
# 0.999, 0.123

# from random import *
# for i in range (10):
#     print(random())                     #  All random value is different 


# 2 Uniform
# generate some float value between two given numbers
# uniform(1,10)

# from random import *
# for i in range (10):
#     print(uniform(1,10))                     # In All random value is different 


# 3 randint()
# # to generate integer between two given numbers(1,10)

# from random import *
# for i in range (10):
#    print(randint(20,100,))                     #  All random value any number will print


# 4 Randrange
# Randrange(10) ==generate random number from 0 to 9
# Randrange(11) ==generate random number from 1 to 10
# randrange(0,11,2)  ==0,2,4,6,8,10

# from random import *
# for i in range (10):
#     print(randrange(1,11))

# from random import *
# for i in range (10):
#     print(randrange(0,11,2))


# 5 Choice
# It won't generate random number
# It will generate a random number from the given sequence


# from random import *
# l=['kavin','sunder','mohan']
# for i in range (10):
#     print(choice(l))

# # To generate  6 digit random number which are used as OTP?

# from random import *
# for i in range(10):
#     print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')


# from random import *
# aplh='adsfdbgfhtyyfyrtrew'
# digits='012345678'
# for i in range(10):
#     print(choice(aplh)+choice(digits)+choice(aplh)+choice(digits))


#Fake Employee Data

# from random import *
# aplh='adsfdbgfhtyyfyrtrew'
# digits='012345678'
# def get_fake_name():
#     name=choice(aplh).upper()
#     n=randint(2,9)
#     for i in range (n):
#         name=name+choice(aplh)
#     return name

# for i in range (10):
#     print(get_fake_name) 


# 66


















# cAlass
# collection of objects.

 

# # Using "instance" method use 'self' argument

# the instance (self) as the first argument, allowing them to access
# and modify the attributes of that specific instance.


# def m1(self):
#     self.x

# class student:  

# #      # init method or constructor 
# #      # inside init pass the                      # argument / parameter 
#     def __init__(self, name,mark):  
#         self.name = name             # Instance attribute
#         self.mark=mark  

#     # Sample Method   
#     def Display(self):  
#         print("Hi ",self.name)  
#         print("Your mark is",self.mark)

#     def Grade(self):
#        if self.mark>=60:
#           print("First mark")  

#        elif self.mark>=40:
#           print("Second mark")       

#        else:
#           print("Last mark")


# n=int(input("Enter the no of Student :"))
# for i in range(n):
#    name=input("Enter the Name :")
#    mark=int(input("Enter the mark :"))
#    s=student(name,mark)
#    s.Display()
#    s.Grade()

# # Using class method use'@classmethod' 

# @classmethod
# def m1(self,cls):
#     cls.x


# class geeks:
#     course = 'DSA'

#     def purchase(obj):
#         print("Purchase course : ", geeks.course)
# geeks.purchase = classmethod(geeks.purchase)
# geeks.purchase()



# # Use '@staticmethod' for this process

# Usage: Static methods are used when you want to perform an action that is related 
# to the class but does not need to access or modify the instance or class-specific attributes.
# They behave just like regular functions but are included in the class's namespace.

# Access: Static methods cannot access or modify the instance's attributes or the class's attributes. 
# They are independent of class or instance state.


# def add(x,y):             # X and Y are parameter    
#     print(x+y)            # 10 and 20 are argument  

# class MyClass:
# 	def __init__(self, value):
# 		self.value = value

# 	def get_value(self):
# 		return self.value

# sample code
# n='asdfg'
# for i in n:
#     print(i)


# def wish(name):
#     print("Hello {},Good Morning".format(name))
# wish('kavin')


# # # creating multiple object in simple program


# class student :
#     def __init__(self,n,o):
#         self.name=n
#         self.no=o

#     def details(self):
#         print("my name is",self.name)
#         print("my no is",self.no)


# print('*'*20)
# s=student ('erevv',34)
# s.details()
# # print(s.name,s.no)        # outside of instance variable

# print('*'*20)
# s2=student('eiopov',2354)
# s2.details()
# print('*'*20)

# s3=student('egdfbh',24)
# s3.details()
# print('*'*20)





# class student:
#     def __init__(self):
#         print(id(self))
        
        
#     @staticmethod
#     def findavg(x,y):
#         print("Average",(x+y)/2)
        
         
# s=student()
# # print(id(s))
# s.findavg(10,20)
                


# # instance variable


# class student:
#     def __init__(self,n,o):
#         self.name=n
#         self.no=o

#     def info(self):
#         self.mark=49
#         x=45                             # local variable

# s=student("ferfc",24)
# s.info()       
# s.a=10
# print(s.__dict__)



# # delete the self variable and object reference



# class cs:
#     def __init__(self):
#         self.a=12
#         self.b=3
#         self.f=4
        
#     def delete (self):
#         del self.a
#         del self.f

# s=cs()
# print(s.__dict__)
# print('*'*20)

# s.delete()
# print(s.__dict__)
# print('*'*20)

# del s.b
# print(s.__dict__)
# print('*'*20)




# class cs:
#     def __init__(self):
#         self.a=12
#         self.b=3
#         self.f=4

#     # def delete (self):
#     #     del self.a

# s=cs()  
# s1=cs()
# print(s.__dict__)
# print(s1.__dict__)

# print('*'*20)
# del s.b
# print(s.__dict__ )


# print('*'*20)
# del s1.a
# print(s1.__dict__ )





# class cs:
#     def __init__(self):
#         self.a=12
#         self.b=3
#         self.f=4
        
# s=cs()
# s1=cs()
# s.a=35435
# s1.f=7688
# print(s.a,s.b,s.f)
# print(s1.a,s1.b,s1.f)


# class test:
#     a=10                     
#     def __init__(self):
#         test.a=20

#     @classmethod
#     def m1(self):
#         self.a =30
#         test.a=40

    
#     @staticmethod
#     def m2():
#         test.a=50
    

    
# t=test()
# t.m1()
# t.m2()
# t.a=60
# print(test.a)
# print(t.a)




# delete  inside of static variable

# class test:
#     a=20
#     def __init__(self):
#         del test.a
        
# print(test.__dict__)
# t=test()
# print(test.__dict__)


# delete outside 

# class test:
#     a=20
#     b=20
    
# t=test()
# del test.a
# print(test.b)
# del test.b





# class test:
#     a=10
#     def m1(self):
#         self.y=20 

# t1=test()
# t2=test()
# test.a=3445
# test.y=6778
# print(test.a,test.y)






# class test:
#     a=10
#     def __init__(self):
#         self.y=20 
        
# t1=test()
# t2=test()
# print(t1.a,t1.y)
# print(t2.a,t2.y)
# print('*'*20) 
# t1.a=3445
# t2.y=6778
# print(t1.a,t1.y)
# print(t2.a,t2.y)




# class test:
#     x=10
#     def __init__(self):
#         self.y=20

# t1=test()
# t2=test()
# print(t1.x,t1.y)
# print(t2.x,t2.y)
# print('*'*20)
# test.x=454
# t1.y=999
# print(t1.x,t1.y)
# print(t2.x,t2.y)



# local variable


# class test:
#     def m1(self):
#         a=100
#         print(a)

#     def m2(self):
#         b=30
#         print(b)

# t=test()
# t.m1()
# t.m2()


# class test:

#     def average(self,l):
#         l=sum(l)/len(l) 
#         print("the average is",l)
        
# t=test()   
# t.average([10,20,30,40])



# x=100         #  global variable
# class test:
#     x=300
#     def m1(self):
#         x=545
#         print(x)
#         print(self.x)
        
#     def m2(self):
#         print(x)
#         print(test.x)

# t=test()
# t.m1()
# t.m2()



# class test:
#     def m1(self):
#         global x
#         x=545
#         print(x)
        
        
#     def m2(self):
#         print(x)
        
# t=test()
# t.m1()
# t.m2()



# # # Application of Banking process
# # import sys

# class customer:

#     bankname='KVB'
      
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance

#     def deposit(self,amt):
#         self.balance=self.balance+amt
#         print("The Total  Account balance is :",self.balance)

#     def withdraw(self,amt):
#         if amt>self.balance:
#             print("Insufficient amount cannot perform the operation")
#             exit()
#         else:
#             self.balance=self.balance-amt
#             print("After withdraw the amount The balance is:",self.balance)
            
#     # def withdraw(self,amt):
#     #     if amt>self.balance:
#     #         print("Insufficient amount cannot perform the operation")
#     #         sys.exit()
            
#     #     self.balance=self.balance-amt
#     #     print("After withdraw the amount The balance is:",self.balance)
            
            
# print("Welcome the ",customer.bankname)
# name=input("Enter the name :")
# c=customer(name)

# while True:
#     print("d-Deposit\nw-Withdraw\ne-Exit")
#     option=input("Enter Your option :")
#     if option=="d":
#         amt=int(input("Enter the amount to deposit :"))
#         c.deposit(amt)

#     elif option=="w":
#         amt=int(input("Enter the amount to withdraw:"))
#         c.withdraw(amt)

#     elif option=="e":
#         print("Thank you for Banking ")
#         exit()

#     else:
#         print("Invalid option\nPlease choose the correct option")
      
      
      
# class students:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark

#     def display(self):
#         print("The student name is :",self.name)
#         print("The student mark is :",self.mark)

#     def grade(self):

#         if self.mark>=80:
#             print("o")
            
#         elif self.mark>=60:
#             print("A")
            
#         elif self.mark>=40:
#             print("B")
            
#         else:
#             print("Fail")
            
# n=int(input("Enter the students :"))
# # count=1 
# #while(count<=n):

# for i in range (n):
#     name=input("Enter the student name :")
#     mark=int(input("Enter the mark:"))
#     n=students(name,mark)
#     n.display()
#     n.grade()
#     # count=count+1


        
        
# class Animal:
#     legs=4
    
#     @classmethod
#     def walk(cls,name):
#         print('{} walks with {} legs'.format(name,cls.legs))
        
# Animal.walk('Dog')
# Animal.walk('cat')
        
        
        
# class Test:
#     count=0
#     def __init__(self):
#         Test.count=Test.count+1


#     @classmethod
#     def Noofobject(cls):
#         print("No of object created",cls.count)

# t1=Test()
# t2=Test()
# t3=Test()
# t4=Test()
# t5=Test()
# t6=Test()
# Test.Noofobject()

        
        
# class Maths:

#     @staticmethod
#     def Add(x,y):
#         print("the sum of two no is",x+y)
         
#     @staticmethod
#     def Sub(x,y):
#         print("the sub of two no is",x-y) 
        
#     @staticmethod
#     def Average(x,y):
#         print("the Average  of two no is",(x+y)/2)

# Maths.Add(10,20)
# Maths.Sub(10,20)
# Maths.Average(10,20)
        
        
 
# # static method
      
# class method:

#     # @staticmethod
#     def m1(x):
#         print("some thing",x)

# method.m1(10)     
# # t=method()
# # t.m1(10)



# class method:
    
#     @staticmethod
#     def m1(x):
#         print("some thing",x)
# method.m1(10)         
        
      
# class method:
#     def m1():
#         print("some thing")
# method.m1()         
        
        
        
# #  Inner classes

# class Employee:
#     def __init__(self,no,name,sal):
#         self.no=no
#         self.name=name
#         self.sal=sal

#     def Display(self):
#         print("Employee no is :",self.no)  
#         print("Employee name id :",self.name)
#         print("Emlpoyeen salary is :",self.sal)
        
        
# class Test:
#     def Modify(emp):
#         emp.sal=emp.sal+10000
#         emp.Display()
        
# A=Employee(123456,'kavin',40000)
# A.Display()
# Test.Modify(A)


# # # Inner class creation 

  
# class outer:
#     def __init__(self):
#         print("Outer class creating")
        
#     class inner:
#         def __init__(self):
#             print("Inner class creation")
            
#         def m1(self):
#             print("Inner class method")
            
# # o=outer()
# # I=o.inner()
# # I.m1()

# # i=outer().inner()
# # i.m1()             
        
# outer().inner().m1()       
        
        
        
        
# class person:
    
#     def __init__(self):
#         self.name='Kavin'
#         self.dob=self.DOB()  

#     def display(self):
#         print("My name is :",self.name)
#         self.dob.Display()

#     class DOB:

#         def __init__(self):
#             self.d=22
#             self.m=1
#             self.y=2004
            
#         def Display(self):
#             print("DOB={}/{}/{}".format(self.d,self.m,self.y)) 
            
            
# p=person()
# p.display()

        
# Another method
      
# class person:
    
#     def __init__(self,name,d,m,y):
#         self.name=name
#         self.dob=self.DOB(d,m,y)  
        
#     def display(self):
#         print("My name is :",self.name)
#         self.dob.Display()
        
#     class DOB:
        
#         def __init__(self,d,m,y):
#             self.d=d
#             self.m=m
#             self.y=y
            
#         def Display(self):
#             print("DOB={}/{}/{}".format(self.d,self.m,self.y)) 
            
            
# p=person("Kavin",22,1,2004)
# p.display()
   
     
# class person:
    
#     def __init__(self,name,d,m,y):
#         self.name=name
#         self.d=d
#         self.m=m
#         self.y=y  
        
#     def display(self):
#         print("My name is :",self.name)
#         DOB=("{}/{}/{}".format(self.d,self.m,self.y))
#         print(DOB)

           
# p=person("kavin",22,1,2004)
# p.display()





        
# class Human:
#     def __init__(self):
#         self.head=self.Head()
#         # self.brain=self.Brain()
        

#     class Head:
#         def __init__(self):
#             # self.brain=self.Brain()
#             print("Head is important")
#             self.brain=self.Brain()
        
#         class Brain:
#             def __init__(self):
#                 print("In brain we can thick a lot")     
# h=Human()

                

# Nested Method

# class Test:
#     def m1(self):
        
#         def sum(a,b):
#             print("First no :",a)
#             print("Second No :",b)
#             print("the sum is :",a+b)
#             print("the product is :",a-b)
#             print('*'*20)
            
#         sum(10,20)
#         sum(100,200)
#         sum(200,400)
        
# a=Test()
# a.m1()
            

# # Garbage Collection
# it will remove the unwanted files  stored in the memory

# import gc
# print(gc.isenabled())
# gc.disable()     
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())
           
           
           
            
# import gc
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} created")

#     def __del__(self):
#         print(f"{self.name} destroyed")

# # Create an object
# obj1 = MyClass("Object 1")

# # Reference it with another variable
# obj2 = obj1

# # Delete one reference
# del obj1

# # Force garbage collection (optional)
# gc.collect()

# # Delete the last reference
# del obj2

# # Force garbage collection (optional)
# gc.collect()



            
              
# import time

# class Test:
#         def __init__(self):
#                 print("Object Initialization")   
#         def __del__(self):
#                 print("fullfilling last wish")
# t1=Test()
# t1=None
# time.sleep(5)
# print("End of application")

            
            
# import time
# class Test:
#         def __init__(self):
#                 print("Object Initialization")
                
#         def __del__(self):
#                 print("fullfilling last wish")
                
# # t1=Test()
# # t2=t1
# # t3=t2
# # t4=t3
# # del t1
# # time.sleep(10)
# # print("After deleting t1 object not destroyed ")
# # del t2
# # del t3
# # time.sleep(10)
# # print("still object is not eligible for gc")
# # time.sleep(10)
# # del t4
# # time.sleep(10)
# # print("end of application")

# list=[Test(),Test(),Test()]
# time.sleep(4)
# list=None
# time.sleep(4)
# print("End of Application")



           
# import time
# import sys
# class Test:
#         def __init__(self):
#                 print("Object Initialization")
 
# t1=Test()
# t2=t1
# t3=t2
# t4=t3
# print(sys.getrefcount(t1))




# Polymorphism
# poly - many
# morph - form

# one name but multiple forms
# Tea, Juice ,Beer
# kavin -friends ,college ,family


# 4 types
# Duck typing
# Method Overloading
# operator Overloading
# method overriding




# Method Overloading

# same name/method but different argument types
# deposit(cash)
# deposit(cheque)
# deposit(dd)
 

# Operator Overloading

# Operator Overloading  +,*,>,<,>=,<=
# 10+3>>13
# kavin**3>> kavinkavinkavin

# + =__add__()
# - =__sub__()
# * =__sub__()
# / =__div__()
# % =__mod__()
# // =__floordiv__()
# ** =__pow__()

# +=  =__iadd__()
# -=  =__isub__()

#  For all symbol

# >  =__gt__()
# >= =__ge__()
# <  =__lt__()
# <= =__le__()

# class Book:

#         def __init__(self,pages):
#                 self.pages=pages
                
#         def __add__(self,other):
#                 return self.pages+other.pages
        
#         def __sub__(self,other):
#                 return self.pages-other.pages
        
#         def __mul__(self,other):
#                 return self.pages*other.pages

#       #   def __div__(self,other):
#       #           return self.pages//other.pages
# b1=Book(100)
# b2=Book(200)
# b3=Book(400)
# print(b1+b2)
# print(b2+b3)
# print(b1-b2)
# print(b1*b2)
# # print(b1//b2)



# class Book:
        
#         def __init__(self,pages):
#                 self.pages=pages
                
#         def __str__(self):
#                 # return "KAVIN"
#                 return "The no of pages :"+str(self.pages)
        
#         def __add__(self,other):
#                 total=self.pages+other.pages      # Add many str function
#                 b=Book(total)
#                 return b
        
# b1=Book(100)
# b2=Book(200)
# b3=Book(300)
# print(b1+b2+b3)              


# class student:
#         def __init__(self,name,marks):
#                 self.name=name
#                 self.marks=marks           
        
#         def __lt__(self,other):
#                 return self.marks<other.marks   
# s1=student("kavin",200)
# s2=student("Mohan",300)
# print(s1<s2)




# class Employee:
        
#         def __init__(self,name,salary):
#                 self.name=name
#                 self.salary=salary
                
#         def __mul__(self,other):
#                 return self.salary*other.days
# class Timesheet:
#         def __init__(self,name,days):
#                 self.name=name
#                 self.days=days
                      
#       #   def __mul__(self,other):
#       #           return self.days*other.salary                

# e=Employee("KAVIN",500)
# t=Timesheet("MOHAN",30)
# print("The Month salary is :",e*t)
# # print("The Month salary is :",t*e)


# Method Overloading


# class Test:
        
#         def m1(self):
#                 print("kavin")
                
#         def m1(self,x):
#                 print("Mohan")
                
# t=Test()
# t.m1(10)


# class Test:
#     def __init__(self):
#         print("yes") 
        
#     def __init__(self,a):
#         print("kavin")          

#     def __init__(self,a,b):
#         print("Nivash")
        
# T=Test(1,3)


# class Test:
        
#         def __init__(self,a=None,b=None,c=None):
        
#                 if a!=None and b!=None and c!=None:
#                         print("Add the 3 numbers :",a+b+c)
                        
#                 elif a!=None and b!=None :
#                         print("Add the 2 numbers :",a+b)
                        
#                 else:
#                         print("provide 2 or more argument")
                        
# t=Test(10,20,30)
# t=Test(10,20)
# t=Test(10)
                        
        
# # We can add many no  
# class Test:
        
#         def __init__(self,*a):
#                 total=0
#                 for i in a:
#                         total=total+i
#                 print("the sum is :",total)

# t=Test(10,20,30)
# t=Test(10,20)
# t=Test(10,23,45,54,90,29) 


# # Add many str function
# class Test:

#         def __init__(self,*a):
#                 total=''
#                 for i in a:
#                         total=total+i
#                 print("the Result is :",total)
                
             
# t=Test('kavin')
# t=Test('kavin','pravin')
# t=Test('kavin','nivash') 
                  



# # # Over Riding

# class p:
#         def m1(self):
#                 print("KAVIN")
                
#         def m2(self):
#                 print("PRAVIN")
                
                
# class C(p):
        
#         def m2(self):
#                 super().m2()
#                 print("NIVASH")
                
# class CC(C):
#     def m3(self):
#         print("Nithish")
    
                
# a=CC()
# a.m1()
# a.m2()
# a.m3()
            
                   
                   
# class p:
#     def memory(self):
#         print("hard Disk+SSD")  
        
#     def ram(self):
#         print(1234)
        
# class C(p):
#     pass 

# a=C()
# a.memory()
# a.ram()        












# # Drive Videos


# # 116

# Generator 


# Memeoy problem will be raised
# l=[x for x in range(1000000000000000)]
# print(l)

# It will work " this is the generator concept"

# g=(x for x in range(10000))
# while True:
#     print(next(g))

# # If u use Yield function ,It is a generator

# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
# g=mygen()
# print(type(g))
# # print(next(g))
# # print(next(g))
# for i in g:
#     print(i)

# Generate first n natural numbers

# def first_n_natural_no(n):
#     x=1
#     while x<=n:
#         yield x
#         x+=1    
# values=first_n_natural_no(10)
# for x in values:
#     print(x)

   
# import time
# def countdown_generator(maxvalue):
#     print("start countdown")
#     while maxvalue>0:
#         yield maxvalue
#         maxvalue=maxvalue-1
# n=int(input("Enter the number:"))   
# values=countdown_generator(n)
# for x in values:
#     print(x)
#     time.sleep(1)


# Fibonaaci Numbers
# 0,1,1,2,3,5,8,13...

# import time
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# g=fib()
# for x in g:
#     print(x)
#     time.sleep(1)


#  Fibonaaci number below  100
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# g=fib()
# for x in g:
#     if x>100:
#         break
#     print(x)
    
    
    
# # # Only 5 number 
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# g=fib()
# count=1
# for x in g:
#     if count>5:
#         break
#     count=count+1
#     print(x)



# # 117

# Generator vs Normal collection
 
# import random
# import time
# names=['kavin','pravin','nivash','jai','nithish']
# subject=['tamil','English','maths','science','social']
# def people_list(num_of_people):
#     result=[] 
#     for i in range(num_of_people):
#         person={'id':i,'name':random.choice(names),'subject':random.choice(subject)}
#         result.append(person)
#     return result
# #   t1=time.sleep()
# people=people_list(2)
# # t2=time.sleep()
# # print("the time taken by generator :",t2-t1)
# print(people)


# Check

# import random
# import time
# names=['kavin','pravin','nivash','jai','nithish']
# subject=['tamil','English','maths','science','social']
# def people_generator(num_of_people):
    
#     for i in range(num_of_people):
#         person={'id':i,'name':random.choice(names),'subject':random.choice(subject)}
#         yield person

# t1=time.clock()
# people=people_generator(100)
# t2=time.clock()
# print("the time taken by generator :",t2-t1)



# We can convert the generator int list

# def first_n_no_generator(n):
#     i=1
#     while i<=n:
#         yield i
#         i=i+1
# g=first_n_no_generator(10)
# l=list(g)
# print(l)

  
# # Syntax Error
# #  The Error will occur because idf invalid syntax : syntax error

# # Run time error / logical error / exceptions error

# x= int(input("Enter the First  number :"))
# y= int(input("Enter the second number :"))
# print(x/y)
# print(10/0)           # Error
# print(10/'ten')         #  type error



#  118 

# Exception Handling
# Purpose of Exception
# Default Exception Handling
#  Syntax 
   
#  Exception Handling
# 3 types
# compilte time
# logic 
# run time

# compilte time error
# syntax error
# colon(:)
# spelling error


# logic error
# code is correct but wrong output


# run time error
# code is correct and logic is also correct
# if u give a input
# 6/0 is a run time error

#  Runtime Error / Logical Error
#  While running the program Runtime Error will come


# Compiler -- Syntax Checking
# Interpreter -- Execution

# Exeception
# It will show the error like string + int or divided by zero

# print(10/0)


#  119

# Exception Hierarchy
# customized exception handling by using try-except blocks 

# Base Exeception

# Arithmetic Error
   # ZeroDivision
   # Floating point Error 
   # OverFlow Error
 
 
# Lookup Error
   # Index Error
   # Kerword Error


# OS Error
   #
   # File not found Error   
   # Interrupter Error
   # pemossion Error
   # TimeOut Error
   
   
# Customised Exeception Handling by using try except
# # Riskycode

# print('stre-1')
# try:
#    print(10/0)
# except ZeroDivisionError:
#    print(10/2)
# print('str3')
  

# try:
#    print(10/0)
# except ZeroDivisionError as e:
#    print("Exception Error :",e.__class__.__name__)
#    print("Exception Error :",type(e))


# try:
#    print(10/2)
# except ZeroDivisionError as e:
#    print("Exception Error :",e.__class__.__name__)
#    print("Exception Error :",type(e))

# try:
#    x=int(input('Enter the First value :'))
#    y=int(input('Enter the Second value:'))
#    print(x/y)
# except ZeroDivisionError:
#    print('ZeroDivisionError raised')
# except ValueError:
#    print("value Error raised")



# try:
#    x=int(input('Enter the First value :'))
#    y=int(input('Enter the Seci=ond value:'))
#    print(x/y)

# except BaseException as e:
#    print('Base exception Error :',e.__class__.__name__)
# except ZeroDivisionError:
#    print('ZeroDivisionError raised')
# except ValueError:
#    print("value Error raised")

# If we do in except method It will check one time only
# If we do in if else method It will check one by one . In if else we can't Expose error



# 120
 
# Single except block thar can handle multiple exception

# try:
#    x=int(input('Enter the First value :'))
#    y=int(input('Enter the Seci=ond value:'))
#    print(x/y)
# except (ZeroDivisionError,ValueError,BaseException)as e:
#    print('Exception raised and Its description :',e)


# try:
#    x=int(input('Enter the First value :'))
#    y=int(input('Enter the Seci=ond value:'))
#    print(x/y)
# except (ZeroDivisionError,ValueError,BaseException)as e:
#    print(e.__class__.__name__)


# try:
#    x=int(input('Enter the First value :'))
#    y=int(input('Enter the Seci=ond value:'))
#    print(x/y)
# except ZeroDivisionError:
#    print('ZeroDivisionError')
# except :
#    print('Default Except Block')


# Default Excption must be last
# try:
#    x=int(input('Enter the First value :'))
#    y=int(input('Enter the Seci=ond value:'))
#    print(x/y)
# except :
#    print('Default Except Block')
# except ZeroDivisionError:
#    print('ZeroDivisionError')


# Various Except Block

# Except ZeroDivisionError
# Except ZeroDivisionError as e:



# Finally Block


# try:
#   print(" Risky Code")
# except:
#    print("Handling code")
# finally:
#    print("Cleanup code")
   
# try:
#    "open db Connection"
#    "read Data"
# finally:
#   " close db connection"


# 121


# # Case 1-If there is no extension
# try:
#   print("try")
# except ZeroDivisionError:
#    print("Handling code")
# finally:
#    print('finally')


# Case 2-if an extension raised and handled
# try:
#   print("try")
#   print(10/0) 
# except ZeroDivisionError:
#    print("Handling code")
# finally:
#    print('finally')


# # Case 3-exception raised but not handled
# try:
#   print("try")
#   print(10/0) 
# except ValueError:
#    print("Handling code")
# finally:
#    print('finally')



# f=None
# try:
#    f=open('file.txt')
#    print(f.read()) 
# except FileNotFoundError:
#    print("specified file not found")
# finally:
#    if f is not None:
#       f.close()
#       print("is file closed:",f.closed)
   
 
#  Finally and return statement
# def f1():
#    return 10
#    print("Hello") 
#    print("Hello")      
#    print("Hello") 
#    print("Hello") 
# print(f1())


# def f1():
#    try:
#       # return 10
#       print("try")
#    except:
#       print("except")
#    finally:
#       print('finally')
# print(f1())


# def f1():
#    try:
#       print(10/0)
#       return 10
#    except:
#       print("except")
#    finally:
#       print('finally')
# print(f1())


# It will exit the after try process 
# import os
# def f1():
#    try:
#       print("try")
#       os._exit(0)
#    except:
#       print("except")
#    finally:
#       print('finally')
# f1()



# def f1():
#    try:
#       return 10
#    except:
#       print("except")
#    finally:
#       return 20
# print(f1())


# print(10/0) Terminated here itself
# try:
#       print("try")
# except:
#       print("except")
# finally:
#       print('finally')


# try: 
#    print(10/0)
# except ZeroDivisionError:
#    print("Exception Handled")
# try:
#    print('try')
# except:
#    print('Except')
# finally:
#    print('Finally')


# 122

# control flow in try except Finally

# try:
#    print('stm1')
#    print('stm2')
#    print('stm3')
# except :
#    print('stm4')
# finally:
#    print('stm5')
# print('stm6')

# case1 : if there is no exception
# 1,2,3,5,6

# Case2: if an exception raised at stm2 and
         # corresponding except block is matched
# 1,4,5,6 Normal Termination

# case3: if an exception raised at stm2 and
         # correspondin except block is not matched
# 1,5,Abnormal termination

# Case4: if an exception raised at stm4

# It is always abnormal Termination,But before abnormal
# termination finally block will be executed


# Case5:if an exception raised at stm5 or stm6 ,then it is
# always abnormal termination



# Nested try except finally
# try:
#    print('stm1')
#    print('stm2')
#    try:
#       print('stm3')
#       print(10/0)
#    except ZeroDivisionError:
#       print('handling code stm3')
#    print("stm4")
#    print("stm5")
#    print("stm6")
#    print("stm7")
#    print("stm8")
# except:
#    print('stm0')
# finally:
#    print('stm9')

      

# try:
#    print('stm1')
#    print('stm2')
#    try:
#       print('stm3')
#       print(10/'ten')
#    except ValueError:
#       print('handling code stm3')
#    print("stm4")
#    print("stm5")
#    print("stm6")
#    print("stm7")
#    print("stm8")
# except:
#    print('stm0')
# finally:
#    print('stm9')
      


# control flow in nested try except Finally


# try:
#    print('stm1')
#    try:
#       print('stm2')
#       print("stm3")
#       print("stm4")
#    except:
#        print('stm5')
#    finally:
#        print('stm6')
#    print('stm7')
   
# except:
#    print('stm8')
# finally:
#    print('stm9')
# print('stm0')

# If the Inner or is matched it is Normal Termination
# If the Inner and outer is not matched it is Abnormal Termination

# Case 1:If there is no exception
# 1,2,3,4,6,7,9,0, Normal termination

# Case2:if an exception raised at outer  stm1 and corresponding
# except block matched
# 8,9,0,Nt

# Case3 : if an exception raised at outer stm1 and corresponding
# except block not matched
# 9 Abnormal Termination

# Case4:if an exception raised at inner stm2 and corresponding
# except block matched
# 1,5,6,7,9,0,NT

# Case 5:if an exception raised at inner stm2 and corresponding
# except block not matched, but outer an exception is matched
# 1,6,7,8,9,0,NT

# Case 6:if an exception raised at inner stm2 and corresponding
# except block not matched, but outer an exception is not matched
# 1,6,7,9, AT


# 123 

# Else Block with try except finally

# If try block executed without any exception ,else will excute
# if inside try  block if any exception occur ,except will execute
# if u want to use else, compulsory except block should be there
# Else part will give only after except ,if it not ,it will give error
# try-except-else-finally the order is must ba same

# try:
#    print("try")
#    # print(10/0)
# except ZeroDivisionError:
#    print('except')
# else:
#    print("else")
# finally:
#    print("finally")



# try:
#    f=open('abc.txt')
# except FileNotFoundError:
#    print('specified file is not already available ')
# else:
#    print(f.read())
# finally:
#    if f is not None:
#       f.cose()
  
# compulsory try and except , try and finally, 
# try except and finally,except and else
# We can't take multiple finally and else state



# 124

# Exception Handling




# 125

# File Handling

# # To hold out data temporarily
# l=[]
# while (data :=input("Enter some name :"))!='done':
#    l.append(data)
# print(l)


# Files  
#  to store less amount of data
# TO store a data permanently

# Database
# to store huge amount of data
# to store structured data/Relational data

# Big Data Tochnologies
# Hadoop
# Cloud

# Types of files
# 1.text files/character files
#    abc.txt,running.txt,test.py

#  2.Binary files
#   video/audio files/images etc

# # Opening a file:
# f=open('open of file,mode')
# f=open('abc.txt','r')
 
# r:read
# open an existing file read operation
# if the specified file is not available,
#   then we will get the FIlenot found Error

# w--Write
# open an existing file for write operation
# if the specified file is not already available,
#  new file will be created
# if the file available bit it contain some data: over write Existing data


# a--append
#  w--Write
# open an existing file for append operation
# if the specified file is not already available,
#  new file will be created
# if the file available bit it contain some data:
#   over write Existing data won't be happened


# r+--read and write
# 
#  if the specified file is not already available,Filenotfound
#  if the file is available,but it contain some data:Overwrites existing data

# w+ ---Write and read

# if the specified file is not already available,then a new file be created
#  if the file is available,but it contain some data:Overwrites existing data


# a+ ---append and reaf

# if the specified file is not already available,then a new file be created
# if the file is available,but it contain some data:Overwrites existing data won't be happend


# x ---->exclusive write operation

# to perform write operation.
# the specified file should not be available already.==>FIleExistsError
#   complusory a new file should be created and then write operation


# r,w,a,r+,w+,a+,x

# 1. In which file of the following file will be created
# w,a,w+,a+,x

# 2. In which of the following mode file should be available already?
# r,r+

#  3. In which of the following mode file should  not be available
# x

#  4. In which of the following modes overwriting of existing data will be happend
# w,r+,w+

# r,w,a,r+,w+,a+,x -->All these modes are applicable only for text files
# B means binary file
# rb,wb,ab,r+b,w+b,a+b,xb -->All these modes are applicable only for text files


# f=open('abc.txt')
# The default mode is :r

# f=open('abc.txt,mode)
# perform required operation
# close the file

# closing a file
# f.close()


# Files
#    RegularExpression
#    web scraping
#    logging

# Various properties of file object
# f=open(name of the file,mode)
# f.name
# f.mode
# f.closed

# f.isreadble()
# f.iswritable()

# f=open('abc.txt','r')
# print('File Name:',f.name)
# print('File Mode:',f.mode)
# print('Is file Readable:',f.readable())
# print('Is file writeable:',f.writeable())
# print('Is file closed:',f.closed)
# f.close()
# print('Is file closed:',f.closed)



# f=open('abc.txt','r')
# print('File Name:',f.name) abc.txt
# print('File Mode:',f.mode)   r
# print('Is file Readable:',f.readable())  True
# print('Is file writeable:',f.writeable()) Flase
# print('Is file closed:',f.closed)  False
# f.close()
# print('Is file closed:',f.closed)  True



# f=open('abc.txt','w')
# print('File Name:',f.name) abc.txt
# print('File Mode:',f.mode)   r
# print('Is file Readable:',f.readable())  False
# print('Is file writeable:',f.writeable()) True
# print('Is file closed:',f.closed)  False
# f.close()
# print('Is file closed:',f.closed)  True




# f=open('abc.txt','a')
# print('File Name:',f.name) abc.txt
# print('File Mode:',f.mode)   r
# print('Is file Readable:',f.readable())  False
# print('Is file writeable:',f.writeable()) True
# print('Is file closed:',f.closed)  False
# f.close()
# print('Is file closed:',f.closed)  True



# f=open('abc.txt','r+')
# print('File Name:',f.name) abc.txt
# print('File Mode:',f.mode)   r
# print('Is file Readable:',f.readable())  True
# print('Is file writeable:',f.writeable()) True
# print('Is file closed:',f.closed)  False
# f.close()
# print('Is file closed:',f.closed)  True



# f=open('abc.txt','w+')
# print('File Name:',f.name) abc.txt
# print('File Mode:',f.mode)   r
# print('Is file closed:',f.closed)  True



# f=open('abc.txt','a+')
# print('File Name:',f.name) abc.txt
# print('File Mode:',f.mode)   r
# print('Is file Readable:',f.readable())  True
# print('Is file writeable:',f.writeable()) True
# print('Is file closed:',f.closed)  False
# f.close()
# print('Is file closed:',f.closed)  True



# f=open('abc123456.txt','x')
# print('File Name:',f.name) abc.txt
# print('File Mode:',f.mode)   r
# print('Is file Readable:',f.readable())  False
# print('Is file writeable:',f.writeable()) True
# print('Is file closed:',f.closed)  False
# f.close()
# print('Is file closed:',f.closed)  True




























