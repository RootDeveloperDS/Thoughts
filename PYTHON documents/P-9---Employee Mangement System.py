"""

<> parent class - employee()
         ~with 2 attributes-name, salary
         ~ getdetails() return f-string employee details

<> child class - developer inherits employee
         ~add attributes -> programing language -> stores language of developer
         ~super().__init__(name,salary) calls constructor of employee for name and salary
         ~mathod overriding: getdetails() is redifined to include program_language.
         
<> child class - manager inherits employee
         ~add attribute -> team_size- store no. of team member
         ~super().__init__(name,salary) init name and salary using employee constr.
         ~Overriding: get_details() modified to include team_size.

<> creating object and testing

"""

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def get_details(self):
        return f"Name: {self.name}, Salary : {self.salary}"

#child class 1 
class developer(employee):
    def __init__(self,name,salary,progg_lang):
        super().__init__(name,salary)#super is used to call function from super class to sub class
        self.progg_lang = progg_lang

    def get_details(self):
        return f"Name: {self.name}, Salary : {self.salary}, Language : {self.progg_lang}"

#child class 2
class manager(employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size = team_size

    def get_details(self):
        return f"Name: {self.name}, Salary : {self.salary}, Team Size : {self.team_size}"

#creating objects
dev =  developer("Devansh",100000,"Python")
mgr =  manager("Rahul",10000,10)


print(dev.get_details())
print(mgr.get_details())


