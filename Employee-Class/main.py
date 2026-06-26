from employee import Employee


def main():

    # Asking the user for the input

    # Validating the name
    while True:

        name = input("Enter your name :")
        if (name.isalpha()):
            break
        else:
            print("This name contain numbers it is not acceptable")

    # Validating the ID
    while True:

        id = input("Enter your E-ID :")
        if (id.isdigit()):
            break
        else:
            print("This E-ID contain charector it is not acceptable")

    # Validating the salary
    while True:

        salary = input("Enter your Monthly salary :")
        if (salary.isdigit()):
            break
        else:
            print("This salary contain charector it is not acceptable")

    salary = int(salary)

    department = input("Enter your Department :")
    address = input("Enter your home address :")

    # Creating object of Employee() class
    E1 = Employee(name, id, salary, department, address)

    # creating user interface
    while True:

        print("===========================================")
        print("======Menu======")
        print("1. Show details")
        print("2. Calculate annual salary")
        print("3. Calculate bonus")
        print("4. Employee category")
        print("5. Exit")
        print("===========================================")

        print("===========================================")
        choice = int(input("Enter a choice from the above menu :"))
        print("===========================================")

        if (choice == 1):
            E1.show_details()
        elif (choice == 2):
            print("Annual salary :", E1.calculate_salary())
        elif (choice == 3):
            E1.calculate_bonus()
        elif (choice == 4):
            E1.employee_category()
        elif (choice == 5):
            exit()
        else:
            print("Please enter a valid choice from the above")


if __name__ == "__main__":
    main()
  

