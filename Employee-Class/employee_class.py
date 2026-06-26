# Program to demonstrate an Employee class

class Employee:

    def __init__(self, name, id, salary, department, address ):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department
        self.address = address

    # Display the employee information
    def show_details(self):
        print("Employee ID :", self.id) 
        print("Employee Name :", self.name) 
        print("Monthly income :", self.salary) 
        print("Employee department :", self.department) 
        print("Employee address :", self.address) 

    # Calculate the annual income
    def calculate_salary(self):
        annual_salary = (self.salary * 12)
        return annual_salary

    # Calculate the annual bonus
    def  calculate_bonus(self):
        annual_salary = self.calculate_salary()
        if (self.salary <= 40000 ):
            print("Yearly bonus :",(annual_salary* 0.20) )
        elif(self.salary > 40000 and self.salary < 120000):
            print("Yearly bonus :", (annual_salary* 0.15))
        elif(self.salary >= 120000):
            print("Yearly bonus :", (annual_salary* 0.10))
        else:
            print("This salary is not under company salary system")             

    # Check category of Employee
    def employee_category(self):
        if (self.salary <= 60000 ):
            print("Junior Employee")
        elif(self.salary > 60000 and self.salary <= 120000):
            print("Mid-Level Employee")    
        elif(self.salary > 120000):
            print("Senior Employee")


      



