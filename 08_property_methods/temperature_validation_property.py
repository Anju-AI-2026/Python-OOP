# Temperature Class using Property Validation

class Temperature:
    # Constructor to initialize temperature
    def __init__(self, value):
        self._value = value  # private attribute

    # Getter method
    @property
    def value(self):
        return self._value

    # Setter method with validation
    @value.setter
    def value(self, new_value):
        if new_value >= -273:
            self._value = new_value
        else:
            print("Invalid temperature! Cannot go below -273°C.")

    # Display temperature details
    def show_details(self):
        print(f"Temperature : {self.value}°C")


# Creating object
temp = Temperature(25)

print("Initial Temperature:")
temp.show_details()

# Updating temperature with a valid value
temp.value = 100

print("\nAfter Valid Update:")
temp.show_details()

# Trying to set an invalid temperature
print("\nTrying Invalid Update:")
temp.value = -500

print("\nFinal Temperature:")
temp.show_details()
