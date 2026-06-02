# Write a program that uses a dictionary to store a simple phone book
# The keys are names and the values are phone numbers.
# Ask the user to enter a name, Use .get() to look up the number and print it
# If the name isn't found print "Contact not found"
# Then ask if they want to add a new contact,
# if yes ask for a name and number and add it to the dictionary
# Print the final phone book using a loop through .items()


contacts = {
    'Tyler': '555-1234',
    'Bob': '555-5678',
    'Sarah': '555-9012'}

while True:
    name = input('Enter a name or nothing to see all contacts: ')
    if name == '':
        break
    if name in contacts:
        print(name + ':' + contacts.get(name, 0))
    else:
        print('Contact not found ' + name)
        new_contact = input('would you like to add them as a new contact? yes or no ')
        if new_contact == ('yes'):
            new_contact_number = input('what is their phone number?: ')
            contacts.setdefault(name, new_contact_number)
        else:
            print('contact not added')

for name, number in contacts.items():
    print(name + ':', number)
