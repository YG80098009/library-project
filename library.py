class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def validate_user_book(self, user_id, book_isbn):
        is_user = False
        is_book = False
        for user in self.list_of_users:
            if user.id == user_id:
                user1 = user
                is_user =True
        for book in self.list_of_books:
            if book.isbn == book_isbn:
                is_book = True
                book1 = book
        if is_book and is_user:
            return True, user1, book1
        else:
            return (False)



    def borrow_book(self, user_id, book_isbn):
        data_from_validation = self.validate_user_book(user_id, book_isbn)
        if data_from_validation[0]:
            data_from_validation[1].borrow_books.append(data_from_validation[2])
            data_from_validation[2].is_available =False
            print("borrow succesfully")
        else:
            print(f"there is no book or user")

    