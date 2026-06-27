# Python program to demonstrate a bank class

class Bank:

    # Constructor to initialize bank account details and default values
    def __init__(self,name,account_number):
        self.name=name
        self.account_number=account_number
        self.balance=0
    
    # Method to deposit amount
    def deposit(self,amount):
        if (amount>0):
            self.balance+=amount
            print("Deposit successfully")
        else:
            print("Enter a valid amount")

    # Method to withdraw amount
    def withdraw(self,amount):
        if(amount>0) and (amount<=self.balance):
            self.balance=(self.balance - amount)
            print("Amount withdraw successfully!!!")
            print("The current Balance : ",self.balance)
        elif(amount>self.balance):
            print("Insufficient fund")
        else:
            print("Enter a valid amount")

    # Method to display phone details
    def show_details(self):
        print("Account name : ",self.name)
        print("Account number : ",self.account_number)
        print("Balance amount : ",self.balance)

    # Display banking menu options
    def see_menu(self):
        print("============Choose a option from the menu============")
        print("1.See menu")
        print("2.Show details")
        print("3.Deposit Amount")
        print("4.Withdraw Amount")
        print("6.Exit")
        
# Taking input from the user and validating the input
while True:
    name=input("Enter your name : ")
    if (name.isalpha()):
        break
    else:
        print("Account number should not contain numbers")


print("Account number should be a 8 digit number")
while True:
    account_number=input("Enter your acount number : ")
    if (len(account_number) ==8 and account_number.isdigit()):
        print("Valid account number")
        break
    else:
         print("Invalid account number! Please enter exactly 8 digits") 

# Create Bank object
account=Bank(name,account_number)

# Initially printing Menu
print("============Choose a option from the menu============")
print("1.See menu")
print("2.Show details")
print("3.Deposit Amount")
print("4.Withdraw Amount")
print("6.Exit")

# Menu-driven banking system
while True: 
   
    choice=int(input("Enter a choice number : "))


    if choice==1:
        account.see_menu()
    elif choice==2:
        account.show_details()    
    elif choice==3:
        amount=float(input("Enter the amount to deposit : "))
        account.deposit(amount)
    elif choice==4:   
        amount=float(input("Enter the amount to withdraw : "))
        account.withdraw(amount)    
    elif choice==6:
        print("======THANK YOU======")
        exit()
    else:
        print("Please enter a valid choice")
