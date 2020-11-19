# -------------------------------------------------------------------------------------------------------------------------------------
# Function
#  Function are way to divide your code
#  Improves code readability and reusability
#  Must be start with (def) keyword
#         2 types
#   - Required arguements    Value assign both varabiles (a=10,b=20)
#   - Defualt arguements     value assign single varabiles  a=50, b automattically assign b=50

# Ex:
#  def add_two_numbers(a,b):   -----> def Keyword, (a+b)-----> Required Argu ,  (a,b) ---> parameters
#      return  a+b

# def add_two_num(a,b):
#     return a+b
#                                   # -----> Required Argu
# Total = add_two_num(10,20)
# print(Total)

# def add_two_num(a, b=10):
#     return a + b
# -----> Default Argu
# Total = add_two_num(50)
# print(Total)


# def string(str):
#     return str
# ------> string
# Total = string("Nishanth")
# print(type(Total))
# print(Total)



                                                  #

# def greet():
#     """"Say Hello"""
#     print('Hello!')
#
# greet()
#
# def greet_user(name):                                         # Parameter---> name
#     print(f'Welcome! to My Website {name}')
#
# your_name = input("Enter your name here")
# greet_user(your_name)                                        #Arguement---> your_name
#     #user_name = input("Please enter your name")
#
#     # print(f'Hello! {user_name} Good morning')    # Formetal String in Print Function
#
#     #print("Hello!" + user_name +" Welcome to My Page")
#
# #greet_user()

# def greet_user(greet_message="Hello!", user_name="Anonymous"):
#     print("%s,%s"%(greet_message,user_name))
# greet_user('Nishanth','Welcome')
#
# greet_user(user_name='Nishanth',greet_message='Hai!') #-->Keyword Argument
# greet_user()


#
# def greet_user(name , greet_message="Welcome"):   # Default Greet-Message
#     print(f'{greet_message},{name}')
# greet_user('Nishanth','Hello')

def get_massage(greet,user):
    return f'{greet.upper()},{user.title()}'

greeting = get_massage("hey","nishanth")
print(greeting)

def square(num):
    return num*num

print(square(2))
print(square(3))
print(square(9))




# def greet_message(greet_message, user_name):
# #     print("%s,%s"%(greet_message,user_name))
#     greet_message = input('Enter your message')
#     user_name = input('Enter your name')
#     print('%s,%s'%(greet_message,user_name))
#
# greet_user(greet_message,user_name=)
#
# print('This will be')
# print('in new line')
#
# print('Using end will prevent it', end="") #-> End is used to compare  print statement
# print('from display new line')
#
# print(10, 20, 30, sep=' - ', end='') #-------> Sep is used to Separated the element or value
# #print('')-----------------------------------> New line