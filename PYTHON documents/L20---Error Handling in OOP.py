"""
~ understanding exception,try-except blocks,custom exceptions    """
# 1. using try-except .
class Calculator:
    def divide(self,a,b):
        try:                     # tries to execute the code
            result = a / b
            return result
        except ZeroDivisionError:# catches error if it occurs
            return "can't divide by Zero!"
#using the class
calc = Calculator()
print(calc.divide(10,2))
print(calc.divide(10,0))

# 2. Handling Multiple Errors .
class filemanager:
    def readfile(self,filename):
        try:
            with open(filename,"r") as file:
                return file.read()
        except FileNotFoundError:
            return "ERROR : File Not Found"
        except PermissionError:
            return "ERROR : No permission to read the file! "
        except Exception as e:
            return f"Unexpected Error : {e} "
  #using the class
file = filemanager()
print(file.readfile("data.txt"))
print(file.readfile("text.txt"))

# 4. Creating Custom EXCEPTION .
"eg.Custom Exception for Negative Age"
class InvalidAgeError(Exception):# create custom exception by inheriting exception
    pass# no additional logic needed,just a custom code
class person:
    def __init__(self,name,age):
        if age < 0:# it raises invalid age error
            raise
            InvalidAgeError("Age cannot be negative! ")
            self.name = name
            self.age = age
    #using class
try:
    p1 = person("Alice",25)
    p2 = person("Bob",-5)
except InvalidAgeError as e:
    print(f"Error : {e}")
    


####### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ########
"""
Project 12:- Safe Bank Transactions
~ users can dposit and withdraw money
~ prevent negative deposits and over withdrawals
~ handles invalid deposits(value error)
~ handers over-withdrawls(InsufficientFundsTransfer)

"""







