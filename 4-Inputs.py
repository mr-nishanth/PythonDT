
                              # Type conversion
# Name = input("Enter your Name ")
# Age = int(input("Enter your Age"))
#
# print(Name)
# print(Name +' is '+ (Age) + ' is old')       #concatnate string to string
# print(Name +' is '+ str(Age) + ' is old')

                               # Without type conversion

# Name = input("Enter your name")
# age = int(input("Enter your your age"))
# height = float(input('Enter your weight'))
Name = 'Nishanth'
age = 21
height = 6.1

#print("{0} is {1} years is old and Height {2} inch " .format(Name, age, weight))
print("%s is %i years is old and Height is %f inch " %(Name, age, height))
print("%s is %s years is old and Height is %s inch " %(Name, age, height))    #--> Fully in String
print("%r is %r years is old and Height is %r inch " %(Name, age, height))    #--> Debugging Information


# F - string


print(f" \n {Name} is {age}  years is old and Height is {height} inch")