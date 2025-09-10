
'''File Handling in Python
Types of Access Modes

Books and Storage Capacity:
10 Books on Shelf: Small, easy to manage.
100 Books in Library: Large, harder to manage.

Types of Storage:
Fast Storage (RAM, Internal Memory): 16 GB.
RAM is volatile memory, meaning data is lost when the system is powered off.

Slow Storage (Hard Disk, External Memory): 256 GB.
Hard disks are non-volatile, retaining data even when the system is powered off.

Why Not Store Movies in RAM?
RAM is volatile, meaning all data is lost once the system is restarted.

Handling Files Using Python

Terminal Commands:

Mac: !pwd (Print Working Directory)
Windows: !cd (Change Directory)'''

#Creating a File:

#f1 = open("file_1.txt", "x")
# Running this command twice will result in an error because the file already exists.

'''Access Modes for File Handles:
The type of operations we perform on a file handle should match its access mode.
These modes also specify the behavior of the file handle within the range.'''

#Different Types of Modes


#--------------------------------------------------------------------------------
'''Read (r):

This mode opens a file for reading only.
The file must already exist; otherwise, an error (I/O error) will be raised.
It is the default mode for opening files.
The file pointer is placed at the beginning of the file.'''

#f1 = open("file_1.txt", "r")  # Raises error if file does not exist
# f1 = open("file_1.txt")  # By default in read mode
#data = f1.read()
#print(data)  # Cannot perform write operation
#-----------------------------------------------------------------------------------
'''Write (w):

This mode opens a file for writing only.
It overwrites the file if it already exists.
The file pointer is placed at the beginning.
If the file does not exist, a new file is created.'''

#f1 = open("file_2.txt", "w")  # Creates file if file_2 does not exist
#f1 = open("file_1.txt", "w")  # Erases content in file_1
#f1.write("Welcome to Abhishek's codeverse") #add this text
# print(f1.read())  # Raises error because read operation is not supported


#'\n' in next line
#------------------------------------------------------------------------------------

'''Read & Write (r+):

This mode opens a file for both reading and writing.
The file must already exist; otherwise, an error will be raised.
The file pointer is placed at the beginning of the file.'''

#f1 = open("file_1.txt", "r+") #do not erase the previous content
#print(f1.read())# Read
#f1.write("This is a Python Course!") #Write # File pointer at beginning
#print(f1.read())


#print(f1.tell())#to find file pointer
#f1.write("HI") #Welcome->HIlcome
#print(f1.tell())
#print(f1.read()) #print-->lcome
#print(f1.tell()) #at last

#-----------------------------------------------------------------------
'''Write & Read (w+):

#File pointer at the beggning
This mode opens a file for both writing and reading.
If the file already exists, its contents are truncated (cleared).
If the file does not exist, a new file is created.'''

#
# f1 = open("file_3.txt", "w+")
''' print(f1.tell())#0 '''
#
# f1.write("This is python")
# print(f1.tell())#10
#
# f1.write("Writing and reading!")
# print(f1.tell())#31
'''' f1.seek(0)#File pointer at begnning (moving) '''
# print(f1.tell())#0
#
# data=f1.read()
# print(data)
# print(f1.tell())#31
#
# f1.close()

#-----------------------------------------------------------------------------------

'''Append (a):

append write 
This mode opens a file for appending (adding new data to the end).
If the file does not exist, it creates a new file.
The file pointer is placed at the end of the file.'''

# f1 = open("file_2.txt", "a")
# f1.write("Appending text!")
# f1.write("Again Appending")


#-----------------------------------------------------------------------------------

'''Append & Read (a+):

This mode opens a file for both appending and reading.
If the file does not exist, it creates a new file.
The file pointer is placed at the end of the file.'''

# f1 = open("file_4.txt", "a+")
# f1.write("Appending and reading!")
# f1.seek(0)
# data = f1.read()
# print(data)

#-----------------------------------------------------------------------------------
# f1=open("D:\Love_Python\Text.txt","a+")
# print(f1.tell())
# f1.seek(0)
# print(f1.read())
# f1.write("Jenny Lecture")

#------------------------------------
#\n in next line
#f.readline() return first entry and after that
#f.readlines() return all content in a list
# along with this we can use indexatiobn




#'' # aoutput at end
#!cls clear
#cd # directory
#!ls availbale file

#s.read(2) # read two character
#f.seek(4)

#print(cont1)
#print(cont2)
#create a empty line in between
#use end='' to avoid this

#---------------------------------
'''Every time we open a file we have to close that particular 
in order to make the change '''

# '''Here is alternative way'''
# # Writing to a file
''' with open('example.txt', 'w') as file: '''
#     file.write("Hello, this is a test file.\n")
#     file.write("We're learning file handling in Python!")
#
# # Reading from a file
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

#--------------------------------
'''When reading from a file, \n is included at the end of each line (except for the last line, typically):'''

'''Strip Newlines
If you want to remove the newline characters when reading lines, you can use the .strip() method:'''

'''INput'''
# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line.strip())
'''Output'''
# Hello, this is the first line.
# And this is the second line.


# The newline character is a fundamental part of handling text files, helping to format the content correctly.

#--------------------------------------------------------------------------------------------------------------
'''
Deleting a File
For an example, I don't want to preserve this file called data.txt, 
now I want it to be removed from my system

import os
os.remove('data.txt')

For deleting a folder,
os.rmdir("examplefolder") <==lt will remove only empty folders'''

#---------------------------------------------------------------------------------------------------------------
'''When reading a file using f.readline(), the method retrieves the next line from the file, including the 
newline character (\n), if it exists. Once all lines are read, 
the method returns an empty string (''), indicating the end of the file.'''
