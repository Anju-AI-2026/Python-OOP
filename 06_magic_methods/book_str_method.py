class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title}\nAuthor: {self.author}\nPrice: ₹{self.price}"


book1 = Book("Python Basics", "Anjali", 499)

print(book1)
