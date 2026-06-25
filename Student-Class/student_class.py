# program to demonstrate a student class

class Student:
    def __init__(self, name, roll_num, sub1, sub2, sub3):
        self.name = name
        self.roll_num = roll_num
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    
    # To show the details of the student
    def show_details(self):
        print("Student Name : ",self.name)
        print("Student Roll Number : ",self.roll_num)
        print("Subject 1 marks : ",self.sub1)
        print("Subject 2 marks : ",self.sub2)
        print("Subject 3 marks : ",self.sub3)
    
    # To calculate the total marks
    def calculate_total(self):
        total_marks = (self.sub1 + self.sub2 + self.sub3)
        return total_marks
    
    # To calculate the avarage marks of all subject
    def calculate_average(self):
        avg_marks = (self.sub1+self.sub2+self.sub3)/3
        return avg_marks
    
    # determine grade 
    def get_grade(self):
        avg = self.calculate_average()
        if (80 <= avg <= 100):
            print("A Grade")
        elif (60 <= avg < 80):
            print("B Grade")
        elif (40 <= avg < 60):
            print("C Grade")
        elif (35 <= avg < 40):
            print("Pass")
        else:
            print("Fail")
        

# Asking the user to enter information
name=input("Enter the student name : ")
roll_num=int(input("Enter the student roll number : "))
sub1=int(input("Enter the marks of first subject : "))
sub2=int(input("Enter the marks of second subject : "))
sub3=int(input("Enter the marks of third subject : "))

# Creating class object
s1=Student(name,roll_num,sub1,sub2,sub3)

# Printing the output
s1.show_details()
print("Total Marks is :",s1.calculate_total())
print("Avarage Marks is :",s1.calculate_average())
s1.get_grade()
