# Wallet Class using __add__() Magic Method

class Wallet:
    # Constructor to initialize the wallet balance
    def __init__(self, balance):
        self.balance = balance

    # __add__() adds the balance of two Wallet objects
    def __add__(self, other):
        return Wallet(self.balance + other.balance)

    # __str__() displays the wallet balance
    def __str__(self):
        return f"Wallet Balance: ₹{self.balance}"


# Creating Wallet objects
wallet1 = Wallet(2500)
wallet2 = Wallet(1800)

# Adding two Wallet objects
wallet3 = wallet1 + wallet2

# Printing the result
print(wallet3)
