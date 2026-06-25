# Program to demonstrate a Date class

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # Display the day
    def display_day(self):
        print("Day:", self.day)

    # Display the month number
    def display_month(self):
        print("Month:", self.month)

    # Display the year
    def display_year(self):
        print("Year:", self.year)

    # Display the month name
    def display_month_name(self):
        months = [
            "Unknown", "JANUARY", "FEBRUARY", "MARCH", "APRIL",
            "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER",
            "OCTOBER", "NOVEMBER", "DECEMBER"
        ]

        print("Month Name:", months[self.month])

    # Check whether the year is a leap year
    def is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            print(self.year, "is a leap year.")
        else:
            print(self.year, "is not a leap year.")


# Create an object of the Date class
date1 = Date(10, 2, 2004)

# Call the methods
date1.display_day()
date1.display_month()
date1.display_year()
date1.display_month_name()
date1.is_leap_year()
