#To OPEN File       open()
file=open("example.txt","r")        ###___'r'=read mode,___'w'=write mode(CREATE New file if not found),___'a'=append mode(Add data to file),___'x'=create a new file

##To READ File      .read()
file=open("example.txt","r")
content=file.read()
print(content)
file.close()                  # #ALWAYS CLOSE the file#

###To Write File    .write()
file=open("example.txt","w")
content=file.write("Hello,This is first file handling program")
print(content)
file.close()

####Appending File
file=open("example.txt","a")
content=file.write('\nAdding a new line without deleting old')    # ''' \n '''use to append in the file
print(content)
file.close()




##### USING with open() FOR AUTOMATIC FILE HANDLING  [{BEST PRACTICE}]
with open("example.txt","r") as file:
    content=file.read()             #Using As READ Mode
    print(content)  #No Need To Close The File

####### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ########

"""CREATE a "Notes Saver" project"""
