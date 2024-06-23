class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def __str__(self):
        return f"Member: {self.name}, ID: {self.member_id}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed {book.title} from the library.")
        else:
            print(f"{book.title} not found in the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member {member.name}.")

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            print(f"Removed member {member.name}.")
        else:
            print(f"Member {member.name} not found.")

    def __str__(self):
        return f"Library with {len(self.books)} books and {len(self.members)} members."


def main():
    # Create a library
    library = Library()

    # Create books
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Create a member
    member = Member("Alice", "M001")

    # Add member to the library
    library.add_member(member)

    # Borrow and return books
    member.borrow_book(book1)
    member.return_book(book1)

    # Print library status
    print(library)


if __name__ == "__main__":
    main()



