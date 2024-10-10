# Base Class - Book
class Book:
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an ebook with file size in addition to title and author."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size  # In KB

    def __str__(self):
        """Return a string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a print book with page count in addition to title and author."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count  # In pages

    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition - Library
class Library:
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (of any type) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
