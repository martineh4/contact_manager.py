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
    print(f"Added {name} to contacts.")

def find_contact(name):
    """Find and print a contact's phone number."""
    try:
        print(contacts[name])
    except KeyError:
        print("Contact not found.")

def delete_contact(name):
    """Delete a contact if it exists."""
    try:
        del contacts[name]
        print(f"Deleted {name}.")
    except KeyError:
        print("Contact not found.")

def main():
    """Main loop for the conact manager."""
    while True:
        # Dispplay menu options
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
                add_contact(name, phone)
            except DuplicateContactError as e:
                print(e)
        elif choice == 2:
            name = input("Enter name to find: ")
            find_contact(name)
        elif choice == 3:
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == 4:
            print("Exiting contact manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    main()

