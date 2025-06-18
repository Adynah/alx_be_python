class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False 

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out       

class Library():
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        """Add a Book instance to the library"""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if available"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"Checked out '{title}"
        return f" '{title}' is unavailable."
    
    def return_book(self, title):
        """Return a book by title"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.return_book()
                return f"Returned '{title}"
        return f" '{title}' was not returned or not found."
    
    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if not available:
            return f"No books available."
        return [f"{book.title} by {book.author}" for book in available]