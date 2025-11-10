class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self,book):
        self.list_of_books.append(book)

    def add_user(self,user):
        self.list_of_users.append(user)

    def list_available_books(self):
        return self.list_of_books

