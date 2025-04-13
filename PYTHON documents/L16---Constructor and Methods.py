#1. what is constructor?(__init__method)    eg.
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def showdetails(self):
        print(f"employee name: {self.name} ,salary: {self.salary}")
         #creating objects
emp1=employee("Devansh",100000)
emp2=employee("Suraj",1000)
emp1.showdetails()
emp2.showdetails()

##2. Types of constructor

    #<1>.Default COnstructor(no arguments)
class example:
    def __init__(self):
        print("default constructor called")

obj=example()

    #<2>.Parameterized Constructor(Takes Parameter)
class Example:
    def __init__(self,value):
        print(f"default constructor called with value:{value}")

obj=Example(990)

    #<3>.Constructor with Default Values
class example:
    def __init__(self,name="Guest"):
        print(f"Hello {name}")

obj=example()
obj1=example("Devansh")

###3. What are Methods -->>Methods are functions inside class defines object behaviour
class Car: 
    def __init__(self,brand,model):
        self.brand=brand        
        self.model=model
        
    def showinfo(self):         #method (fnction inside the class)
        print(f"the Car is of {self.brand} with model{self.model}")


#creating object
Car1=Car("Toyota","Fortuner")
Car1.showinfo()

####4. Types of Methods in class
    #1#.. Instance Methods(operate on object data)
class Person:
    def __init__(self,name):
        self.name=name
                                                    #~Uses self to access instance attribute
    def greet(self):#instance method
        print(f"Hello ,my name is {self.name}")

P1=Person("Devansh")
P1.greet()

    #2#... Class Methods(operate on class data)
class School:
    school_name="ABC school" #class variable
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
                                                    #~uses classmethod and cls insted of self.,Modifies Class-Level Data insted of instance data 
School.change_school("XYZ Public School")
print(School.school_name)


    #3#... Static Method(Indipendent Utility Function)
class Math:
    def add(a,b):
        return a+b
                                                    #~Works as normal function insidea class
print (Math.add(55,45))




####### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ########
"""
project :- Bank Account Management

init initialises account holder and balance
deposit() adds money to balance
withdraw() deducts money from balance

"""







