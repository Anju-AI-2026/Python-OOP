# Smartwatch Class using Read-Only Property

class Smartwatch:
    # Constructor to initialize smartwatch details
    def __init__(self, brand, serial_number):
        self.brand = brand
        self._serial_number = serial_number  # private attribute

    # Read-only property
    @property
    def serial_number(self):
        return self._serial_number

    # Display smartwatch details
    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Serial Number : {self.serial_number}")


# Creating object
watch = Smartwatch("FitPulse", "SW2026X1001")

# Display details
watch.show_details()

# Trying to modify the read-only property
print("\nTrying to change serial number...")

try:
    watch.serial_number = "NEW12345"
except AttributeError:
    print("Serial number is read-only!")
