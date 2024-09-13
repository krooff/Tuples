def add_book(library, book):
    # Check if the book already exists in the library
    if book in library:
        print(f"The book '{book[0]}' by {book[1]} is already in the library.")
    else:
        # Add the new book to the library
        library.append(book)
        print(f"'{book[0]}' by {book[1]} has been added to the library.")

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Adding a new book
new_book = ("Fahrenheit 451", "Ray Bradbury")
add_book(library, new_book)

# Trying to add a duplicate book
duplicate_book = ("1984", "George Orwell")
add_book(library, duplicate_book)

# Print updated library
print("\nUpdated Library:")
for book in library:
    print(f"{book[0]} by {book[1]}")
