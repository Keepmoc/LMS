# -*- coding: utf-8 -*-

from library import Library

class LibraryManagementSystem:
    
    def __init__(self, library):
        self.library = library
        self.user = None
    
    def run(self):
        while True:
            print("\n----- Login -----")
            account = input("\nEnter your account:")
            password = input("\nEnter your password:")
            
            self.login(account, password)
            
            if self.user:
                while True:
                    print("\n----- Library Management System -----")
                    print("1. Book Management")  
                    print("2. Patron Management")  
                    print("3. Search Book")
                    print("4. Search Patron")
                    print("5. Borrow Book")
                    print("6. Return Book")
                    print("7. Generate report")
                    print("8. User Management")
                    print("9. Quit")
                    
                    choice = input("\nEnter your choice:")
                    
                    if choice == "1":
                        self.book_management()
                    elif choice == "2":
                        self.patron_management()
                    elif choice == "3":
                        self.search_book()
                    elif choice == "4":
                        self.search_patron()
                    elif choice == "5":
                        self.borrow_book()
                    elif choice == "6":
                        self.return_book()
                    elif choice == "7":
                        self.generate_report()
                    elif choice == "8":
                         self.user_Management()
                    elif choice == "9":
                        print("\nExiting the system...")
                        self.save_data()
                        break
                    else:
                        print("\nInvalid choice, Please try again.")
            else:
                print("\nInput error, Please try again.")                      
        
    def login(self, account, password):
        self.user = self.library.login(account, password)
    
    def book_management(self):
        while True:
            print("\n----- Book management -----")
            print("1. Add Book")  
            print("2. Update Book")  
            print("3. Delete Book")
            print("4. Search Book")
            print("5. Quit")
            
            choice = input("\nEnter your choice:")
            
            if choice == "1":
                title = input("Please enter book title: ")
                author = input("Please enter book author: ")
                isbn = input("Please enter book ISBN: ")
                quantity = input("Please enter book quantity: ")
                self.library.add_book(title, author, isbn, quantity)
                
            elif choice == "2":
                isbn = input("Please enter book ISBN: ")
                title = input("Please enter book title: ")
                author = input("Please enter book author: ")
                quantity = input("Please enter book quantity: ")
                self.library.update_book(isbn, title, author, quantity)
                
            elif choice == "3":
                isbn = input("Please enter book ISBN: ")
                self.library.delete_book(isbn)
           
            elif choice == "4":
                self.search_book()
                
            elif choice == "5":
                print("\nBack to main menu...")
                self.save_data()
                break
            else:
                print("\nInvalid choice, Please try again.")
    
    def patron_management(self):
        while True:
            print("\n----- Patron management -----")
            print("1. Add Patron")  
            print("2. Update Patron")  
            print("3. Delete Patron")
            print("4. Search Patron")
            print("5. Quit")
            
            choice = input("\nEnter your choice:")
            
            if choice == "1":
                name = input("Please enter patron name: ")
                patron_id = input("Please enter patron Id: ")
                contact_info = input("Please enter patron contact information: ")
                self.library.add_patron(name, patron_id, contact_info)
                
            elif choice == "2":
                patron_id = input("Please enter patron Id: ")
                name = input("Please enter patron name: ")
                contact_info = input("Please enter patron contact information: ")
                self.library.update_patron(patron_id, name, contact_info)
                
            elif choice == "3":
                patron_id = input("Please enter patron Id: ")
                self.library.delete_patron()
            
            elif choice == "4":
                self.search_patron()
            
            elif choice == "5":
                print("\nBack to main menu...")
                self.save_data()
                break
            else:
                print("\nInvalid choice, Please try again.")
    
    def search_book(self):
        keyword = input("Please enter a keyword: ")
        self.library.search_book(keyword)
    
    def search_patron(self):
        keyword = input("Please enter a keyword: ")
        self.library.search_patron(keyword)
    
    def borrow_book(self):
        isbn = input("Please enter book ISBN: ")
        patron_id = input("Please enter patron Id: ")
        self.library.borrow_book(isbn, patron_id)
    
    def return_book(self):
        isbn = input("Please enter book ISBN: ")
        patron_id = input("Please enter patron Id: ")
        self.library.return_book(isbn, patron_id)
    
    def user_Management(self):
        if self.user.role != "Administrator":
            print("\nAccount not authorized")
            return
        else:
            while True:
                print("\n----- User management -----")
                print("1. Add Book")  
                print("2. Delete Book")
                print("3. Quit")
                
                choice = input("\nEnter your choice:")
                
                if choice == "1":
                    account = input("Please enter user account: ")
                    password = input("Please enter user password: ")
                    role = input("Please enter user role (Administrator or User): ")
                    self.library.add_user(account, password, role)
                    
                elif choice == "2":
                    account = input("Please enter user account: ")
                    password = input("Please enter user password: ")
                    self.library.delete_user(account, password)
                    
                elif choice == "3":
                    print("\nBack to main menu...")
                    self.save_data()
                    break
                else:
                    print("\nInvalid choice, Please try again.")
    
    def generate_report(self):
        self.library.generate_report()
    
    def save_data(self):
        self.library.save_data()
    
if __name__ == '__main__':
    library = Library()
    cli = LibraryManagementSystem(library)
    cli.run()