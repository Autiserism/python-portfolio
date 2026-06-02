'''Write a function called format_name that takes a full name string in any format and returns it properly formatted. It should:

Strip whitespace from both ends
Convert to title case
Split into first and last name
Return a dictionary with keys first and last

Test it with: names = ["  tyler smith  ", "JOHN DOE", "sarah CONNOR  "]
Loop through the list, pass each name into the function and print the result dictionary for each.'''

names = ["  tyler smith  ", "JOHN DOE", "sarah CONNOR  "]

def format_name(name):
        name = name.strip()
        name = name.lower()
        name = name.title()
        parts = name.split()
        first = parts[0]
        last = parts[1]
        dictionary = {'first': first, 'last': last}
        return dictionary

for name in names:
    print(format_name(name))

