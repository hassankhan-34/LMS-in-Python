# LMS-in-Python
This Python program implements a complete Library Management System using object-oriented programming (OOP) concepts. Below is a detailed breakdown of each component:

## 1. Class Definition (`Library`)
The `Library` class serves as the core of our system, managing all book-related operations.

### 1.1 Constructor (`__init__` method)
```python
def __init__(self):
    self.books = {}  # Dictionary to store books (key: book_id, value: book details)
    self.load_books()  # Load existing books from file
```
- `self.books = {}`: Initializes an empty dictionary to store books.
- `self.load_books()`: Calls the method to load books from a file (`library.txt`).

### 1.2 `load_books()` Method
```python
def load_books(self):
    try:
        with open("library.txt", "r") as file:
            for line in file:
                book_id, title, author, status = line.strip().split(",")
                self.books[book_id] = {
                    "title": title,
                    "author": author,
                    "status": status
                }
    except FileNotFoundError:
        open("library.txt", "w").close()  # Create file if it doesn't exist
```
- Purpose: Loads books from `library.txt` into `self.books`.
- How it works:
  - Opens `library.txt` in read mode.
  - Each line represents a book (format: `book_id,title,author,status`).
  - Splits each line into `book_id`, `title`, `author`, and `status`.
  - Stores them in `self.books` as a nested dictionary.
- If file doesn't exist (`FileNotFoundError`), creates an empty file.

### 1.3 `save_books()` Method
```python
def save_books(self):
    with open("library.txt", "w") as file:
        for book_id, details in self.books.items():
            file.write(f"{book_id},{details['title']},{details['author']},{details['status']}\n")
```
- Purpose: Saves the current state of `self.books` back to `library.txt`.
- How it works:
  - Opens `library.txt` in write mode (overwrites existing content).
  - Writes each book in the format:  
    `book_id,title,author,status\n`

### 1.4 `add_book()` Method
```python
def add_book(self):
    book_id = input("Enter book ID: ")
    if book_id in self.books:
        print("Book ID already exists!")
        return
        
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    
    self.books[book_id] = {
        "title": title,
        "author": author,
        "status": "Available"
    }
    self.save_books()
    print("Book added successfully!")
```
- Purpose: Adds a new book to the library.
- Steps:
  1. Takes `book_id` from user.
  2. Checks if `book_id` already exists.
  3. Takes `title` and `author` as input.
  4. Adds the book with status `"Available"`.
  5. Calls `save_books()` to update the file.

### 1.5 `borrow_book()` Method
```python
def borrow_book(self):
    book_id = input("Enter book ID to borrow: ")
    if book_id in self.books:
        if self.books[book_id]["status"] == "Available":
            self.books[book_id]["status"] = "Borrowed"
            self.save_books()
            print("Book borrowed successfully!")
        else:
            print("Book is not available!")
    else:
        print("Book not found!")
```
- Purpose: Allows a user to borrow a book.
- Steps:
  1. Takes `book_id` input.
  2. Checks if the book exists and is `"Available"`.
  3. Updates status to `"Borrowed"`.
  4. Calls `save_books()` to update the file.

### 1.6 `return_book()` Method
```python
def return_book(self):
    book_id = input("Enter book ID to return: ")
    if book_id in self.books:
        if self.books[book_id]["status"] == "Borrowed":
            self.books[book_id]["status"] = "Available"
            self.save_books()
            print("Book returned successfully!")
        else:
            print("This book wasn't borrowed!")
    else:
        print("Book not found!")
```
- Purpose: Allows a user to return a borrowed book.
- Steps:
  1. Takes `book_id` input.
  2. Checks if the book exists and was `"Borrowed"`.
  3. Updates status back to `"Available"`.
  4. Calls `save_books()` to update the file.

### 1.7 `display_books()` Method
```python
def display_books(self):
    print("\n===== LIBRARY BOOKS =====")
    print(f"{'ID':<10}{'Title':<25}{'Author':<20}{'Status':<15}")
    print("-" * 70)
    for book_id, details in self.books.items():
        print(f"{book_id:<10}{details['title']:<25}{details['author']:<20}{details['status']:<15}")
```
Purpose: Displays all books in a formatted table.
Formatting:
`:<10` → Left-aligns text in 10-character width.
`"-" * 70` → Prints a separator line.

## 2. `main()` Function (User Interface)
```python
def main():
    library = Library()  # Create Library object
    
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.borrow_book()
        elif choice == "3":
            library.return_book()
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice! Please try again.")
```
- Purpose: Provides a menu-driven interface.
- How it works:
  1. Creates a `Library` object.
  2. Displays a menu with options (1-5).
  3. Calls the respective method based on user input.
  4. Loops until the user chooses `5` (Exit).

## 3. Program Entry Point
```python
if __name__ == "__main__":
    main()
```
Purpose: Ensures `main()` runs only when the script is executed directly (not when imported as a module).
Best Practice: Used to make the script reusable.

## Key Features
✅ Persistent Storage (Saves books to `library.txt`)  
✅ User-Friendly Menu (Easy navigation)  
✅ Error Handling (Checks for existing books, availability)  
✅ Clean Output Formatting (Displays books in a table)  
