class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Name: {self.name}")
        print("Borrowed Books:", self.borrowed_books)


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        self.books.append(Book(title, author))
        print("Book Added Successfully!")

    def register_patron(self):
        name = input("Enter Patron Name: ")
        self.patrons.append(Patron(name))
        print("Patron Registered Successfully!")

    def issue_book(self):
        pname = input("Enter Patron Name: ")
        btitle = input("Enter Book Title: ")

        patron = None
        for p in self.patrons:
            if p.name == pname:
                patron = p
                break

        if patron is None:
            print("Patron Not Found!")
            return

        for book in self.books:
            if book.title == btitle:
                if book.available:
                    book.available = False
                    patron.borrowed_books.append(book.title)
                    print("Book Issued Successfully!")
                else:
                    print("Book is Already Issued!")
                return

        print("Book Not Found!")

    def return_book(self):
        pname = input("Enter Patron Name: ")
        btitle = input("Enter Book Title: ")

        for p in self.patrons:
            if p.name == pname:
                if btitle in p.borrowed_books:
                    p.borrowed_books.remove(btitle)
                    for book in self.books:
                        if book.title == btitle:
                            book.available = True
                    print("Book Returned Successfully!")
                    return

        print("Invalid Return!")

    def display_books(self):
        if len(self.books) == 0:
            print("No Books Available.")
        else:
            for book in self.books:
                book.display()

    def display_patrons(self):
        if len(self.patrons) == 0:
            print("No Patrons Registered.")
        else:
            for patron in self.patrons:
                patron.display()


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.register_patron()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        library.display_patrons()
    elif choice == "7":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
