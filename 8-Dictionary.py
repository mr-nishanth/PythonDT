# Dictionary are key value pair

            # Syndex  [] its represent to value the elements

# It's represent { "key" : "value"}
# it's mutable
# Key must br unique
# Methods Get
#        key
#        Copy
#        clear
# Dicr = {
#             "Name":"Gopi",
#              "No" : 1
#           }
#   ------------------------------------------------------------------------------------------------------------


dic = {"Name": "Nishanth", "Age": 20, "Schooling": "DJMS", "list": [10, 20, 30, 40, 50]}
dic2 = {"NAme": "Mohan", "Age": 50, "work": "Electrical"}

dic_copy = dic2.copy()
# dic["Age"]=25    it's use to change in dict'
# del dic["Name"] it's us to delete'

# print(type(dic))  FIND THE TYPE

# Get

A = dic.get("Schooling")
print(A)
print(dic)

# Clear

# A = dic.clear()
#
# print(A)   None
# print(dic)   Empty

# COPY

# print(dic_copy)
# dic2["NAme"]="Vaseekaran"
# print(dic2)

# Sample example Dict and List comb
# dic["list"].append(60)
# #print(A)
# print(dic)


person ={"Name": "VijaySurya","Age":24}
print(person['Name'])
print(person['Age'])

person['School']='AKN' #--> Add a element in Dictionary
person["Location"]= (12.3497 , 58.8375)
print(person)
print(type(person['Location']))

# del person["Location"]
# print(person)

# Nested Dictionary

person["Address"]={
                   'Street': 'Royal Street',
                   'City':'VAcitan City',
                    'Postal Code': 100020
}

#List In Dictionary
person['languages'] = ['Tamil', 'English']
print(person)
print(person['Address'])

# LOOP THROUGH's
# for key in person.keys():
#     print(key)
# for value in person.values():
#     print(value)
#
# for key, value in person.items():          # Items is use to print both (KEY and VALUE)
#     print(key.title(), '=', value)       # print(f'{key} ={value})

print("It's Complex DIctionary")
for key, value in person.items():
    if isinstance(value, tuple) or isinstance(value, list):   #isinstance is bulit in function
        for item in value:
            print(f'\t {key.title()} = {item}')
    elif isinstance(value, dict):
       # print(key)
        for key2, value2 in person.items():
            print(f'\t{key2.title()} = {value2}')
    else:
        print(f'\t{key.title()} = {value}')
