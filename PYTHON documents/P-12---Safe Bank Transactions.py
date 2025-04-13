"""
Project 12:- Safe Bank Transactions
~ users can dposit and withdraw money
~ preven negative deposits and over withdrawals
~ handles invalid deposits(value error)
~ handers over-withdrawls(InsufficientFundsTransfer)

"""

"""
~define custom exception class insufficientfundserror thrt inherits fron exception.it will be raise when withdraw amount exceed balance
~define bank account class
~implement deposit method
    deposit(deposit method)
     check if deposit amount is - and raise error
     else add the amount to balance
~implement new withdrawl method
    withdraw (withdraw method)
     chect if amount is greater than balance and raise an error insufficentfunderror
     else subtract amount from balance
~ create account object and do transactions"""


class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self,acc_holder,balance = 0):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self,amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        print(f"{amount} Deposited, New Balance: {self.balance}")
    def withdraw(self,amount):
        try:
            
            if amount > self.balance:
               raise InsufficientFundsError("Not Enoung Balance! ")
            self.balance -= amount
            print(f"{amount} Withdrawn, Remaining Balance: {self.balance}")
        except InsufficientFundsError as e:
           print(f"Error, {e}")

#using class
account1 = BankAccount("Devansh",1000)
account1.deposit(1500)
account1.withdraw(500)
account1.withdraw(True)



