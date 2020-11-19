# Exception

# Exceptions are the (errors)  which we can handle
# All the exception classes are must need to derive from exception
# Ex:
#     ZeroDivisionError or DivideByZero Exception,
#     StackOverflow Exception and more ,
# How to handle Exception
#
# syntax:
#              try:    This is try catch block , suppose any errors coming in the code ,that time we use this
#                 ..........
#                 Except IOError:
#                 .............
#
# We have finally block
# We have else block
#  Syntax
#     try:
#     ..........
#     Except:
#     .........
#     else:
#     ........
#     finally
#     .........

# print(1/0)
# try:
#     print(1/0)
# except ZeroDivisionError as i:
#     print("Handling " + str(i))
# else:
#     print("Null Error")
# # except BaseException:
# #     print("Here Exception")
# finally:
#     print("Please try again")

#   Customs Exceotions


# class ApplicationCustomException(BaseException):
#     pass
#
# class validationException(ApplicationCustomException):
#     pass
# try:
#     if 0 < 10 :
#         raise validationException
# except validationException as ex:
#     print(validationException)
#     print("Excepation raise")
