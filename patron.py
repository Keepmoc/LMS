# -*- coding: utf-8 -*-

class Patron:
    patrons = {} # Dictionary for storing all patron information
    
    def __init__(self, name, patron_id, contact_info):
        self.name = name
        self.patron_id = patron_id
        self.contact_info = contact_info
        
        # Add patron to the Patrons dictionary
        Patron.patrons[patron_id] = self
        
    def __str__(self):
        return f"Name: {self.name}, ID: {self.patron_id}, Contact Info: {self.contact_info}"

    @staticmethod
    def add_patron(name, patron_id, contact_info):
        if patron_id not in Patron.patrons:
            Patron(name, patron_id, contact_info)
        else:
            print(f"Patron with ID {patron_id} already exists.")
            
    @staticmethod
    def update_patron(patron_id, new_name=None, new_contact_info=None):
        if patron_id in Patron.patrons:
            patron = Patron.patrons[patron_id]
            if new_name:
                patron.name = new_name
            if new_contact_info:
                patron.contact_info = new_contact_info
            print(f"Patron with ID {patron_id} updated successfully.")
        else:
            print(f"Patron with ID {patron_id} does not exist.")
            
    @staticmethod
    def delete_patron(patron_id):
        if patron_id in Patron.patrons:
            del Patron.patrons[patron_id]
            print(f"Patron with ID {patron_id} deleted successfully.")
        else:
            print(f"Patron with ID {patron_id} does not exist.")
            
    @staticmethod
    def display_patron(patron_id):
        if patron_id in Patron.patrons:
            print(Patron.patrons[patron_id])
        else:
            print(f"Patron with ID {patron_id} does not exist.")