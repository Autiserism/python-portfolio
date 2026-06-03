import re
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Load existing contacts
def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

contacts = load_contacts()

# Validation patterns
patternFN = re.compile(r'^[A-Za-z-]+(?:\s[A-Z]\.?)?\s[A-Za-z-]+$')
patternPN = re.compile(r'^(?:\+?1[\s\-\.]?)?(\(?\d{3}\)?)?[\s\-\.]?(\d{3})[\s\-\.]?(\d{4})$')
patternEM = re.compile(r'^[\w._-]+@[\w.-]+\.[a-zA-Z]{2,}$')

# Prompts and errors
name_prompt = 'Enter first and last name: '
name_error = 'Must include first and last name, letters only'
phone_prompt = 'Enter phone number: '
phone_error = 'Must be format 555-555-5555'
email_prompt = 'Enter email address: '
email_error = 'Must include @ and domain like .com'

# Address validation
address_checks = [
    (r'^\d+\s+[\w\s]+$', "Street Address (e.g. 123 Main St): "),
    (r'^[A-Za-z\s]+$', "City: "),
    (r'^[A-Z]{2}$', "Province (e.g. ON): "),
    (r'^[A-Za-z]\d[A-Za-z][\s.-]?\d[A-Za-z]\d$', "Postal Code (e.g. A1A 1A1): ")
]

field_validators = {
    'name':    (patternFN, name_prompt,  name_error),
    'phone':   (patternPN, phone_prompt, phone_error),
    'email':   (patternEM, email_prompt, email_error),
    'address': None
}

def clean_phone(phone_num):
    """Normalize phone to XXX-XXX-XXXX format"""
    cleaned = re.sub(r'\D', '', phone_num)
    pattern = re.compile(r'^(\d{3})(\d{3})(\d{4})$')
    match = pattern.search(cleaned)
    if match:
        area, prefix, suffix = match.groups()
        return f"{area}-{prefix}-{suffix}"
    return cleaned

def validate_address():
    """Validate and build address from components"""
    address = []
    for check, prompt in address_checks:
        while True:
            value = input(prompt).strip()
            if re.search(check, value):
                address.append(value)
                break
            else:
                print("Invalid format, please try again.")
    return ', '.join(address)

def get_valid_input(prompt, pattern, error_message):
    """Get validated input from user"""
    while True:
        value = input(prompt).strip()
        if re.fullmatch(pattern, value):
            return value
        print(f'Invalid: {error_message}')

def add_contact():
    """Add new contact with validation"""
    print("\n--- Add New Contact ---")
    full_name = get_valid_input(name_prompt, patternFN, name_error)
    phone_num = get_valid_input(phone_prompt, patternPN, phone_error)
    email = get_valid_input(email_prompt, patternEM, email_error)
    address = validate_address()

    contact = {
        'name': full_name.title(),
        'phone': clean_phone(phone_num),
        'email': email,
        'address': address
    }

    contacts.append(contact)
    print('\n✓ Contact added successfully!')
    logging.info(f"Added contact: {full_name}")
    return contact

def list_contacts():
    """Display all contacts"""
    if not contacts:
        print("\nNo contacts found.")
        return

    print('\n' + '=' * 60)
    print(f'ALL CONTACTS ({len(contacts)} total)')
    print('=' * 60)

    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. {contact['name']}")
        print(f"   Phone:   {contact['phone']}")
        print(f"   Email:   {contact['email']}")
        print(f"   Address: {contact['address']}")

def search_contacts():
    """Search contacts by any field"""
    query = input("Enter search term: ").strip()
    if not query:
        return None

    results = []
    for contact in contacts:
        for value in contact.values():
            if re.search(query, str(value), re.IGNORECASE):
                results.append(contact)
                break

    return results if results else None

def display_contact():
    """Search and display matching contacts"""
    print("\n--- Search Contacts ---")
    results = search_contacts()

    if results:
        print(f"\nFound {len(results)} contact(s):")
        for contact in results:
            print(f"\n--- {contact['name']} ---")
            for field, value in contact.items():
                print(f"  {field.title()}: {value}")
    else:
        print("\nNo contacts found.")

def delete_contact():
    """Delete a contact after search"""
    print("\n--- Delete Contact ---")
    results = search_contacts()

    if not results:
        print("\nNo contacts found.")
        return

    if len(results) > 1:
        print(f"\nFound {len(results)} contacts:")
        for i, contact in enumerate(results, 1):
            print(f"  {i}. {contact['name']} - {contact['phone']}")

        try:
            choice = int(input("Select contact to delete: ")) - 1
            contact = results[choice]
        except (ValueError, IndexError):
            print("Invalid choice.")
            return
    else:
        contact = results[0]

    confirm = input(f"Delete {contact['name']}? (yes/no): ").lower()
    if confirm == 'yes':
        contacts.remove(contact)
        print(f"\n✓ {contact['name']} deleted.")
        logging.info(f"Deleted contact: {contact['name']}")
    else:
        print("Deletion cancelled.")

def edit_contact():
    """Edit an existing contact"""
    print("\n--- Edit Contact ---")
    results = search_contacts()

    if not results:
        print("\nNo contacts found.")
        return

    if len(results) > 1:
        print(f"\nFound {len(results)} contacts:")
        for i, contact in enumerate(results, 1):
            print(f"  {i}. {contact['name']} - {contact['phone']}")

        try:
            choice = int(input("Select contact to edit: ")) - 1
            contact = results[choice]
        except (ValueError, IndexError):
            print("Invalid choice.")
            return
    else:
        contact = results[0]

    print(f"\nEditing: {contact['name']}")
    fields = list(contact.keys())
    for i, field in enumerate(fields, 1):
        print(f"  {i}. {field.title()}: {contact[field]}")

    try:
        choice = int(input("\nEnter field number to edit: ")) - 1
        if choice < 0 or choice >= len(fields):
            raise IndexError
        selected_field = fields[choice]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    if selected_field == 'address':
        new_value = validate_address()
    elif selected_field in field_validators:
        pattern, prompt, error = field_validators[selected_field]
        new_value = get_valid_input(f"New {selected_field}: ", pattern, error)
        if selected_field == 'phone':
            new_value = clean_phone(new_value)
        if selected_field == 'name':
            new_value = new_value.title()
    else:
        new_value = input(f"New {selected_field}: ").strip()

    contact[selected_field] = new_value
    print(f"\n✓ {selected_field.title()} updated!")
    logging.info(f"Updated {contact['name']}: {selected_field}")

def save_contacts():
    """Save contacts to JSON file"""
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f, indent=2)
    print("\n✓ Contacts saved to file!")
    logging.info("Contacts saved to file")

# Main menu
def main():
    while True:
        try:
            print("\n" + "=" * 40)
            print("📇 CONTACTS MANAGER")
            print("=" * 40)
            choice = int(input("""
1. Add Contact
2. Edit Contact
3. Delete Contact
4. View All Contacts
5. Search Contacts
6. Save to File
9. Quit

Enter choice: """))

            if choice == 1:
                add_contact()
            elif choice == 2:
                edit_contact()
            elif choice == 3:
                delete_contact()
            elif choice == 4:
                list_contacts()
            elif choice == 5:
                display_contact()
            elif choice == 6:
                save_contacts()
            elif choice == 9:
                save_contacts()  # Auto-save on exit
                print("\n👋 Goodbye!")
                break
            else:
                print("\n⚠️  Invalid choice. Try again.")

        except ValueError:
            print("\n⚠️  Please enter a number.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
