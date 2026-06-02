# Write a program that creates a dictionary called person
# with the following keys: name, age, city. Fill it with your own values. Then:
# Print the value of each key individually
# Add a new key called job with any value
# Delete the city key
# Print the final dictionary

import pprint
person = {'name': 'tyler', 'age': 24, 'city': 'windsor'}
for v in person.values():
    print (v)
person.setdefault('job','programer')
del person['city']
#for key, value in person.items():
#    print(key + ':', value)

pprint.pprint(person)


# pretty_print = list(person.items())
#print(pretty_print[0])
#print(*pretty_print)
