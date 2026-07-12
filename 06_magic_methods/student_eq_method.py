# Student Class using __eq__() Magic Method

class Student:
    # Constructor to initialize student details
    def __init__(self, usn, name):
        self.usn = usn
        self.name = name

    # __eq__() compares two Student objects
    def __eq__(self, other):
        return self.usn == other.usn


# Creating Student objects
student1 = Student("CS001", "Anjali")
student2 = Student("CS001", "Rahul")
student3 = Student("CS002", "Priya")

# Comparing objects
print(student1 == student2)
print(student1 == student3)
