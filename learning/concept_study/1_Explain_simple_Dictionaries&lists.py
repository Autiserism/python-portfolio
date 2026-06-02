
    Complete CRUD Function
Question: Write a function called remove_item that:

Takes items and item_name as parameters
Checks if item exists
If yes: removes it and prints "Removed [item]"
If no: prints "Item not found"

items = {
    'apple': {'price': 2, 'stock': 50}

def remove_item(items, item_name):
    if item_name in items:
        del items[item_name]
        print(f"Removed {item_name}")
    else:
        print('Item Not Found')

item_name = 'apple'
remove_item(items, item_name)
Pattern: Function with dictionary parameter → check existence → delete → confirm

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Removing an Item
items = {
    'apple': {'price': 2, 'stock': 50},
    'bread': {'price': 3, 'stock': 20}
}
Question: Remove 'bread' from the dictionary.

del items['bread']
Pattern: del dictionary[key]
Alternative: items.pop('bread') (also removes but returns the value)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Adding New Item to Dictionary
items = {
    'apple': {'price': 2, 'stock': 50}
}
Question: Add a new item 'orange' with price 3 and stock 25 to the dictionary.

items['orange'] = {'price': 3, 'stock': 25}
Pattern: dictionary[new_key] = {nested_dictionary}
This adds a whole new item with its nested structure.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

 Full Mini-Program
Question: Write a function called show_all_prices that:

Takes items as a parameter
Checks if empty (print "No items" and return if empty)
Loops through and prints each item with its price
Format: "apple: $2"

items = {
    'apple': {'price': 2, 'stock': 50},
    'bread': {'price': 3, 'stock': 20}
}
def show_all_prices(items):
    if not items:
        print('No Items')
        return
    for item_name in items:
        print(f"{item_name}: ${items[item_name]['price']}")

show_all_prices(items)
Pattern breakdown:

Early return pattern: if not dictionary: return
Loop through keys: for key in dictionary:
Access nested value: dictionary[loop_variable]['inner_key']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Empty Dictionary Check
items = {}

Question: Write an if statement to check if the dictionary is empty and print "No items" if it is.

if not items:
    print('No Items')
else:
    print('not empty')
Pattern:
if not dictionary: returns True when empty (empty containers are falsy)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Function That Modifies
items = {
    'apple': {'price': 2, 'stock': 50}
}
Question: Write a function called add_stock
that takes items, item_name, and amount as parameters.
It should add the amount to that items stock. No return needed (it modifies in place).

def add_stock(items, item_name, amount):
    if item_name in items:
        items[item_name]['stock'] += amount
        print(f'{amount} Added to {item_name}')
    else:
        print('invalid')

item_name = 'apple'
if item_name in items:
    amount = int(input('Enter an amount: '))
    add_stock(items, item_name, amount)
else:
    print('item not found')

Pattern:

Function does ONE thing (adds stock)
Input/validation happens OUTSIDE
Check existence BEFORE asking for more input

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Function Definition Pattern
items = {
    'apple': {'price': 2, 'stock': 50}
}
Question: Write a function called get_price that takes items as a parameter and returns the price of 'apple'.

items = {
    'apple': {'price': 2, 'stock': 50}
}
item_name = 'apple'
def get_price(items, item_name):
    if item_name in items:
        return items[item_name]['price']
    else:
        return None
result = get_price(items, item_name)
print(f'{item_name}: ${result}')

Create a reusable function called get_price.
It needs two pieces of information:
1. the dictionary to search
2. the item name to search for

items[item_name]['price'] gets the price from that inner dictionary.
return sends that price back out of the function.
result receives the returned price.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

 User Input + Stock Update
items = {
    'apple': {'price': 2, 'stock': 50}
}
item = input('Item: ')  # User types 'apple'
amount = int(input('Amount: '))  # User types 10

Question: Update apples stock by adding the amount, then print the new stock.

if item in items:
    amount = int(input('Amount: '))
    items[item]['stock'] += amount
    print(f"{item} \nStock: {items[item]['stock']}")
else:
    print('invalid item')
Pattern: Check existence → modify nested value with += → print updated value


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

 Combining: Check Existence Then Access
items = {
    'apple': {'price': 2, 'stock': 50}
}
item = input('Enter item: ')  # User types 'apple'
Question: Write code that checks if the item exists, then prints its price. If not found, print "Not available".

if item in items:
    print(f"{item}: ${items[item]['price']}")
else:
    print("Not available")
Pattern: Check existence first (if key in dictionary), then safely access nested data.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Checking if Key Exists
items = {
    'apple': {'price': 2, 'stock': 50}
}
user_input = 'banana'
Question: Write an if statement to check if 'banana' exists in items.

if user_input in items:
    print('yes')
else:
    print('no')
Pattern: if key in dictionary: (returns True/False)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

 Multi-Line Print (Your display_all Pattern)
items = {
    'apple': {'price': 2, 'stock': 50, 'category': 'fruit'}
}
Question: Using .items(), print this exact format for apple:
apple:
  Price: $2
  Stock: 50
  Category: fruit

for item_name, item_data in items.items():
    print(f'\n{item_name}:')
    print(f'  Price: ${item_data["price"]}')
    print(f'  Stock: {item_data["stock"]}')
    print(f'  Category: {item_data["category"]}')
Pattern: After .items() unpacking, access all nested values through value_variable['key']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Accessing Nested Data After .items() Unpacking
items = {
    'apple': {'price': 2, 'stock': 50},
    'bread': {'price': 3, 'stock': 20}
}
Question: Using .items() unpacking, print each items name and price.
Example output:
apple: $2
bread: $3

for item_name, item_data in items.items():
    print(f"{item_name}: ${item_data['price']}")

Pattern: After unpacking with .items(), access nested data
with value_variable['inner_key'] (not dictionary[key]['inner_key'])


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

.items() Pattern (Your display_all Function)
items = {
    'apple': {'price': 2, 'stock': 50},
    'bread': {'price': 3, 'stock': 20}
}
Question: Write a for loop using .items() that prints each item name and its complete nested dictionary.

for item_name, item_data in items.items():
    print(item_name)
    print(item_data)
'''    #prints
apple
{'price': 2, 'stock': 50}
bread
{'price': 3, 'stock': 20}
'''
Pattern: for key, value in dictionary.items(): (unpacks each key-value pair)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Looping and Accessing Nested Data
items = {
    'apple': {'price': 2, 'stock': 50},
    'bread': {'price': 3, 'stock': 20}
}

Question: Write a for loop that prints each item name AND its price.
Example output:
apple: $2
bread: $3

for item in items:
    print(f"{item}: ${items[item]['price']}")

Pattern: Loop through keys, access nested value with dictionary[loop_variable]['inner_key']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Looping Through Keys
items = {
    'apple': {'price': 2, 'stock': 50},
    'bread': {'price': 3, 'stock': 20}
}
Question: Write a for loop that prints each item name (apple, bread).
for item in items:
    print(item)

Pattern: for key in dictionary: (automatically loops through keys)
Note: use for item_name in items.keys()

for item_name in items.keys():
        print(f'{item_name}')


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Print Pattern with f-string
items = {
    'apple': {'price': 2, 'stock': 50}
}
item_name = 'apple'
Question: Write the print statement to display: "The price of apple is $2"

Basic Pattern
apple_price = items['apple']['price']apple_price = items['apple']['price']
print(f'The price of apples is ${apple_price}')

More compact pattern:

print(f'The price of {item_name} is ${items[item_name]["price"]}')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Try the Inline Pattern
items = {
    'bread': {'price': 3, 'stock': 20}
}
item_name = 'bread'

Question: Print "The price of bread is $3" using inline access (no intermediate variable).

print(f"The price of {item_name} is ${items[item_name]['price']}")

Pattern: f"text {variable} text ${dictionary[variable]['key']}"


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Pattern:
dictionary['key'] or dictionary.get('key')
dictionary = {'key' : 'value'}
# calls out the value assinged to the 'key'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Pattern:
dictionary['key'][index] = value
#to modify the index value
dictionary = {'kA1':'vA1', 'kB1' : [00,00,00,00]

dictionary['kB1'][1] = 25  #[00,25,00,00]


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Pattern:
dictionary = {'kA1' :'vA1', 'NB1':{'kC2':'vC2','kD2':'vD2'}}

dictionary['NB1']['kC2']        #calles out vD2

#call out a value thats within another nested dictionary

Basic Nested Access (Price Pattern)

items = {
    'apple': {'price': 2, 'stock': 50},
    'bread': {'price': 3, 'stock': 20}
}
Question: How would you get the price of apple
items['apple']['price'] → 2

Pattern: dictionary[outer_key][inner_key]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Modifying Nested Value (Stock Update Pattern)

items = {
    'apple': {'price': 2, 'stock': 50},
    'bread': {'price': 3, 'stock': 20}
}
Question: How would you add 10 to breads stock (make it 30)?

items['bread']['stock'] += 10

Pattern: dictionary[outer_key][inner_key] += amount

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Pattern:

dictionary['xyzkey'].append(new_item)

#when you have a dictionary of keys with a list as its value appends new_item to list
dictionary = { 'xyzkey' : ['list', 'item']}

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Pattern:

dictionary = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
# to update a value in a dictionary
dictionary['k3']='W25'              #1st method
dictionary.update({'k3':'W25'})     #2nd method
dictionary = {'k1':'v1', 'k2':'v2', 'k3':'W25'} # updated k3's value pair

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


Pattern:
company = {'key1': {'key2': {'key3': 'value3','key4': 'value4'}}}
dictionary['key1']['key2']['key3'] #gives the value, value3
#(chain as deep as needed)


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

 List Inside Nested Dictionary

school = {
    'classes': {
        'math': {
            'teacher': 'Mr. Smith',
            'students': ['Amy', 'Bob', 'Carl']
        }
    }
}
Question: How would you call out 'Bob'?
school['classes']['math']['students'][1] → 'Bob'

Pattern: dictionary['key1']['key2']['key3'][index] (dictionary chain, then list index)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


Modifying in Deep Nesting

school = {
    'classes': {
        'math': {
            'teacher': 'Mr. Smith',
            'students': ['Amy', 'Bob', 'Carl']
        }
    }
}
Question: How would you change 'Carl' to 'Carlos'?

school['classes']['math']['students'][2] = 'Carlos'
Pattern: dictionary['key1']['key2']['key3'][index] = new_value


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


Adding to a Nested List

school = {
    'classes': {
        'math': {
            'teacher': 'Mr. Smith',
            'students': ['Amy', 'Bob', 'Carl']
        }
    }
}

Question: How would you add 'Dana' to the students list?

school['classes']['math']['students'].append('Dana')
Pattern: dictionary['key1']['key2']['key3'].append(new_item)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

List of Dictionaries (Deeper)

team = [
    {'name': 'Alex', 'position': 'forward', 'points': [12, 15, 18]},
    {'name': 'Jordan', 'position': 'guard', 'points': [8, 10, 14]},
    {'name': 'Taylor', 'position': 'center', 'points': [20, 22, 19]}
]
Question: How would you call out Jordans second game points (the 10)
team[1]['points'][1] → 10
Pattern: list[index]['key'][index] (list index → dictionary key → list index)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


Modifying in List of Dictionaries
team = [
    {'name': 'Alex', 'position': 'forward', 'points': [12, 15, 18]},
    {'name': 'Jordan', 'position': 'guard', 'points': [8, 10, 14]},
    {'name': 'Taylor', 'position': 'center', 'points': [20, 22, 19]}
]
Question: How would you change Taylors first game points from 20 to 25?

team[2]['points'][0] = 25
Pattern: list[index]['key'][index] = new_value

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

 Dictionary with Multiple Nested Lists
store = {
    'fruits': ['apple', 'banana', 'orange'],
    'vegetables': ['carrot', 'broccoli', 'spinach'],
    'prices': [1.50, 0.75, 2.00]
}
Question: How would you call out 'broccoli' and its price (2.00)?

b_veg = store['vegetables'][1]
b_veg = store['vegetables'][1]
b_price = store['prices'][2]
print(b_veg,b_price)

store['vegetables'][1] → 'broccoli' store['prices'][2] → 2.00

Pattern:
variable1 = dictionary['key'][index]
variable2 = dictionary['key'][index]
print variable1, variable2

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


Complex Nesting (Dictionary → List → Dictionary)
library = {
    'books': [
        {'title': 'Python Basics', 'author': 'Smith', 'year': 2020},
        {'title': 'Advanced Python', 'author': 'Jones', 'year': 2022}
    ]
}
Question: How would you call out the author of 'Advanced Python'?

library['books'][1]['author'] → 'Jones'

Pattern: dictionary['key'][index]['key'] (dictionary → list → dictionary)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Adding to Nested Structure
library = {
    'books': [
        {'title': 'Python Basics', 'author': 'Smith', 'year': 2020},
        {'title': 'Advanced Python', 'author': 'Jones', 'year': 2022}
    ]
}
Question: How would you add a new book: {'title': 'Data Science', 'author': 'Lee', 'year': 2023}?

library['books'].append({'title': 'Data Science', 'author': 'Lee', 'year': 2023})

Pattern: dictionary['key'].append({new_dictionary})

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Modifying a Value Deep in Nesting
library = {
    'books': [
        {'title': 'Python Basics', 'author': 'Smith', 'year': 2020},
        {'title': 'Advanced Python', 'author': 'Jones', 'year': 2022}
    ]
}
Question: How would you change the year of 'Python Basics' from 2020 to 2021?

library['books'][0]['year'] = 2021

Pattern: dictionary['key'][index]['key'] = new_value

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


 Modifying in Nested Lists
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Question: How would you change the 9 to a 99?

grid[2][2] = 99

Pattern: list[row_index][column_index] = new_value

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


Modifying in Dictionary with Nested Lists
game = {
    'board': [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['X', 'O', 'X']
    ]
}
Question: How would you change the top-right 'X' to an 'O'?

game['board'][0][2] = 'O'

Pattern: dictionary['key'][row_index][column_index] = new_value

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Complex Mixed Nesting
company = {
    'departments': [
        {
            'name': 'Sales',
            'teams': [
                {'lead': 'Anna', 'members': ['Bob', 'Carl']},
                {'lead': 'Diana', 'members': ['Eve', 'Frank']}
            ]
        }
    ]
}
Question: How would you call out 'Eve'?

company['departments'][0]['teams'][1]['members'][0] → 'Eve'

Pattern: dictionary['key'][index]['key'][index]['key'][index]
(Chain as deep as needed: dict → list → dict → list → dict → list)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Adding to Deep Nesting
company = {
    'departments': [
        {
            'name': 'Sales',
            'teams': [
                {'lead': 'Anna', 'members': ['Bob', 'Carl']},
                {'lead': 'Diana', 'members': ['Eve', 'Frank']}
            ]
        }
    ]
}
Question: How would you add 'Grace' to Dianas team members?

company['departments'][0]['teams'][1]['members'].append('Grace')

Pattern: dictionary['key'][index]['key'][index]['key'].append(new_item)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Modifying in Deep Nesting
company = {
    'departments': [
        {
            'name': 'Sales',
            'teams': [
                {'lead': 'Anna', 'members': ['Bob', 'Carl']},
                {'lead': 'Diana', 'members': ['Eve', 'Frank']}
            ]
        }
    ]
}
Question: How would you change Annas name to 'Anna Smith'?

company['departments'][0]['teams'][0]['lead'] = 'Anna Smith'

Pattern: dictionary['key'][index]['key'][index]['key'] = new_value

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

 Multiple Operations
inventory = {
    'warehouse_A': {
        'electronics': ['laptop', 'phone'],
        'furniture': ['desk']
    },
    'warehouse_B': {
        'electronics': ['tablet'],
        'furniture': ['chair', 'lamp']
    }
}
Question A: How would you call out 'tablet'?

A: inventory['warehouse_B']['electronics'][0] → 'tablet'
Pattern: dictionary['key1']['key2'][index]

Question B: How would you add 'sofa' to warehouse_B furniture

B: inventory['warehouse_B']['furniture'].append('sofa')
Pattern: dictionary['key1']['key2'].append(new_item)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Final Challenge (Everything Combined)
school = {
    'grades': {
        '10th': [
            {
                'class': 'Math',
                'students': [
                    {'name': 'Sam', 'scores': [85, 90, 88]},
                    {'name': 'Riley', 'scores': [92, 95, 91]}
                ]
            }
        ]
    }
}
Question A: How would you call out Rileys second score (95)?

A: school['grades']['10th'][0]['students'][1]['scores'][1] → 95
Pattern: dictionary['key1']['key2'][index]['key3'][index]['key4'][index]

Question B: How would you change Sams first score from 85 to 87

B: school['grades']['10th'][0]['students'][0]['scores'][0] = 87
Pattern: dictionary['key1']['key2'][index]['key3'][index]['key4'][index] = new_value







