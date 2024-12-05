from save_all_contacts import save_all_contacts


def add_contacts(all_contacs):
    name = input("Enter Contact name: ")
    number = int(input("Enter contact number: "))
    email = input("Enter email address: ")

    contact = {
        "name": name,
        "number": number,
        "email": email,
    }

    all_contacs.append(contact)
    save_all_contacts(all_contacs)

    print("Contuct Number Added Successully")

    return all_contacs
