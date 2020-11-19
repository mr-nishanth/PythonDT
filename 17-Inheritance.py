# --------------------------------------------------------------------------------------------------------------------------------------------

# Inheritance is an important aspects
#    It provide code reuseability
#  Concepts are Base class and derived class
# Derived class acquires properties from the base class
# Derived class----> Base class   {One on One Inheritance}

# Multi level Inheritance [ ClassN-->Class2-->Class1]

# Base Class1  Base Class2  Base Class N
#       |          |           |
#       |          |           |
#       ----Derived Class-----

# class Vehicle:
#     def engine(self):
#         print("I am from base class")
# class Car(Vehicle):
#     def break_system(self):
#         print("I am from derived class")
#
# # v = Vehicle()
# # v.engine()
# c = Car()
# c.break_system()
# c.engine()
#

# class Tree:
#     def Root(self):
#         print("It's base class ")
# class Mango(Tree):
#     def leaf(self):
#         print("It's derived class")
#
# # t = Tree ()
# # t.Root()
# m = Mango()
# m.Root()
# m.leaf()

# Multi level inheritance
class Vehicle:
    def engine(self):
        print("I am from base class")
class Car(Vehicle):
    def break_system(self):
        print("I am from derived class")
class Mini_Car(Car):
    def mini_hand_break(self):
        print("I am from CAR derived class")
# v = Vehicle()
# v.engine()
# c = Car()
# c.break_system()
# c.engine()
m = Mini_Car()
m.engine()
m.mini_hand_break()
m.break_system()


#        # Multiple inheritance
# class Vehicle:
#     def engine(self):
#         print("I am from base class")
# class Car:
#     def break_system(self):
#         print("I am from derived class")
# class Mini_Car(Car,Vehicle):-------------------------> #This the diff of multi and multiple
#     def mini_hand_break(self):
#         print(" I am from CAR derived class")
#
# m = Mini_Car()
# m.engine()
# m.break_system()
# m.mini_hand_break()
#
# class Shoes:
#     def Sports_Shoes(self):
#         print("I am from base class")
# class Addids_Shoes(Shoes):
#     def Running_shoe(self):
#         print(" I am from derived class")
#
# # S = Shoes()
# # S.Sports_Shoes()
# #                                                                            <It's my sample Ex>
# A = Addids_Shoes()
# A.Running_shoe()
# A.Sports_Shoes()
