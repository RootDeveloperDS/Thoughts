#1.
"""
class  = blue print of object,eg:--   class Car: #class
                                                pass  #empty class
                                                """
#2.
'object = instance of class'
#<!> Creating Object

class Car:  #Class(blueprint)
    def __init__(self,brand,model):
        self.brand=brand        #Object Properties
        self.model=model
        
    def showinfo(self):         #method (fnction inside the class)
        print(f"the car is of {self.brand} with model{self.model}")


#creating object
Car1=Car("Toyota","Fortuner")
Car2=Car("Tesla","Model 3")


Car1.showinfo()
Car2.showinfo()

"the __init__ method initialises the object properties "
#3. __init__()          method(CONSTRUCTOR)
    #called Automatically when object is created
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
#Creating Objects
s1=student("Devansh","18")
s2=student("Rahul","19")


print(s1.name,s1.age)   #we us e 'self' to make local variable use out of the __init__ function
print(s2.name,s2.age)


#4. creating METHODS in class
'method = function inside a class that defines object behaviour'
'eg:-'
class dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"{self.name} is barking")

dog1=dog("Bruno","Labrador")
dog1.bark()

####### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ########
"project:- Employee Management system"
"""employee class store name salary
show details() show their info"""
