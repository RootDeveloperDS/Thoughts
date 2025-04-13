class BankAccount:

    def __init__(self,acc_holder,balance=0): #constructor
        self.acc_holder = acc_holder
        self.balance = balance
        
        
    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited: {amount} ,New Balance: {self.balance}")

    def withdraw(self,amount):
        
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print(f"Withdraw: {amount},New Balance: {self.balance}")




#Creating Bank Account
Account1=BankAccount("Devansh",1000)


#Performing Transactions
Account1.deposit(1000)
Account1.withdraw(500)
Account1.withdraw(100)
