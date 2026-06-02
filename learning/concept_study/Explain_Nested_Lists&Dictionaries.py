
                    Nested Lists in Dictionaries

# Dictionary with lists as values
inventory = {
    'tools': ['hammer', 'wrench', 'screwdriver'],
    'parts': ['bolt', 'nut', 'screw'],
    'materials': ['wood', 'metal', 'plastic']
}

# Access the list
print(inventory['tools'])  # ['hammer', 'wrench', 'screwdriver']

# Access specific item in the list - CHAIN the brackets
print(inventory['tools'][0])  # 'hammer'
print(inventory['tools'][1])  # 'wrench'

# Breakdown:
# inventory['tools'] → gets the list
#                 [0] → gets first item from that list

                    Step-by-Step Visual

inventory['tools'][1]
    ↓           ↓
    |           |
    |           └── Then grab index 1 from that list
    └── First get the list at key 'tools'

# Think of it as working LEFT to RIGHT:
# Step 1: inventory['tools'] = ['hammer', 'wrench', 'screwdriver']
# Step 2: ['hammer', 'wrench', 'screwdriver'][1] = 'wrench'

Pattern: dictionary['key'][index] = value # to update an index's value

Nested Dictionaries in Lists
# List containing dictionaries
employees = [
    {'name': 'Alice', 'role': 'Manager'},
    {'name': 'Bob', 'role': 'Developer'},
    {'name': 'Charlie', 'role': 'Designer'}
]

# Access a specific dictionary
print(employees[0])  # {'name': 'Alice', 'role': 'Manager'}

# Access a value inside that dictionary - CHAIN the brackets
print(employees[0]['name'])  # 'Alice'
print(employees[1]['role'])  # 'Developer'

# Breakdown:
# employees[0] → gets first dictionary
#         ['name'] → gets value at key 'name' from that dict
Step-by-Step Visual
employees[1]['role']
    ↓      ↓
    |      |
    |      └── Then get value at key 'role'
    └── First get dictionary at index 1

# Think LEFT to RIGHT:
# Step 1: employees[1] = {'name': 'Bob', 'role': 'Developer'}
# Step 2: {'name': 'Bob', 'role': 'Developer'}['role'] = 'Developer'

Deep Nesting - Dictionary → List → Dictionary
# More complex structure
company = {
    'departments': [
        {
            'name': 'Engineering',
            'employees': ['Alice', 'Bob', 'Charlie']
        },
        {
            'name': 'Sales',
            'employees': ['Dana', 'Eve']
        }
    ]
}

# Get the list of departments
print(company['departments'])

# Get first department dict
print(company['departments'][0])

# Get name of first department
print(company['departments'][0]['name'])  # 'Engineering'

# Get employees list from first department
print(company['departments'][0]['employees'])  # ['Alice', 'Bob', 'Charlie']

# Get second employee from first department
print(company['departments'][0]['employees'][1])  # 'Bob'
The Chain Breakdown
company['departments'][0]['employees'][1]
   ↓         ↓         ↓       ↓        ↓
   |         |         |       |        |
   |         |         |       |        └── Index 1 from that list
   |         |         |       └── Get 'employees' key from that dict
   |         |         └── Index 0 from that list
   |         └── Get 'departments' key (returns a list)
   └── Start with the dictionary

# Read LEFT to RIGHT, one bracket at a time

The choice Feature (I think you mean random.choice())

import random

# Pick random item from a list
tools = ['hammer', 'wrench', 'screwdriver']
random_tool = random.choice(tools)
print(random_tool)  # Could be any: 'hammer', 'wrench', or 'screwdriver'

# Each time you run it, could be different
print(random.choice(tools))  # 'wrench'
print(random.choice(tools))  # 'hammer'
print(random.choice(tools))  # 'wrench'

                    Using with Nested Structures

inventory = {
    'tools': ['hammer', 'wrench', 'screwdriver'],
    'parts': ['bolt', 'nut', 'screw']
}

# Pick random tool
random_tool = random.choice(inventory['tools'])
print(random_tool)  # Random from tools list

# Pick random part
random_part = random.choice(inventory['parts'])
print(random_part)  # Random from parts list

Practice Pattern - "Drill Down"
Rule: Work LEFT to RIGHT, one step at a time
data[key][index]['another_key'][another_index]
  1   2     3          4

1. Start with data
2. Get value at 'key' (returns something)
3. Get item at index from that something (returns something else)
4. Get value at 'another_key' from that something else
5. Get item at another_index from THAT result
