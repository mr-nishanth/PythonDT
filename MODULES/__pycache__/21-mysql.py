"""
How to connect MySQL to Python ?

install mysql.connected -- how to install pip install mysql connector

mysql.connected is breach for MySQL and Python

"""
from mysql import mysql.connector

con = mysql.connector.connect(host="localhost", username="root", password="NiShAnTh@007", database="")

cur = con.cursor_obj()

cur.execute("select * from student")


result = cur.fetchall()

for i in result:
    print(i)