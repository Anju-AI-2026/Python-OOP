# Temperature Class using @classmethod

class Temperature:
    # Class variable
    unit = "Celsius"

    # Constructor to initialize temperature
    def __init__(self, value):
        self.value = value

    # Class method to change the temperature unit
    @classmethod
    def change_unit(cls, new_unit):
        cls.unit = new_unit

    # Display temperature details
    def show_details(self):
        print(f"Temperature : {self.value}° {Temperature.unit}")


# Creating Temperature objects
temp1 = Temperature(25)
temp2 = Temperature(30)

print("Before changing the unit:")
temp1.show_details()
temp2.show_details()

# Changing the unit using the class method
Temperature.change_unit("Fahrenheit")

print("\nAfter changing the unit:")
temp1.show_details()
temp2.show_details()
