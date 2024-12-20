from models.author import Author
from models.book import Book




Author.create_table()
Book.create_table()


def main():
    while True:
        display_main_menu()
        choice = input("> ")
        if choice == "1":
            exit_program()
        elif choice == "2":
            handle_authors()
        elif choice == "3":
            handle_books()
        else:
            print("Invalid choice! Please try again.")


def display_main_menu():
    print("\n--- Library Management System ---")
    print("1. Exit")
    print("2. Manage Authors")
    print("3. Manage Books")
    print("\nPlease choose an option:")


def exit_program():
    print("Exiting the program. Goodbye!")
    exit()


def handle_authors():
    while True:
        display_author_menu()
        choice = input("> ")
        if choice == "1":
            add_author()
        elif choice == "2":
            list_authors()
        elif choice == "3":
            delete_author()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")


def display_author_menu():
    print("\n--- Manage Authors ---")
    print("1. Add Author")
    print("2. List All Authors")
    print("3. Delete Author")
    print("4. Back to Main Menu")


def add_author():
    name = input("Enter the author's name: ")
    Author.create(name)
    print(f"Author '{name}' added successfully!")


def list_authors():
    authors = Author.get_all()
    if authors:
        for author in authors:
            print(author.show())
    else:
        print("No authors found in the system.")


def delete_author():
    try:
        author_id = int(input("Enter the author ID to delete: "))
        Author.delete(author_id)
        print(f"Author with ID {author_id} deleted successfully.")
    except ValueError:
        print("Invalid ID. Please enter a number.")


def handle_books():
    while True:
        display_book_menu()
        choice = input("> ")
        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            view_books_by_author()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")


def display_book_menu():
    print("\n--- Manage Books ---")
    print("1. Add Book")
    print("2. List All Books")
    print("3. Delete Book")
    print("4. View Books by Author")
    print("5. Back to Main Menu")


def add_book():
    try:
        title = input("Enter book title: ")
        author_id = int(input("Enter author ID: "))
        publisher = input("Enter publisher: ")
        year = int(input("Enter year of publication: "))
        Book.create(title, author_id, publisher, year)
        print(f"Book '{title}' added successfully!")
    except ValueError:
        print("Invalid input. Please ensure author ID and year are numbers.")


def list_books():
    books = Book.get_all()
    if books:
        for book in books:
            print(book.show())
    else:
        print("No books found in the system.")


def delete_book():
    try:
        book_id = int(input("Enter the book ID to delete: "))
        Book.delete(book_id)
        print(f"Book with ID {book_id} deleted successfully.")
    except ValueError:
        print("Invalid ID. Please enter a number.")


def view_books_by_author():
    try:
        author_id = int(input("Enter the author ID to view their books: "))
        books = Book.get_books_by_author(author_id)
        if books:
            for book in books:
                print(book.show())
        else:
            print("No books found for this author.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()