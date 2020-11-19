# Sample while

# count = 1
# while count <= 10:
#     print(count)
#     count += 1    # count = count +1


# count = 1
# while (count != 10)
#     count+=1:
#     print(count)

                                                # Poem
prompt = "Write a poem! \n"
prompt += "Enter 'Quit' or 'quit' to End \n"

poem = ""
line = ""

while line != 'Quit' and line != 'quit':

    line = input(prompt)
    if line == 'Quit':
        break
    elif line == 'quit':
            break
    poem += line  # poem = poem + line ,(Here line stored in the poem becoz line empty ah irruthathain next while loop run panna mudiuim
    poem += '\n'  # It's mention the new line of the poem

# print(poem.replace('Quit' and 'quit', ''))

print(poem)
                          # Month

                 # Break
                 # Continue
# month = int(input("Enter your month"))
# day = 1
# while day <= 31:
#     if month == 2 and day > 28:
#         break
#     elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
#        # day +=1
#         break
#     print(day)
#     day += 1

                                       # While in List

# Sports =['Football', 'Volleyball', 'Handball', 'Throwball', 'Football', 'Handball', 'Handball']
# #print(Sports)
# while 'Handball' in Sports:
#     Sports.remove('Handball')
#
#     print(Sports)







