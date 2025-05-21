import os

contacts_file = "contacts.txt"

# Load Contacts from file
def load_contacts():
    contacts = {}

    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as file:
            for line in file:
                name, phone = line.strip().split(":")
                contacts[name] = phone

    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(contacts_file, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}:{phone}\n")

# Add a new contact
def add_contact(contacts):
    name = input("Enter Contact Name: ").strip().title()
    phone = input("Enter Phone Number: ").strip()

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = phone
        save_contacts(contacts)
        print("Contact Added Succcessfully!")

# View all contacts
def view_contact(contacts):
    if not contacts:
        print("No Contacts found!")
    else:
        print("\n---Contact List---")
        for name, phone in contacts.items():
            print(f"Name: {name}\nPhone Number: {phone}")

# Search for a contact
def search_contact(contacts):
    name = input("Enter Name to Search: ").strip().title()
    if(name in contacts):
        print(f"Contact Found: {name} -> {contacts[name]}")
    else:
        print("Contacts Not Found!")

# Update an existing contact
def update_contact(contacts):
    name = input("Enter Name to Update: ").strip().title()
    if(name in contacts):
        new_phone = input("Enter New Phone Number: ").strip()
        contacts[name] = new_phone
        save_contacts(contacts)
        print("Contact Updated Successfully!")
    else:
        print("Contact Not Found!")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter Name to Delete: ").strip().title()
    if(name in contacts):
        del contacts[name]
        save_contacts(contacts)
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found!")

# Menu function
def contact_book():
    contacts = load_contacts()

    while True:
        print("\n---Contact Book---")
        print("1- Add Contact")
        print("2- View Contact")
        print("3- Search Contact")
        print("4- Update Contact")
        print("5- Delete Contact")
        print("6- Exit")

        choice = int(input("Enter your choice (1-6): "))

        if(choice == 1):
            add_contact(contacts)
        elif(choice == 2):
            view_contact(contacts)
        elif(choice == 3):
            search_contact(contacts)
        elif(choice == 4):
            update_contact(contacts)
        elif(choice == 5):
            delete_contact(contacts)
        elif(choice == 6):
            print("Goodbye! Have a nice Day! \U0001F603")
        else:
            print("Invalid choice! Please enter a number between 1-6.")

# Menu
if __name__ == "__main__":
    contact_book()