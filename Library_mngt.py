# ----------------------------
# Library Management System
# ----------------------------

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True   # all new books are available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added to the library.")

    def show_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)

# ----------------------------
# Demo / Testing
# ----------------------------

# Create a library
library = Library()

# Add books
b1 = Book("1984", "George Orwell", "12345")
b2 = Book("The Hobbit", "J.R.R. Tolkien", "67890")
library.add_book(b1)
library.add_book(b2)

# Add members
m1 = Member("Alice", "M001")
m2 = Member("Bob", "M002")
library.add_member(m1)
library.add_member(m2)

# Show books
library.show_books()

# Borrow & Return
m1.borrow_book(b1)   # Alice borrows 1984
m2.borrow_book(b1)   # Bob tries to borrow 1984 (should fail)
m1.return_book(b1)   # Alice returns 1984
m2.borrow_book(b1)   # Now Bob can borrow it
