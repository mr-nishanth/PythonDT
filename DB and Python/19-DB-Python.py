"""

1. Python supports Database operations as like any other programming languages
2. Python has inbuilt Sqlite3 DB within it
3. For any other DB we need to install the packages.
4. Databases are nothing but the collection of Tables
5. Tables are the collection on Rows and Columns
6. DBMS vs RDBMS

Note PK --> Primary Key
-----------------------------------------------------------------------------------------------------------------------
REPORT:
         PK
    col  Id            name        salary        department                position                    hireData 

    row   1         Nishanth         50k         HR                        Manager                     2020-01-04
    
-------------------------------------------------------------------------------------------------------------------------

7. DML statements ---->(Modify) insert , update , delete

8. DDL statements ---> Data Defination languages --> create , alter , table 

9. Transaction related Statement (more the two tables) one record ah depend painne update painnukoim 

    eg:
        Bank --> Amount transfer from one person to another person suppose in between la error 
        vaintha namakaa amount return vainthuruim
                        This is the main Advantages of Transaction related Statement


                        ------DATA TYPES-------
                Sample:
                --> Varchar / text
                --> Integer / number
10. What ius primary key ?
    Its not allowed duplicate keys
    """

"""

                    How to Create Table in SQLite 3

import sqlite3

# How to Create DB in SQLITE 3

con = sqlite3.connect("Students.db")

# we need to excute Any statement in sqlite3 ,  we have one cursor object ...in this below statement cursor_obj is variables
# How to create cursor Object ?
# Connection is used to create cursor object

cursor_obj = con.cursor()

sql_query = "create table student(id integer primary key, name text)"


# How to excute 

cursor_obj.execute(sql_query)


# To save 
con.commit()

"""
#----------------------x-----------------------------------x-------------------------x----------------------------
"""
import sqlite3

con = sqlite3.connect("Students.db")

cursor_obj = con.cursor()

# sql_query = "create table student(id integer primary key, name text)"
 
# cursor_obj.execute(sql_query)

sql_insert = "insert into student(id, name) values(?, ?)"      # values (?,?) its us to overcome the SQL injuction
cursor_obj.execute(sql_insert, (2, "Mohan"))

sql_select = "select * from student"
cursor_obj.execute(sql_select)
datas = cursor_obj.fetchall()


for data in datas:
    print(data)


con.commit()

"""
#---------------------x------------------------------x------------------------------------------x-------------------------------

                                #  Convert  String to (method) function

import sqlite3

def get_connection():

    return sqlite3.connect("Students.db")

def create_table(con):  # Create table work yakanuim na cursor object ah pass painnanuim , 
                            #create_table inu irrukara variable ikku cur_obj yaruinu theriyathu so we pass cur_obj 
                            # so oru object ah craete painnanuim

    cur_obj = con.cursor()
    sql_query = "create table student(id integer primary key, name text)"
    #cursor_obj.execute(sql_query)
    cur_obj.execute(sql_query)
    #cur_obj is object
    con.commit()

def insert_record(con, values):
    ins_cur_obj = con.cursor()
    sql_insert = "insert into student(id, name) values(?, ?)"      # values (?,?) its us to overcome the SQL injuction
    ins_cur_obj.execute(sql_insert, values)
    con.commit()



def fetch_record(con):
    cursor_obj = con.cursor()
    sql_select = "select * from student"
    cursor_obj.execute(sql_select)
    datas = cursor_obj.fetchall()


    for data in datas:
        print(data)


    con.commit()

conn = get_connection()
# create_table(conn)

insert_record(conn, (4, "Arun"))
fetch_record(conn)
