# Book Class using __str__() Magic Method

class Book:
    # Constructor to initialize book details
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # __str__() returns a readable string representation of the object
    def __str__(self):
        return (
            f"Book Title : {self.title}\n"
            f"Author     : {self.author}\n"
            f"Price      : ₹{self.price}"
        )


# Creating Book objects
book1 = Book("Python Programming", "Anjali", 499)
book2 = Book("Artificial Intelligence", "John Smith", 799)

# Printing the book objects

print(book1)

print()

print(book2)
