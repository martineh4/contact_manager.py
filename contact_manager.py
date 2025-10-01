# contact_manager.py

class DuplicateContactError(Exception):
    """Custom exception for duplicate contacts."""
    pass

contacts = {}

def add_contact(name, phone):
    """Add a new contact if it doesn't already exist."""
    if name in contacts:
        raise DuplicateContactError(f"Contact '{name}' already exists.")
    contacts[name] = phone
    return f"Added {name} to contacts."

def find_contact(name):
    """Return a contact's phone number, or None if not found."""
    return contacts.get(name, None)
    
def delete_contact(name):
    """Delete a contact if it exists."""
    if name in contacts:
        del contacts[name]
        return f"Deleted {name}."
    return None

def main():
    """Main loop for the contact manager."""
    while True:
        # Display menu options
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        # Get user choice and handle invalid input
        try:
            choice = int(input("Enter your choice: "))  
        except ValueError:
            print("Invalid input. Please enter a number between 1-4.")
            continue

        # Execute menu choice
        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            try:
                result = add_contact(name, phone)
                print(result)
            except DuplicateContactError as e:
                print(e)
        elif choice == 2:
            name = input("Enter name to find: ")
            result = find_contact(name)
            if result:
                print(f"Name: {name}\nPhone Number: {result}")
            else:
                print("Contact not found.")
        elif choice == 3:
            name = input("Enter name to delete: ")
            result = delete_contact(name)
            if result:
                print(result)
            else:
                print("Contact not found.")
        elif choice == 4:
            print("Exiting contact manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    main()



