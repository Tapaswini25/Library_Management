# ----------------------------
# Library Management System (Menu Driven)
# ----------------------------

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

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
            print(f"\n {self.name} borrowed '{book.title}'")
        else:
            print(f"\n Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"\n {self.name} returned '{book.title}'")
        else:
            print(f"\n {self.name} does not have '{book.title}' borrowed.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"\n Book '{book.title}' added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"\n Member '{member.name}' added to the library.")

    def show_books(self):
        print("\n===== Library Books =====")
        if not self.books:
            print("No books in the library yet.")
        for book in self.books:
            print(book)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None


# ----------------------------
# Menu System
# ----------------------------
def main():
    library = Library()

    while True:
        print("\n====== Library Menu ======")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Show Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            library.add_book(Book(title, author, isbn))

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.add_member(Member(name, member_id))

        elif choice == "3":
            library.show_books()

        elif choice == "4":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            member = library.find_member(member_id)
            book = library.find_book(isbn)
            if member and book:
                member.borrow_book(book)
            else:
                print("\n Invalid member ID or ISBN.")

        elif choice == "5":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            member = library.find_member(member_id)
            book = library.find_book(isbn)
            if member and book:
                member.return_book(book)
            else:
                print("\n Invalid member ID or ISBN.")

        elif choice == "6":
            print("\n Exiting... Goodbye!")
            break
        else:
            print("\n Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    main()
