# class Vechile:
#     def engine(self):
#         print("From base class")


#     def __engines(self):
#         print("From base private method")


# class Car(Vechile):
#     def brake_system(self):
#         print("From the derived class")

# C = Car()

# C.brake_system()
# C.engine()
# C.__engines()

#---------------------------------------------------------------------------------------------------

class Vechile:
    def __init__(self):
        print("From Base Class Constructor")
    def engine(self):
        print("From base class")


    def __engines(self):
        print("From base private method")


class Car(Vechile):

                                       
    def brake_system(self):
        print("From the derived class")

    

C = Car()

C.brake_system()


