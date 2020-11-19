"""
    1. Design Pattern
    2. Adding Additional functionality to an object at RUN TIME
    3. Reduce code duplicate
    4. Python provide easy syntax for decorators too
    5. Deecorators are like a extension methods
    6. Which can accepts  arguments too
    7. Decorators executes first

            EX

                def to_upparcase(function):
                    def wrapper():
                        return function().upper()

                    return wrapper

                    How to call @

"""
#----x----x----x--------------------------------x-------------------x---------------------x--------------------

'''

def upper_decorator(function):
    def wrapper():
        return function().upper()
    return wrapper

#@upper_decorator
def getname():
    return 'Python Tutorial'

print(getname())

'''

def upper_decorator(function):
    def wrapper(a):
        print("From Decorator",str(a))
        return function(a).upper()
    return wrapper

@upper_decorator
def getname(name):
    return 'Python Tutorial'

print(getname("Nishanth"))
