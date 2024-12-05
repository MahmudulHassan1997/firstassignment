#Contact Book Management System

import add_contacts
import view_all_contacts

all_contacs = []

while True:
    print("Contact Book Management System")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Remove a contact information")
    print("4. Update a contact information")

    menu = input("Select an Option: ")

    if menu == "0":
        print("Thanks for using Contact book Management System ")
        break
    elif menu == "1":
        all_contacs = add_contacts.add_contacts(all_contacs)
    elif menu == "2":
        view_all_contacts.view_all_contacs(all_contacs)
    elif menu == "3":
        all_contacs.remove(add_contacts)
        print("Contact remove successfully! ")
    else:
        print("Choose a valid option!! ")


