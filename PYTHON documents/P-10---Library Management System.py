"""
Project :-  Library Management System

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

from abc import ABC,abstractmethod

#abstract class
class Library(ABC):
    def __init__(self):
        self.__books = {"Python":5,"C++":3,"Java":4} #pvt variable

    @abstractmethod
    def borrow_books(self,bookname):
        pass
    def available_books(self):#only be access by available_books() function
        return self.__books  #Getter method to access pvt. variable


#child class
class user(Library):
    def borrow_books(self,bookname):
        books = self.available_books() #accessing pvt data via parent class method

        
        if bookname in books and books[bookname] > 0:
            print(f"You Borrowed : {bookname}, Remaining : {books[bookname]}")
        else:
            print("Book not available")


#Creating object
user1 = user()
user1.borrow_books("Python")
user1.borrow_books("C++")
        









