
from datetime import datetime, timedelta
from book import Book
from patron import Patron

class Transaction:
    records = {} # Store borrowing records
    fines = {} # Store fines records
    
    def __init__(self, transaction_id, isbn, patron_id, loan_start_date, expiry_date):
        self.transaction_id = transaction_id
        self.isbn = isbn
        self.patron_id = patron_id
        self.loan_start_date = loan_start_date
        self.expiry_date = expiry_date
        
        # Add transaction to the record dictionary
        Transaction.records[transaction_id] = self
    
    @staticmethod
    def add_transaction(transaction_id, isbn, patron_id, loan_start_date, expiry_date):
        Transaction(transaction_id, isbn, patron_id, loan_start_date, expiry_date)
    
    @staticmethod
    def check_out_book(isbn, patron_id, duration=3):
        if isbn not in Book.books:
            print(f"Book with ISBN {isbn} does not exist.")
        else:
            book = Book.books[isbn]
            if book.quantity < 1 :
                print(f"All the books with ISBN {isbn} have been checked out.")
            else:
                transaction_id = f"{isbn}_{patron_id}"
                if transaction_id in Transaction.records:
                    print(f"{patron_id} has checked out the book with ISBN {isbn}.")
                else:
                    Book.update_book(isbn, new_quantity=book.quantity-1)
                    current_date = datetime.now().date()
                    expiry_date = current_date + timedelta(days=duration)
                    Transaction(f"{isbn}_{patron_id}", isbn, patron_id, current_date.strftime("%Y-%m-%d"), expiry_date.strftime("%Y-%m-%d"))
                    print(f"Book with ISBN {isbn} has been checked out by {patron_id} with an expiry date of {expiry_date}.")
        
               
    @staticmethod
    def return_book(isbn, patron_id):
        transaction_id = f"{isbn}_{patron_id}"
        if transaction_id not in Transaction.records:
            print(f"Book with ISBN {isbn} is not borrowed by {patron_id}")
        else:
            transaction = Transaction.records[transaction_id]
            current_date = datetime.now().date()
            expiry_date = datetime.strptime(transaction.expiry_date,"%Y-%m-%d").date()
            if current_date > expiry_date:
                fines = Transaction.calculate_fines(expiry_date, current_date)
                if patron_id in Transaction.fines:
                    Transaction.fines[patron_id] += fines
                else:
                    Transaction.fines[patron_id] = fines
                
                book = Book.books[isbn]
                Book.update_book(isbn, new_quantity=book.quantity+1)
                del Transaction.records[transaction_id]
                print(f"Book with ISBn {isbn} has been returned with a fines of ${fines}. (The fines is $1 per day)")
            else:
                book = Book.books[isbn]
                Book.update_book(isbn, new_quantity=book.quantity+1)
                del Transaction.records[transaction_id]
                print(f"Book with ISBn {isbn} has been returned on time.")
            
    @staticmethod
    def calculate_fines(expiry_date, current_date):
        late_days = (current_date - expiry_date).days
        fines_per_day = 1 # Let's say the fine is $1 per day
        return late_days*fines_per_day
