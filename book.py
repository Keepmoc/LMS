class Book:
    books = {} # Dictionary for storing all book information
    
    def __init__(self, title, author, isbn, quantity=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        
        # Add books to the Books dictionary
        Book.books[isbn] = self
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity}" 
        
    @staticmethod
    def add_book(title, author, isbn, quantity=1):
        if isbn not in Book.books:
            Book(title, author, isbn, quantity)
        else:
            print(f"Book with ISBN {isbn} already exists. Updating quantity instead.")
            Book.books[isbn].quantity += quantity
            
    @staticmethod
    def update_book(isbn, new_title=None, new_author=None, new_quantity=None):
        if isbn in Book.books:
            book = Book.books[isbn]
            if new_title:
                book.title = new_title
            if new_author:
                book.author = new_author
            if new_quantity:
                book.quantity = new_quantity
            print(f"Book with ISBN {isbn} updated successfully.")
        else:
            print(f"Book with ISBN {isbn} does not exist.")
            
    @staticmethod
    def delete_book(isbn):
        if isbn in Book.books:
            del Book.books[isbn]
            print(f"Book with ISBN {isbn} deleted successfully.")
        else:
            print(f"Book with ISBN {isbn} does not exist.")
            
    @staticmethod
    def display_book(isbn):
        if isbn in Book.books:
            print(Book.books[isbn])
        else:
            print(f"Book with ISBN {isbn} does not exist.")