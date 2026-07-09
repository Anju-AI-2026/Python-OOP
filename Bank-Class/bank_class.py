# Python program to demonstrate a bank class

class Bank:

    # Constructor to initialize bank account details and default values
    def __init__(self,name,account_number):
        self.name=name
        self.account_number=account_number
        self.balance=0

    # Method to deposit amount
    def deposit(self,amount):
        if (amount>0):
            self.balance+=amount
            print("Deposit successfully")
        else:
            print("Enter a valid amount")
