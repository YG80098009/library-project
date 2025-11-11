class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []


    def find_user_by_id(self, user_id):
        for user in self.list_of_users:
            if user.id == user_id:
                return user
        print(f"the user does not exist")
        return False

    def find_book_by_isbn(self, book_isbn):
        for book in self.list_of_books:
            if book.isbn == book_isbn:
                return book
        print(f"the book does not exist")
        return False

    def borrow_book(self, user_id, book_isbn):
        is_user_exist = self.find_user_by_id(user_id)
        is_book_exist = self.find_book_by_isbn(book_isbn)
        if is_user_exist and is_book_exist:
            is_user_exist.borrow_books.append(is_book_exist)
            is_book_exist.is_available = False
            print("borrow successfully")
        else:
            print(f"there is no book or user")

    def return_book(self, user_id, book_isbn):
        is_user_exist = self.find_user_by_id(user_id)
        is_book_exist = self.find_book_by_isbn(book_isbn)
        if is_user_exist and is_book_exist:
            is_user_exist.borrow_books.remove(is_book_exist)
            is_book_exist.is_available = True
            print("return successfully")
        else:
            print(f"there is no book or user")