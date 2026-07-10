# Shopping Cart Class using __len__() Magic Method

class ShoppingCart:
    # Constructor to create an empty shopping cart
    def __init__(self):
        self.items = []

    # Method to add an item to the cart
    def add_item(self, item):
        self.items.append(item)

    # __len__() returns the total number of items in the cart
    def __len__(self):
        return len(self.items)


# Creating a ShoppingCart object
cart = ShoppingCart()

# Adding items to the cart
cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

# Printing the total number of items
# Python automatically calls the __len__() method
print("Items in Cart:", len(cart))
