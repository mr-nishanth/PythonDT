"""
1. Regular Expresion is for validation
2. Python has re module
3. With match method we can compare the data with pattern
4. Ex pattern: [0-9],[a-d],[^0-9]

        Code sample :

        import re
            pattern = '^a...a$'
            re.match(pattern,data)--> return boolean

"""

import re

data = "Python"

pattern = "^P....n$"

isvalid = re.match(pattern,data)


if isvalid:
    print("Success")
else:
    print("Failure")