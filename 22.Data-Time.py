from datetime import datetime
from datetime import date

print(datetime.now())  # System Time Zone  -- today date ,time with seconds
print(date.today())  # Today date only

print(date.today().strftime("%d-%m/-y"))
  # (strftime) used to Change the order of data , month , year   

print(date.today().strftime("%d-%B-%y"))  



# ---------------------------X ------------- TypeCasteX  ----------------------------------x--------------------------


a =datetime.strptime("20-09-05","%y-%m-%d")
print("\n\t", a)
print(type(a))