# Email Validator using @staticmethod

class EmailValidator:

    # Static method to validate an email address
    @staticmethod
    def is_valid(email):
        if "@" in email and "." in email:
            return True
        return False


# Sample email addresses
email1 = "anjali@gmail.com"
email2 = "pythonprogramming"

# Checking email validity
print(f"{email1} : {EmailValidator.is_valid(email1)}")
print(f"{email2} : {EmailValidator.is_valid(email2)}")
