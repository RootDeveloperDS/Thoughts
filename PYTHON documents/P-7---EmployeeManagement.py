
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
