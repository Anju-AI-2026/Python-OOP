# Python program to demonstrate a bank class

class Bank:

    # Constructor to initialize bank account details and default values
    def __init__(self,name,account_number):
        self.name=name
        self.account_number=account_number
        self.balance=0
