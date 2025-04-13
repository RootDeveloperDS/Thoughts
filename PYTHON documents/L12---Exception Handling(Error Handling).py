#use if Program crash due to error s in program
#handling with     try-except
try:
    x=int(input("Enter a number"))                              
    print(10/x)     #error if x=0
except ZeroDivisionError:               #if TRY code Gives Error Then Except Code is executed
    print("Cant divide by 0")

##Catching multiple errors
try:
    x=int(input("Enter a number"))                              
    print(10/x)    
except ZeroDivisionError:               #if TRY code Gives Error due to x=0
    print("Cant divide by 0")
except ValueError:
    print("Invalid input")              #if x=text

###Using   finally (always execute code)
try:
    file=open("test.txt","r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing program")        #ALWAYS EXECUTE


####### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ########
    """Create a "Safe Calculator" """
