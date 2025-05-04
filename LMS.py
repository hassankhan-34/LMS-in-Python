class Library:
    def __init__(self):
        self.books = {}
        self.load_books()

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
            # Create file if it doesn't exist
            open("library.txt", "w").close()

    def save_books(self):
        with open("library.txt", "w") as file:
            for book_id, details in self.books.items():
                file.write(f"{book_id},{details['title']},{details['author']},{details['status']}\n")

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

    def display_books(self):
        print("\n===== LIBRARY BOOKS =====")
        print(f"{'ID':<10}{'Title':<25}{'Author':<20}{'Status':<15}")
        print("-" * 70)
        for book_id, details in self.books.items():
            print(f"{book_id:<10}{details['title']:<25}{details['author']:<20}{details['status']:<15}")

def main():
    library = Library()
    
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

if __name__ == "__main__":
    main()