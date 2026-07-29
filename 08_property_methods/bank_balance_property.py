# Bank Account using @property and Setter

class BankAccount:
    # Constructor to initialize account holder and balance
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance  # private attribute

    # Getter method
    @property
    def balance(self):
        return self._balance

    # Setter method with validation
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative!")

    # Display account details
    def show_details(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance : ₹{self.balance}")


# Creating object
account = BankAccount("Anjali", 5000)

print("Initial Details:")
account.show_details()

# Updating balance using setter
account.balance = 7500

print("\nAfter Updating Balance:")
account.show_details()

# Trying to set a negative balance
print("\nTrying Invalid Update:")
account.balance = -1000
