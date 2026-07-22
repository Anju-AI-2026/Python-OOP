# Pizza Class using Factory Method and @classmethod

class Pizza:
    # Constructor to initialize pizza details
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    # Factory method to create a Margherita pizza
    @classmethod
    def margherita(cls):
        return cls("Medium", ["Cheese", "Tomato"])

    # Factory method to create a Veggie pizza
    @classmethod
    def veggie(cls):
        return cls("Large", ["Cheese", "Capsicum", "Onion", "Corn"])

    # Display pizza details
    def show_details(self):
        print(f"Size     : {self.size}")
        print(f"Toppings : {', '.join(self.toppings)}")


# Creating pizzas using factory methods
pizza1 = Pizza.margherita()
pizza2 = Pizza.veggie()

print("Margherita Pizza")
pizza1.show_details()

print("\nVeggie Pizza")
pizza2.show_details()
