class Book:
    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return f"""Title: {self.title}
Author: {self.author}
isbn: {self.isbn}
Is available?: {self.is_available}"""
    
    