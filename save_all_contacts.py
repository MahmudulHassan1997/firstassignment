def save_all_contacts(all_contacs):
    with open("all_contacs.cvs", "w") as cbm:
        for contact in all_contacs:
            cline = f"Name: {contact['name']} | Number: {contact['number']} | Email: {contact['email']}\n"
            cbm.write(cline)