"""
1. Python also supports file operations as like other programming languages
2. No need to import any third party library to do so.
3. Python provides inbuilt function itself
4. File creation, open and read all the operations are based on the file mode

--> Available file modes:

        --> w --> Writing
        --> r --> Reading
        --> a --> Appending               --> eg : log
        --> r+ -> Both read and write

5. Also can use (With - Keyword) for file operation
6. Need to memorizes only few method alone

        --> Open()          -->
        --> Close()         -->
        --> Write()         -->
        --> Read()          -->

7. File operations are slow always . Keep mind

"""
                # Write mode ,here override the content eachtime

# try:
#         file = open("Tutorial.txt", mode="w")
#         file.write("This is new content to the file")
# finally:
#         file.close()

#------------------------------------------------------------------------------------
                # Append Mode

# try: 
#         file = open("Append.txt", mode="a")
#         file.write("New content Added soon Dears!")
# finally:
#         file.close()

#--------------------------------------------------------------------------------
                                # Read mode
# try:
#         file = open("Read.txt", mode="r")
#         file.write("Welcome to learn Read mode in files operation")
# finally:
#         file.close()

# Its come error becoz its in read mode but we try to write so it's error ..
# Important one 1st time only create the file,then check the file here or not



# try:
#         file = open("Append.txt", mode="r")
#         print(file.read())

# finally:
#         file.close()

#----------------------------------------------------------------------------

try:
      with open("Append.txt", mode="a") as f :
        f.write("New contant From Both Read and write Mode")
finally:
        f.close()
