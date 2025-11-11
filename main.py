from user import User
from book import Book
from library import Library

l1 = Library()
def show_menu():
    while True:
        print("1. Add Book\n2. Add User\n3. Borrow Book\n4. Return_book\n5. List_available_books\n6. Search_book\n7. Save & Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title , author , isbn = input("title"),input("author"),input("isbn")
            book1 = Book(title,author,isbn)
            l1.add_book(book1)
            print("added successfully")

        elif choice == "2":
            name,id = input("name"),input("id")
            user1 = User(name,id)
            l1.add_user(user1)
            print("added successfully")

        if choice == "3":
            pass
        elif choice == "4":
            pass
        if choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            break
        else:
            print("Invalid choice, try again.")

show_menu()

