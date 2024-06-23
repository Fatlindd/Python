import argparse
import json
import os

FILE_NAME = 'contacts.json'


def load_contacts(file_name=FILE_NAME):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return []


def save_contacts(contacts, file_name=FILE_NAME):
    with open(file_name, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(name, phone, email, file_name=FILE_NAME):
    contacts = load_contacts(file_name)
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts, file_name)
    print(f"Added contact: {name}")


def view_contacts(file_name=FILE_NAME):
    contacts = load_contacts(file_name)
    if not contacts:
        print("No contacts found.")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def search_contact(name, file_name=FILE_NAME):
    contacts = load_contacts(file_name)
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found contact: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
    print(f"No contact found with name: {name}")


def delete_contact(name, file_name=FILE_NAME):
    contacts = load_contacts(file_name)
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    save_contacts(contacts, file_name)
    print(f"Deleted contact: {name}")


def main():
    parser = argparse.ArgumentParser(description='Command-line Contact Book Application')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new contact')
    add_parser.add_argument('name', type=str, help='The contact name')
    add_parser.add_argument('phone', type=str, help='The contact phone number')
    add_parser.add_argument('email', type=str, help='The contact email address')

    view_parser = subparsers.add_parser('view', help='View all contacts')

    search_parser = subparsers.add_parser('search', help='Search for a contact by name')
    search_parser.add_argument('name', type=str, help='The name of the contact to search for')

    delete_parser = subparsers.add_parser('delete', help='Delete a contact by name')
    delete_parser.add_argument('name', type=str, help='The name of the contact to delete')

    args = parser.parse_args()

    if args.command == 'add':
        add_contact(args.name, args.phone, args.email)
    elif args.command == 'view':
        view_contacts()
    elif args.command == 'search':
        search_contact(args.name)
    elif args.command == 'delete':
        delete_contact(args.name)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()