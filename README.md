## Contact Manager
A Python program that manages contacts, allowing users to:
- Add contacts with a name and phone number
- Find contacts
- Delete contacts
- Exit the program

## Unit Tests
Unit tests are included to ensure the following functions are working properly:
- Adding contacts
- Finding existing and non-existing contacts
- Deleting existing and non-existent contacts
- Preventing duplicate contacts

These tests can be run using **python -m unittest test_contact_manager.py**

## Bugs Fixed
- **Crash when inputting non-numeric values in the menu**
    - Now prompts user until valid input is received
- **Crash when finding non-existent contact**
    - Now returns 'None' and shows 'Contact not found.'
- **Crash when deleting non-existent contact**
    - Now returns 'None' and shows 'Contact not found.'
- **Adding duplicate contact overwrites old contact**
    - Now 'DuplicateContactError' is raised and prevents overwriting phone numbers

## How to Run
1. Ensure Python is installed on your device
2. Download or clone this project
3. Open the folder containing contact_manager.py in your terminal
4. Run the program by typing python contact_manager.py

## Code Walkthrough and Demonstration
https://www.loom.com/share/19f99590f8f64263becf589c18d632e2?sid=5ad0640d-c8c7-40cc-8e55-67ca0ebad3a6
