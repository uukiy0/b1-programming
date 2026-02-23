# Lab Task 2: Library System with Composition
# create a Book Class

class Book:
    # This constructor runs when a new Book is created
    # stores the books basic details
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    # returns formatted information about the book
    def get_details(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn}"


# create library class
class Library:
    # The library has a name and a collection of books
    # This shows COMPOSITION (Library HAS Book objects)
    def __init__(self, library_name):
        self.library_name = library_name
        self.book_collection = []  # Empty list to store Book objects

    # Adds a Book object to the collection
    def add_book(self, book):
        self.book_collection.append(book)
        print(f"Book added successfully: {book.get_details()}")

    # Removes a book by matching its title
    def remove_book(self, title):
        for book in self.book_collection:
            if book.title.lower() == title.lower():
                self.book_collection.remove(book)
                print(f"Book removed: {book.get_details()}")
                return
        print(f"Could not find a book titled '{title}'.")

    # Displays all books currently in the library
    def show_books(self):
        if not self.book_collection:
            print(f"{self.library_name} currently has no books.")
            return

        print(f"\n--- Book List for {self.library_name} ---")
        count = 1
        for book in self.book_collection:
            print(f"{count}. {book.get_details()}")
            count += 1

    # Searches for books that contain a word in the title
    def search_title(self, keyword):
        matches = []

        for book in self.book_collection:
            if keyword.lower() in book.title.lower():
                matches.append(book)

        if matches:
            print(f"\nSearch Results for '{keyword}':")
            for book in matches:
                print("-", book.get_details())
        else:
            print(f"No books found with the title containing '{keyword}'.")

# Testing the Library System
# Create a library instance
my_library = Library("Downtown Library")

# Create at least 3 books
book_a = Book("Learning Python", "Mark Lutz", "978-1449355739")
book_b = Book("Code Complete", "Steve McConnell", "978-0735619678")
book_c = Book("Think Python", "Allen Downey", "978-1491939369")

# Add books to the library
my_library.add_book(book_a)
my_library.add_book(book_b)
my_library.add_book(book_c)

# List all books
my_library.show_books()

# Search for a specific book
my_library.search_title("Python")

# Remove one book and verify it :))
my_library.remove_book("Code Complete")
my_library.show_books()
