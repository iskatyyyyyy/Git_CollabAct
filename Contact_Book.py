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
    print(f"\nContact '{name}' added successfully.")

def delete_contact(name):
    """Delete a contact by name."""
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"\nContact '{name}' deleted successfully.")
    else:
        print(f"\nContact '{name}' not found.")

def update_contact(name, new_contact, new_email):
    """Update an existing contact."""
    if name in contacts:
#Added a feature where the program will ask for clarification regarding the updates made.
        print(f"\nCurrent Contact Info - Name: {name}, Contact: {contacts[name]['contact']}, Email: {contacts[name]['email']}")
        confirmation = input("Are you sure you want to update this contact? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            contacts[name] = {"contact": new_contact, "email": new_email}
            save_contacts(contacts)
            print(f"\nContact '{name}' updated successfully.")
        else:
            print("\nUpdate canceled.")
    else:
        print(f"\nContact '{name}' not found.")

def display_contacts():
    """Display all contacts."""
    if not contacts:
        print("\nNo contacts available.")
        return
    
    print("\nContact List")
    print("=" * 45)
    print(f"{'Name':<20}{'Contact':<15}{'Email'}")
    print("-" * 45)
    
    for name, info in contacts.items():
        print(f"{name:<20}{info['contact']:<15}{info['email']}")

    print("=" * 45)

def show_menu():
    """Display the menu options."""
    print("\nContact Book")
    print("=" * 25)
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")
    print("=" * 25)

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("\nName: ").strip()
            contact = input("Contact: ").strip()
            email = input("Email: ").strip()
            add_contact(name, contact, email)

        elif choice == '2':
            name = input("\nName to update: ").strip()
            new_contact = input("New Contact: ").strip()
            new_email = input("New Email: ").strip()
            update_contact(name, new_contact, new_email)

        elif choice == '3':
            name = input("\nName to delete: ").strip()
            delete_contact(name)

        elif choice == '4':
            display_contacts()

        elif choice == '5':
            print("\nExiting Contact Book. Have a great day!\n")
            break

        else:
            print("\nInvalid choice! Please enter a number from 1 to 5.")
