'''
W3P5 — Mini Address Book W3P5_address_book.py
Full address book program.
Store name, phone, email and address for each contact.
Use regex to validate phone numbers and emails on entry.
Menu driven with add, find, edit, delete, display all. Log all changes.
'''

import re , logging
logging.basicConfig(level=logging.DEBUG)

contacts = [
    {"name": "John Smith", "phone": "416-555-1234", "email": "john@email.com","address": "123 Main St, Toronto, ON, M5V 3A8" },
    {"name": "Jane Doe", "phone": "647-555-5678", "email": "jane@test.com","address":"321 Side St, Toronto, ON, M3V 2A9"},
    {"name": "Bob Girard", "phone": "519-555-9999", "email": "bob@email.com","address":"333 Div St, Pearly-Gates, HV, G0D 1S1"}
]

patternFN = re.compile(r'^[A-Za-z-]+(?:\s[A-Z]\.?)?\s[A-Za-z-]+$')
patternPN = re.compile(r'^(?:\+?1[\s\-\.]?)?(\(?\d{3}\)?)?[\s\-\.]?(\d{3})[\s\-\.]?(\d{4})$')
patternEM = re.compile(r'^[\w._-]+@[\w.-]+\.[a-zA-Z]{2,}$')

name_prompt = 'Enter your first and last name: '
name_error = 'Must include first and last name, letters only'
phone_prompt = 'Enter your phone number: '
phone_error = 'Must be format 555-555-5555'
email_prompt = 'Enter your email address: '
email_error = 'Must include @ and domain like .com'

address_checks = [
    (r'\d+\s[\w\s]+',"Street Address (e.g. 123 Main St): "),
    (r'^[A-Za-z]+$',"City: "),
    (r'^[A-Za-z]{2}$',"Province (e.g. ON): "),
    (r'^[A-Za-z]\d[A-Za-z][\s.-]?\d[A-Za-z]\d$', "Postal Code (e.g. A1A 1A1): ")
]

def clean_phone(phone_num):
    cleaned = re.sub(r'\D', '', phone_num)
    pattern = re.compile(r'^(\d{3})(\d{3})(\d{4})$')
    match = pattern.search(cleaned)
    area, prefix, suffix = match.groups()
    return (f"{area}-{prefix}-{suffix}")

def validate_address():
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
    while True:
        value = input(prompt).strip()
        if re.fullmatch(pattern, value):
            return value
        print(f'Invalid: {error_message}')

def add_contact():
    full_name = get_valid_input(name_prompt, patternFN, name_error)
    phone_num = get_valid_input(phone_prompt, patternPN, phone_error)
    email = get_valid_input(email_prompt, patternEM, email_error)
    address = validate_address()
    cleanPN = clean_phone(phone_num)
    contact = {
        'name': full_name.title(),
        'phone': cleanPN,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print('\nContact Added successfully!')
    logging.debug(f"{full_name} added to contacts")
    return contact

def list_contacts():
    print('\nAll Contacts:')
    for name in contacts:
        for field, value in name.items():
            print(f'  {field.title()}: {value}')
        print("\n")

def search_contacts():
    results = []
    query = str(input("Enter contact information: "))
    for contact in contacts:
        for value in contact.values():
            if re.search(query, str(value), re.IGNORECASE | re.DOTALL):
                results.append(contact)
                break
    return results if results else None

def display_contact():
    picked = str(input("Enter the contact's name: ")).title()
    results = []
    for contact in contacts:
        for value in contact.values():
            if re.search(picked, str(value), re.IGNORECASE | re.DOTALL):
                results.append(contact)
                break
    if results:
        for contact in results:
            for field, value in contact.items():
                print(f'  {field.title()}: {value}')
    else:
        print("Not found.")
    return

def delete_contact():
    print("Search for the contact to remove:")
    picked = search_contacts()
    if picked:
        for contact in picked:
            contacts.remove(contact)
        print("Contact deleted.")
        logging.debug(f"{contact['name']} removed")
    else:
        print("Not found.")

field_validators = {
    'name':    (patternFN, name_prompt,  name_error),
    'phone':   (patternPN, phone_prompt, phone_error),
    'email':   (patternEM, email_prompt, email_error),
    'address': None
}

def edit_contact():
    print("Search for the contact to edit:")
    picked = search_contacts()
    if not picked:
        print("Not found.")
        return
    contact = picked[0]
    fields = list(contact.keys())
    for i, field in enumerate(fields, 1):
        print(f"  {i}. {field.title()}: {contact[field]}")
    try:
        choice = int(input("Enter the field number to edit: ")) - 1
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
        new_value = get_valid_input(f"Update {selected_field.title()} to: ", pattern, error)
        if selected_field == 'phone':
            new_value = clean_phone(new_value)
    else:
        new_value = input(f"Update {selected_field.title()} to: ").strip()
    contact[selected_field] = new_value
    print(f"{selected_field.title()} updated successfully.")
    logging.debug(f"{contact['name']} - {selected_field} updated")

while True:
    try:
        choice = int(input("""Contacts Book
    would you like to
    1 Add Contact
    2 Edit Contact
    3 Delete A Contact
    4 View All Contacts
    5 Find A Contact
    9 quit
    """))
        if choice == 1:
            add_contact()
            continue
        elif choice == 2:
            edit_contact()
            continue
        elif choice == 3:
            delete_contact()
            continue
        elif choice == 4:
            list_contacts()
            continue
        elif choice == 5:
            display_contact()
            continue
        elif choice == 9:
            print("=========")
            break
        else:
            print("numbers are hard")
            continue
    except ValueError:
        print("if only you could count")
        continue

logging.disable(logging.CRITICAL)


















