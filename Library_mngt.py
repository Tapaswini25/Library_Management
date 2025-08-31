import json
import os
from datetime import datetime, timedelta
# ----------------------------
# Library Management System 
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

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["isbn"], data["available"])


class Member:
    def __init__(self, name, member_id, borrowed_books=None):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books else []

    def borrow_book(self, book, days=14):
        if book.available:
            book.available = False
            due_date = (datetime.now() + timedelta(days=days)).strftime("%d-%m-%Y")
            self.borrowed_books.append({"isbn": book.isbn, "due_date": due_date})
            print(f"\n {self.name} borrowed '{book.title}'. Due date: {due_date}")
        else:
            print(f"\n Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        for record in self.borrowed_books:
            if record["isbn"] == book.isbn:
                due_date = datetime.strptime(record["due_date"], "%d-%m-%Y")
                today = datetime.now()
                fine = 0
                if today > due_date:
                    days_late = (today - due_date).days
                    fine = days_late * 10  # Rs.10 per day late
                book.available = True
                self.borrowed_books.remove(record)
                print(f"\n {self.name} returned '{book.title}'")
                if fine > 0:
                    print(f" Book was {days_late} days late. Fine = Rs.{fine}")
                return
        print(f"\n {self.name} does not have '{book.title}' borrowed.")

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        return Member(data["name"], data["member_id"], data["borrowed_books"])


class Library:
    def __init__(self,data_file="Library.json"):
        self.books = []
        self.members = []
        self.data_file = data_file
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        print(f"\n Book '{book.title}' added to the library.")
        self.save_data()

    def add_member(self, member):
        self.members.append(member)
        print(f"\n Member '{member.name}' added to the library.")
        self.save_data()

    def add_member(self, member):
        self.members.append(member)
        print(f"\n Member '{member.name}' added to the library.")
        self.save_data()

    def show_books(self):
        print("\n===== Library Books =====")
        if not self.books:
            print("No books in the library yet.")
        for book in self.books:
            print(book)
    
    def search_books(self, keyword):
        print(f"\n Search Results for '{keyword}':")
        results = []
        for book in self.books:
            if (keyword.lower() in book.title.lower() or 
                keyword.lower() in book.author.lower() or 
                keyword == book.isbn):
                results.append(book)

        if results:
            for book in results:
                print(book)
        else:
            print(" No matching books found.")


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
    
    def save_data(self):
        data = {
            "books": [book.to_dict() for book in self.books],
            "members": [member.to_dict() for member in self.members]
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(b) for b in data.get("books", [])]
                self.members = [Member.from_dict(m) for m in data.get("members", [])]


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
        print("6. Search Books")
        print("7. Exit")

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
                library.save_data()
            else:
                print("\n Invalid member ID or ISBN.")

        elif choice == "5":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            member = library.find_member(member_id)
            book = library.find_book(isbn)
            if member and book:
                member.return_book(book)
                library.save_data()
            else:
                print("\n Invalid member ID or ISBN.")

        elif choice == "6":
            keyword = input("Enter title or author or isbn to search: ")
            library.search_books(keyword)

        elif choice == "7":
            print("\n Exiting... Goodbye!")
            library.save_data()
            break
        else:
            print("\n Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    main()
