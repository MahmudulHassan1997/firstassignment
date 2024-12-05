def view_all_contacs(all_contacs):
    if all_contacs != []:
        for contact in all_contacs:
            print(f"Name: {contact['name']} | Number: {contact['number']} | Email: {contact['email']}")
    else:
        print("No Contact found in CBM")