<<<<<<< HEAD

import json
import os

from contact_manager import (
    display_menu,
    view_contact,
    add_contact,
    search_contact,
    delete_contact
)

FILE_NAME = "contact.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)


def main():
    while True:
        display_menu()
        user_choice = input("Enter a choice (1 - 5): ").strip()

        if user_choice == "1":
            view_contact()

        elif user_choice == "2":
            add_contact()

        elif user_choice == "3":
            search_contact()

        elif user_choice == "4":
            delete_contact()

        elif user_choice == "5":
            print("Exit the program!")
            break

        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
=======

import json
import os

from contact_manager import (
    display_menu,
    view_contact,
    add_contact,
    search_contact,
    delete_contact
)

FILE_NAME = "contact.json"

# Create JSON file if it does not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)


def main():
    while True:
        display_menu()
        user_choice = input("Enter a choice (1 - 5): ").strip()

        if user_choice == "1":
            view_contact()

        elif user_choice == "2":
            add_contact()

        elif user_choice == "3":
            search_contact()

        elif user_choice == "4":
            delete_contact()

        elif user_choice == "5":
            print("Exit the program!")
            break

        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
>>>>>>> e8d872a2170c95e87577429dbb85af0699410128
