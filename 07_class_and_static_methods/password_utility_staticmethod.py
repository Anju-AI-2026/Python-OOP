# Password Utility using @staticmethod

class PasswordUtility:

    # Static method to check password strength
    @staticmethod
    def check_strength(password):

        if len(password) < 8:
            return "Weak Password"

        elif password.isalpha():
            return "Medium Password"

        elif password.isalnum():
            return "Strong Password"

        else:
            return "Very Strong Password"


# Checking different passwords
print(PasswordUtility.check_strength("python"))

print(PasswordUtility.check_strength("Python123"))

print(PasswordUtility.check_strength("Python@123"))
