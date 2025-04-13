"""
# Encapsulation = Hiding Details and protecting Data.
        pvt attriute->   using   __      .eg.__balance
            ~to access pvt. attributes ,we use Getter Methods
                                          eg. get_balance()
            ~ eg. Bank Acc Balance

# Abstraction = Hiding Implementation details and showing only necessary features.
            ~ eg. Car Engine Functionaity
"""
#1.Encapsulation
    #eg.
class bankaccount :
    def __init__(self,acc_number,balance):
        self.acc_number = acc_number  # Public attribute
        self.__balance = balance      # Private Attribute using __

    def deposit(self ,amount):
        self.__balance += amount
        print(f"Deposited : {amount}, New Balance : {self.__balance}")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn : {amount}, Remaining Balance : {self.__balance}")
        else:
            print("Insufficient Balance")

    def get_balance(self):  #Getter method to access balance
        return self.__balance 

#creating obj
account = bankaccount("10293837465",4000)

account.deposit(1000)
print(account.get_balance) #we use getter insted of writing' account.__balance '


## 2 . Abstraction - using abstract class with abc module

from abc import ABC,abstractmethod
    #abstract class - cannot be init directly 
class vehicle(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def speed(self):
        pass

class car(vehicle):
    def speed(self):
        return "car speed : 100 km/h"
    
class bike(vehicle):
    def speed(self):
        return "bike speed : 80 km/h"
#objects
car= car("Tata")
bike = bike("Yamaha")

print(car.speed())
print(bike.speed())

####### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ########
"""
Project 10:-  Library Management System

~1 creting abstract class 'library'
~  have a pvt dictionary __books to store book name and availability
~  abstract method borrowbook() in child class
~  getter method available_books() provide access to pvt directory

~2 creating child class (user) inherits from library
~  implements borrowbooks() to allow use to borrow book
~  when borrowed ,count of book is desc. by 1
~  if book unavailable print unavailable

~3 creating object and borrow book
~  user object is created
~  book are borrowed by borrow books()
~  if available ,success message is printed.if not available, failed message is printed.


"""











