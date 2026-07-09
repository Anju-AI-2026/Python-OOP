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

    # Method to withdraw amount
    def withdraw(self,amount):
        if(amount>0) and (amount<=self.balance):
            self.balance=(self.balance - amount)
            print("Amount withdraw successfully!!!")
            print("The current Balance : ",self.balance)
        elif(amount>self.balance):
            print("Insufficient fund")
        else:
            print("Enter a valid amount")

    # Method to display phone details
    def show_details(self):
        print("Account name : ",self.name)
        print("Account number : ",self.account_number)
        print("Balance amount : ",self.balance)
