class LibraryBook:

    def __init__(self, title, author, price, is_available=True):
        self.title = title
        self.author = author
        self.price = price
        self.is_available = is_available

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return "Book borrowed successfully."
        else:
            return "Book is already borrowed."

    def return_book(self):
        self.is_available = True
        return "Book returned successfully."

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"Title: '{self.title}' | Author: {self.author} | Price: ₹{self.price:.2f} | Status: {status}"


class LibraryManager:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def search_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.strip().lower():
                return book
        return None


# Driver Code
manager = LibraryManager()

# Create 3 book objects
b1 = LibraryBook("Python Basics", "Guido van Rossum", 450.0)
b2 = LibraryBook("Clean Code", "Robert C. Martin", 750.0)
b3 = LibraryBook("Data Structures", "Mark Allen", 600.0)

# Add books to the manager
manager.add_book(b1)
manager.add_book(b2)
manager.add_book(b3)

# Display all books
print("--- All Library Books ---")
manager.display_books()

# Search for a book
search_title = input("\nEnter a book title to search: ")
found_book = manager.search_by_title(search_title)

if found_book:
    print(f"\nBook Found: {found_book}")
    borrow_choice = (
        input("Do you want to borrow this book? (yes/no): ").strip().lower()
    )

    if borrow_choice == "yes":
        message = found_book.borrow_book()
        print(message)
        print(f"Updated Book Details: {found_book}")
else:
    print("Book not found.")

# Calculate available and borrowed counts
available_count = sum(1 for book in manager.books if book.is_available)
borrowed_count = len(manager.books) - available_count

# Display totals
print("\n--- Library Summary ---")
print(f"Total Available Books: {available_count}")
print(f"Total Borrowed Books: {borrowed_count}")