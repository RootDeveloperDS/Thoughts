"""
Inheretence =  Reusing code from existing class.
    helps new Child class to reuse Parent class property and methods.
    
Polymorphism =  using common interface(METHODS)but for diff. behaviour
"""
#1.Eg.
class animal:
    def __init__(self,name):
        self.name=name

    def makesound(self):
        return "some sound"

#child class
class dog(animal):  #<(animal) is used to inherit>
    def makesound(self):                                #  dog inherits name and makesound() from animal.
 #overriding parent method                                                       #  dog overrides makesound() to return bark.
        return "Bark"

#creating objects
dogy = dog("Tommy")
print(dogy.name)

print(dogy.makesound())

##2. Types Of Inheritance

    #<1>. Single Inheritance (1 child,1 parent) (Above example)
    #<2>. Multiple Inheritance(multi parent,1 child)
class A:
    def method_A(self):
        return "Method A"
class B:
    def method_B(self):
        return "Method B"
class C(A,B):#Inherit from A and B
    pass

obj=C()#C can access methods from both A and B
print(obj.method_A())
print(obj.method_B())
    #<3>. Multilevel Inheritance(child to child)
class A:
    def method_A(self):
        return "Method A"
class B(A):
    def method_B(self):
        return "Method B"
class C(B):
    def method_C(self):
        return "Method C"

obj=C()
print(obj.method_A())
print(obj.method_B())
print(obj.method_C())
'-----------------------------------------------------------------------------------------------------------------------------------------------------------------'

###3. Polymorphism  eg.
class cat:
    def sound(self):
        return "meow"
class dog:
    def sound (self):
        return "bark"
    #using same method name
animals=[cat(),dog()]
for aniimal in animals:
    print (aniimal.sound())#calling methods by using for loop in list

####4. Method Overriding
class vehicle:
    def speed(self):
        return "speed varies"
class car(vehicle):
    def speed(self):
        return "car speed 100km/h"
class bike(car):
    def speed(self):
        return "bike speed is 80km/h"
    #objects
v=vehicle()
c=car()
b=bike()
print(v.speed())
print(c.speed())    # car and bike override speed from vehicle
print(b.speed())    

####### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ########


"""project:---  Employee Mangement system"""


"""

<> parent class - employee()
         ~with 2 attributes-name, salary
         ~ getdetails() return fstring employee details

<> child class - developer inherits employee
         ~add attributes -> programing language -> stores language of developer
         ~super.__init__(name,salary) calls constructor of employee for name and salary
         ~mathod overriding: getdetails() is redifined to include program_language.
         
<> child class - manager inherits employee
         ~add attribute -> team_size- store no. of team member
         ~super().__init__(name,salary) init name and salary using employee constr.
         ~Overriding: get_details() modified to include team_size.

<> creating object and testing

"""















