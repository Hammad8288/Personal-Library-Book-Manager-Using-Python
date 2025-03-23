import json

# File to store library data
LIBRARY_FILE = "library.json"

def load_library():
    """Load library data from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save library data to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a new book to the library."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "Title": title,
        "Author": author,
        "Year": int(year),
        "Genre": genre,
        "Read": read_status
    }
    library.append(book)
    print("Book added successfully!")

def remove_book(library):
    """Remove a book by title."""
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_books(library):
    """Search for a book by title or author."""
    choice = input("Search by: \n1. Title \n2. Author \nEnter your choice: ")
    query = input("Enter search term: ").lower()
    
    matches = [book for book in library if query in book["Title"].lower() or query in book["Author"].lower()]
    
    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, 1):
            read_status = "Read" if book["Read"] else "Unread"
            print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {read_status}")
    else:
        print("No matching books found.")

def display_books(library):
    """Display all books in the library."""
    if not library:
        print("Your library is empty.")
        return
    
    print("Your Library:")
    for i, book in enumerate(library, 1):
        read_status = "Read" if book["Read"] else "Unread"
        print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {read_status}")

def display_statistics(library):
    """Display total books and percentage read."""
    total_books = len(library)
    if total_books == 0:
        print("No books in library.")
        return
    
    read_books = sum(1 for book in library if book["Read"])
    percentage_read = (read_books / total_books) * 100
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    """Main function to run the Library Manager."""
    library = load_library()
    
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
