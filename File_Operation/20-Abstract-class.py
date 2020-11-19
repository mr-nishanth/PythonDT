"""
1. It's always a base class
2. It's incomplete. So can't create object of it.
3. Python won't support it in straight  forward
4. We need to use module  called  ABC
5. Derived class must  provide definition for the abstract method
6. All the Abstract class must inherit from the ABC class
7. All the methods must be declared with attribute abstractmethod 


        @abstractmethod   ---> Attribute

        def method (self):

        pass


"""

#from abc import ABC, abstractmethod


# ( Is abstractclass in python ? no )   (Is abstractclass in C# ,java ? yes)
# class Abc_Class:
#     def method(self):
#         pass

# How to convert abstract class

#------------x------------------x---------------------x------------------------x------------------------x-------------x-xx
#from abc import ABC,abstractmethod

# class Abc_Class(ABC):
#     @abstractmethod
#     def method(self):
#         print(" From ABC class ")

# class ord_class:
#     def method1(self):
#         print(" From method 1 ")


#---------x--------------------x--------------------x------------------------x---------------------x------------------x----

from abc import ABC, abstractmethod


class Abc_Class(ABC):
    @abstractmethod
    def method(self):
        pass

class ord_class(Abc_Class):
    def method1(self):
        print(" From method 1 ")
    def method(self):
        print(" Base Class ")

A = ord_class()
A.method()
A.method1()