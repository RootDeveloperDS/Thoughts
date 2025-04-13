"""
~ reading & writing files using Class and Objects
~ storing and retriving data in Text Files
~ implementing a Simple File Manager using OOP
""" 
# 1. allows us to - Save ,Modify , Retrive stored data """

## 2.Reading and Writing Files in OOP
    
'Creating class to handle file operations'
class filemanager:
    def __init__(self,filename):
        self.filename = filename

    #<1>.Writing File
    def write_to_file(self,data):
        with open(self.filename,"w") as file:#can create a file also
            file.write(data)
        print("Data written successfully!")

    #<2>.Reading file data
    def read_from_file(self):
        with open(self.filename,"r") as file:
            return file.read()#read and returns file content

    
    #Using above class
file = filemanager("data.txt")
file.write_to_file("Hello , its python file. ")

print(file.read_from_file())

### 3. Appending data to file (XNot OverwritingX)
class file_manager:
    def __init__(self,filename):
        self.filename = filename
    #<> Appending file
    def append_to_file(self,data):
        with open(self.filename,"a") as file:
            file.write("\n" + data)
        print("Data Appended Successfully")
    #using above class
file=file_manager("data.txt")
file.append_to_file("This Is an Added line")

####### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ########
"""
Project 11:-  Notes Manager

~create and save note,view , append new notes



"""









