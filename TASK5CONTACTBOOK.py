class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\n--- Contacts ---")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        
        if not found_contacts:
            print("No matching contacts found.")
        else:
            print("\n--- Matching Contacts ---")
            for idx, contact in enumerate(found_contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Current details for '{contact.name}':")
                print(f"Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
                choice = input("Update (phone/email/address/all): ").lower()
                
                if choice == 'phone':
                    new_phone = input("Enter new phone number: ")
                    contact.phone_number = new_phone
                elif choice == 'email':
                    new_email = input("Enter new email address: ")
                    contact.email = new_email
                elif choice == 'address':
                    new_address = input("Enter new address: ")
                    contact.address = new_address
                elif choice == 'all':
                    new_phone = input("Enter new phone number: ")
                    new_email = input("Enter new email address: ")
                    new_address = input("Enter new address: ")
                    contact.phone_number = new_phone
                    contact.email = new_email
                    contact.address = new_address
                else:
                    print("Invalid choice.")
                print(f"Contact '{contact.name}' updated successfully!")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for idx, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[idx]
                print(f"Contact '{contact.name}' deleted successfully!")
                return
        print(f"Contact '{name}' not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")

            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)

        elif choice == '4':
            name = input("Enter name of contact to update: ")
            contact_book.update_contact(name)

        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
