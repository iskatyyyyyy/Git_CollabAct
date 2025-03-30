import json

# File handling functions
def load_contacts(filename="contacts.json"):
    """Load contacts from a file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts, filename="contacts.json"):
    """Save contacts to a file."""
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

# Core functionalities
contacts = load_contacts()

def add_contact(name, contact, email):
    """Add a new contact."""
    contacts[name] = {"contact": contact, "email": email}
    save_contacts(contacts)

def delete_contact(name):
    """Delete a contact by name."""
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)

#Added a feature where the user can update the existing record of contacts.

def update_contact(name, new_contact, new_email):
    """Update an existing contact."""
    if name in contacts:
        contacts[name] = {"contact": new_contact, "email": new_email}
        save_contacts(contacts)

def display_contacts():
    """Display all contacts."""
    print(json.dumps(contacts, indent=4) if contacts else "No contacts available.")

if __name__ == "__main__":
    while True:
        choice = input("\n1.Add 2.Update 3.Delete 4.View 5.Exit\nChoice: ")
        if choice == '1':
            add_contact(input("Name: "), input("Contact: "), input("Email: "))
        elif choice == '2':
            update_contact(input("Name: "), input("New Contact: "), input("New Email: "))
        elif choice == '3':
            delete_contact(input("Name to delete: "))
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")
