'''
Build a contact book with a menu loop.
Options: add contact, find contact, delete contact, view all, quit.
Store contacts as a dictionary with name as key and phone number as value.
'''

# define add_contact(contacts)
#   ask for name, convert to title case
#   ask for phone number
#   if name in contacts print 'already exists'
#   else contacts[name] = number, print confirmation

# define find_contact(contacts)
#   ask for name, convert to title case
#   if name in contacts print name and number
#   else print 'not found'

# define delete_contact(contacts)
#   ask for name, convert to title case
#   if name in contacts del contacts[name], print confirmation
#   else print 'not found'

# define view_all(contacts)
#   if contacts is empty print 'no contacts'
#   else loop through items printing name and number

# contacts = {}
# while True loop
#   print menu options
#   get choice
#   call matching function
#   if quit break


def add_contact(contacts):
    name = input('Enter a name: ').title()
    if name not in contacts:
        number = input('Enter their number: ')
        contacts[name] = number
        print(f'{name} was added to contacts')
    else:
        print('Already exists')

def find_contact(contacts):
    name = input('Type in their name: ').title()
    if name in contacts:
        print(f'{name}: {contacts[name]}')
    else:
        print('Not Found')

def delete_contact(contacts):
    print(contacts)
    name = input('What contact to delete: ').title()
    if name in contacts:
        del contacts[name]
        print(f'{name} has been deleted')
    else:
        print('not found')
def view_all(contacts):
    if not contacts:
       print('No contacts')
    else:
        for name ,number in contacts.items():
            print(f'{name}, {number}')

contacts = {}

while True:
    print("""\nContacts
1 Add a contact
2 Remove a contact
3 View contacts
4 Find contact
9 To Quit\n""")

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print('Enter a valid number')
        continue

    if choice == 1:
        add_contact(contacts)
    elif choice == 2:
        delete_contact(contacts)
    elif choice == 3:
        view_all(contacts)
    elif choice == 4:
        find_contact(contacts)
    elif choice == 9:
        break
    else:
        print('Enter a valid input')




