contacts = {}

def add_contact(name, number):
    contacts[name] = number
    with open("contacts.txt", "a") as file:
        file.write(f"{name}: {number}\n")
    print("Contact added successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts available.")
    else:
        for name, number in contacts.items():
            print(f"{name} : {number}")

def search_contact(name):
    if name in contacts:
        print(f"Found → {name}: {contacts[name]}")
    else:
        print("Contact not found.")

# Example usage:
add_contact("Alice", "12345")
add_contact("Bob", "98765")
view_contacts()
search_contact("Alice")
