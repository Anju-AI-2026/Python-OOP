# Smartphone Class using @property

class Smartphone:
    # Constructor to initialize brand and model
    def __init__(self, brand, model):
        self.brand = brand
        self._model = model  # private attribute

    # Getter method using @property
    @property
    def model(self):
        return self._model

    # Display phone details
    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")


# Creating object
phone = Smartphone("Samsung", "Galaxy A15")

# Accessing property like an attribute
phone.show_details()
