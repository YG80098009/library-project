import json
from book import Book
class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []
        
    def add_book(self,book):
        self.list_of_books.append(book)

    # def write_to_json(self):
    #     with open("data.json","w") as f:
    #         json.dump(self.list_of_books , f)



    def add_user(self,user):
        self.list_of_users.append(user)


    def find_book_by_isbn(self,book_isbn):
        for book in self.list_of_books:
            if book.isbn == book_isbn:
                return book
        print("book not exist")
        return False

    def find_user_by_id(self,user_id):
        for user in self.list_of_users:
            if user.id == user_id:
                return user
        print("user not exist")
        return False


    def borrow_book(self, user_id, book_isbn):
        is_book_exist = self.find_book_by_isbn(book_isbn)
        is_user_exist = self.find_user_by_id(user_id)
        if is_book_exist and is_user_exist:
            is_user_exist.borrow_books.append(is_user_exist)
            is_book_exist.is_available = False
            print("borrow successfully")
        else:
            print(f"there is no book or user")

    def return_book(self, user_id, book_isbn):
        is_book_exist = self.find_book_by_isbn(book_isbn)
        is_user_exist = self.find_user_by_id(user_id)
        if is_book_exist and is_user_exist:
            is_user_exist.borrow_books.remove(is_user_exist)
            is_book_exist.is_available = True
            print("return successfully")
        else:
            print(f"there is no book or user")


    def list_available_books(self):
        available_books = []
        for book in self.list_of_books:
            if book.is_available:
                available_books.append(book)
            return available_books
                

    def search_book(self,title,author):
        for book in self.list_of_books:
            if book.title == title:
                return book
            elif book.author == author:
                return book
            else:
                print("not found")
