import json

FILE_NAME = "contact.json"


def load_contacts():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def display_menu():
    print("\n---------- Contact Management System ----------")
    print("1). View Contacts")
    print("2). Add Contact")
    print("3). Search Contact")
    print("4). Delete Contact")
    print("5). Exit")


def view_contact():
    contacts = load_contacts()

    if not contacts:
        print("No Contact Available!")
        return

    print("\n----------- Contacts -----------")

    for idx, contact in enumerate(contacts, start=1):
        print(
            f"{idx}. Name: {contact['name']} \n "
            f"Phone: {contact['phone']} \n "
            f"Email: {contact['email']}"
        )


def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone number: ").strip()
    email = input("Enter contact email address: ").strip()

    if not name or not phone or not email:
        print("All fields are required!")
        return

    contact_info = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts = load_contacts()
    contacts.append(contact_info)
    save_contacts(contacts)

    print(f"Contact {name} added successfully!")


def search_contact():
    keyword = input(
        "Enter name, phone number, or email to search: "
    ).strip().lower()

    if not keyword:
        print("Search keyword cannot be empty!")
        return

    contacts = load_contacts()

    matching_contacts = [
        contact for contact in contacts
        if keyword in contact["name"].lower()
        or keyword in contact["phone"].lower()
        or keyword in contact["email"].lower()
    ]

    if matching_contacts:
        print("\n---------- Matching Contacts ----------")

        for idx, contact in enumerate(matching_contacts, start=1):
            print(
                f"{idx}. Name: {contact['name']} | "
                f"Phone: {contact['phone']} | "
                f"Email: {contact['email']}"
            )
    else:
        print("No matching contact found!")


def delete_contact():
    contacts = load_contacts()

    if not contacts:
        print("No Contact Available!")
        return

    print("\n----------- Contacts -----------")

    for idx, contact in enumerate(contacts, start=1):
        print(
            f"{idx}. Name: {contact['name']} | "
            f"Phone: {contact['phone']} | "
            f"Email: {contact['email']}"
        )

    try:
        serial_num = int(
            input("Enter the contact number to delete: ")
        )
    except ValueError:
        print("Please enter a valid number!")
        return

    if 1 <= serial_num <= len(contacts):
        deleted_contact = contacts.pop(serial_num - 1)
        save_contacts(contacts)

        print(
            f"Contact {deleted_contact['name']} "
            "deleted successfully!"
        )
    else:
        print("Invalid contact number. Try again!")
