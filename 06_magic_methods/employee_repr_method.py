# Employee Class using __repr__() Magic Method

class Employee:
    # Constructor to initialize employee details
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # __repr__() returns the official string representation of the object
    def __repr__(self):
        return f"Employee({self.emp_id}, '{self.name}', {self.salary})"


# Creating Employee objects
emp1 = Employee(101, "Anjali", 50000)
emp2 = Employee(102, "Rahul", 45000)

# Printing the objects
print(emp1)
print(emp2)
