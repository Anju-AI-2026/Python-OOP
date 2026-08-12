# Gaming Profile using Getter, Setter, and Deleter

class GamingProfile:
    # Constructor to initialize profile details
    def __init__(self, username):
        self._username = username  # private attribute

    # Getter method
    @property
    def username(self):
        return self._username

    # Setter method with validation
    @username.setter
    def username(self, new_username):
        if len(new_username) >= 4:
            self._username = new_username
        else:
            print("Username must contain at least 4 characters!")

    # Deleter method
    @username.deleter
    def username(self):
        print("Gaming profile username deleted!")
        del self._username

    # Display profile details
    def show_details(self):
        if hasattr(self, "_username"):
            print(f"Username : {self.username}")
        else:
            print("No username found!")


# Creating object
profile = GamingProfile("ShadowNinja")

print("Initial Profile:")
profile.show_details()

# Updating username
profile.username = "BlazeKing"

print("\nAfter Updating Username:")
profile.show_details()

# Trying invalid username
print("\nTrying Invalid Username:")
profile.username = "AB"

# Deleting username
print("\nDeleting Username:")
del profile.username

print("\nFinal Profile:")
profile.show_details()
