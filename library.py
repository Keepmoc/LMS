# -*- coding: utf-8 -*-

import csv
from book import Book
from patron import Patron
from transaction import Transaction
from user import User

class Library:
    
    def __init__(self):
        self.load_data()
    
    def add_book(self, title, author, isbn, quantity):
        Book.add_book(title, author, isbn)
    
    def update_book(self, isbn, new_title=None, new_author=None, new_quantity=None):
        Book.update_book(isbn, new_title, new_author, new_quantity)
    
    def delete_book(self, isbn):
        Book.delete_book(isbn)
    
    def search_book(self, keyword):
        result = []
        for isbn, book in Book.books.items():
            if keyword in book.title or keyword in book.author or keyword in book.isbn:
                result.append(book)
                
        if result:
            print(f"\nThe number of query results is {len(result)}: ")
            for book in result:
                print(f"{book} \n")
        else:
            print("No result")
    
    def add_patron(self, name, patron_id, contact_info):
        Patron.add_patron(name, patron_id, contact_info)
    
    def update_patron(self, patron_id, new_name=None, new_contact_info=None):
        Patron.update_patron(patron_id, new_name, new_contact_info)
    
    def delete_patron(self, patron_id):
        Patron.delete_patron(patron_id)
        
    def search_patron(self, keyword):
        result = []
        for patron_id, patron in Patron.patrons.items():
            if keyword in patron.name or keyword in patron.patron_id:
                result.append(patron)
        
        if result:
            print(f"\nThe number of query results is {len(result)}: ")
            for patron in result:
                print(f"{patron} \n")
        else:
            print("No result")

    def borrow_book(self, isbn, patron_id, duration=3):
        Transaction.check_out_book(isbn, patron_id, duration)
    
    def return_book(self, isbn, patron_id):
        Transaction.return_book(isbn, patron_id)
    
    def add_user(self, account, password, role):
        User.add_user(account, password, role)
        
    def delete_user(self, account, password):
        User.delete_user(account, password)
        
    def login(self, account, password):
        return User.login(account, password)
    
    def generate_report(self):
        book_len = len(Book.books)
        patron_len = len(Patron.patrons)
        transaction_len = len(Transaction.records)
        fines = 0
        for patron_id, value in Transaction.fines.items():
           fines += int(value)
        
        print("***** Statistical Report ****")
        print(f"The number of Books: {book_len}")
        print(f"the number of patrons: {patron_len}")
        print(f"The number of books currently on loan: {transaction_len}")
        print(f"The total overdue fines: {fines}")
        pass
    
    def save_data(self):
        book_path = 'database/book.csv'
        with open(book_path, 'w', newline='',encoding='utf-8') as csvfile:  
            fieldnames = ['Title', 'Author', 'ISBN', 'Quantity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for isbn, book in Book.books.items():
                writer.writerow({
                    'Title': book.title,  
                    'Author': book.author,  
                    'ISBN': book.isbn,  
                    'Quantity': book.quantity
                    })
        
        patron_path = 'database/patron.csv'
        with open(patron_path, 'w', newline='',encoding='utf-8') as csvfile:  
            fieldnames = ['Name', 'Id', 'Contact Information']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for patron_id, patron in Patron.patrons.items():
                writer.writerow({
                    'Name': patron.name,  
                    'Id': patron.patron_id,  
                    'Contact Information': patron.contact_info
                    })
        
        transaction_path = 'database/transaction.csv'
        with open(transaction_path, 'w', newline='',encoding='utf-8') as csvfile:  
            fieldnames = ['Id', 'ISBN', 'Patron', 'Loan_Start_Date', 'Expiry_Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for transaction_id, transaction in Transaction.records.items():
                writer.writerow({
                    'Id': transaction.transaction_id,  
                    'ISBN': transaction.isbn,  
                    'Patron': transaction.patron_id,
                    'Loan_Start_Date': transaction.loan_start_date,
                    'Expiry_Date': transaction.expiry_date
                    })
                
        transaction_path = 'database/fines.csv'
        with open(transaction_path, 'w', newline='',encoding='utf-8') as csvfile:  
            fieldnames = ['Id', 'fines']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for patron_id, fines in Transaction.fines.items():
                writer.writerow({
                    'Id': patron_id,  
                    'fines': fines
                    })
        
        user_path = 'database/user.csv'
        with open(user_path, 'w', newline='',encoding='utf-8') as csvfile:  
            fieldnames = ['Account', 'Password', 'Role']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for account, user in User.users.items():
                writer.writerow({
                    'Account': user.account,  
                    'Password': user.password,  
                    'Role': user.role
                    })
    
    def load_data(self):
        book_path = 'database/book.csv'
        with open(book_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Book.add_book(row['Title'], row['Author'], row['ISBN'], int(row['Quantity']))
        
        patron_path = 'database/patron.csv'
        with open(patron_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Patron.add_patron(row['Name'], row["Id"], row["Contact Information"])
        
        transaction_path = 'database/transaction.csv'
        with open(transaction_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Transaction.add_transaction(row['Id'], row["ISBN"], row["Patron"], row["Loan_Start_Date"], row["Expiry_Date"])
    
        transaction_path = 'database/fines.csv'
        with open(transaction_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Transaction.fines[row['Id']] = row['fines']
        
        user_path = 'database/user.csv'
        with open(user_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                User(row['Account'], row['Password'], row['Role'])
        
    
if __name__ == '__main__':
    library = Library()
    library.load_data()
    print(Book.books)
    print(Patron.patrons)
    print(Transaction.records)
    print(User.users)
    
    print(User.login("Administrator", "Administrator"))
    
    #library.add_book("title", "ww", "1400021", 2)
    library.search_book("t")
    
    #library.add_patron("joe", "140000", "15513568749")
    
    #library.borrow_book("1400021", "140000")
    #library.return_book("1400021", "140000")
    
    library.add_user("root", "root123", "User")
    
    print(Book.books)
    print(Patron.patrons)
    print(Transaction.records)
    print(Transaction.fines)
    print(User.users)
    
    library.generate_report()
    
    library.save_data()
    