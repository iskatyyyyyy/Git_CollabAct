class Contact:
    def __init__(self, name, sec, num, email, address):
        self.name = name
        self.num = num
        self.sec = sec
        self.email = email
        self.address = address

    def __str__(self):
        return f"NAME: {self.name}, Phone: {self.phone}, Section: {self.sec}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []
    def addcontact(self, contact):
        self.contacts.append(contact)
    def delcontact(self, name):
        for contact in self.contacts:
            self.contacts.remove(contact)
    def searchcontact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    def displaycontact(self):
        for contact in self.contacts:
            print(contact)

def getcontact():
    contact_book = ContactBook()
    name = input("Enter Name (Ex: Juan Dela Cruz): ")
    sec = input("Enter Course & Section (Ex: BSCS 2B): ")
    num = input("Enter Contact Number (Ex: 09123456789): ")
    email = input("Enter Email Address (Ex: yourname@email.com): ")
    address = input("Enter Home Address (Ex: Ermita, Manila): ")
    contact = Contact(name, sec, num, email, address)
    contact_book.addcontact(contact)

if __name__ == "__main__":
    contactbook = ContactBook()
    while True:
        print("[X] WELCOME TO MASTERCONTACT! [X]")
        print("(1) Add Contact")
        print("(2) Delete Contact")
        print("(3) Edit Contact")
        print("(4) Search Contact")
        print("(5) Display Contacts")
        print("(6) Exit")
        choice = input("Enter Number: ")

        if choice == "1":
            getcontact()
            print("Contact Inserted.")
        elif choice == "2":
            name = input("Enter Contact Name to Delete: ")
            contactbook.delcontact(name)
            print("Contact Deleted.")
        elif choice == "3":
            name = input("Enter Contact Name to Edit: ")
            # asdad
        elif choice == "4":
            name = input("Enter Contact Name to Search: ")
            contact = contactbook.searchcontact(name)
            if contact:
                print("Contact Searched!")
                print(contact)
            else:
                print("Invalid Contact.")
        elif choice == "5":
            print("Contact Book Information")
            contactbook.displaycontact()
        elif choice == "6":
            print("Thank You For Using MasterContact!")
            break




