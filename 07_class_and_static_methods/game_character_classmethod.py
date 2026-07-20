# Game Character using @classmethod

class GameCharacter:
    # Class variable
    total_characters = 0

    # Constructor to initialize character details
    def __init__(self, name, character_type):
        self.name = name
        self.character_type = character_type

        # Increase total characters whenever a new object is created
        GameCharacter.total_characters += 1

    # Display character details
    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Type : {self.character_type}")

    # Class method to display total characters
    @classmethod
    def show_total_characters(cls):
        print(f"Total Characters : {cls.total_characters}")


# Creating objects
character1 = GameCharacter("Shadow", "Assassin")
character2 = GameCharacter("Blaze", "Warrior")
character3 = GameCharacter("Luna", "Mage")

character1.show_details()
print()

character2.show_details()
print()

character3.show_details()
print()

GameCharacter.show_total_characters()
