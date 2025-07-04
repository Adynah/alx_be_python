from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    print("Brave New World by Aldous Huxley")
    print("1984 by George Orwell")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    print("Brave New World by Aldous Huxley")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    print("Brave New World by Aldous Huxley")
    print("1984 by George Orwell")
    library.list_available_books()

if __name__ == "__main__":
    main()