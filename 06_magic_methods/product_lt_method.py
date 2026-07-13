# Product Class using __lt__() Magic Method

class Product:
    # Constructor to initialize product details
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # __lt__() compares the price of two products
    def __lt__(self, other):
        return self.price < other.price


# Creating Product objects
product1 = Product("Laptop", 65000)
product2 = Product("Mobile", 30000)

# Comparing objects
print(product1 < product2)
print(product2 < product1)
