
    Accessing Nested Dictionary (3 levels)
student = {
    'name': 'Bob',
    'subjects': {'math': 90, 'english': 85}
}
Question: How would you access Bobs math score (90)?

student['subjects']['math'] → 90
Pattern: dict['key1']['key2'] - chain as deep as needed

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Dictionary .values() for Calculation
subjects = {'math': 90, 'english': 85, 'gym': 80}
Question: Get the sum of all scores using sum() and .values().

sum(subjects.values()) → 255
Pattern: sum(dict.values()) - adds all values in dictionary

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Calculating Average
subjects = {'math': 90, 'english': 85, 'gym': 80}
Question: Calculate the average using sum(), .values(), and len().

#average = sum(subjects.values()) / len(subjects.values()) → 85.0

Slightly cleaner:
    average = sum(subjects.values()) / len(subjects)

Both work! len(subjects) counts keys (same as number of values).
Pattern: Average = sum of values ÷ count

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Lambda Function Basics
Question: What does this lambda do?
lambda x: x * 2
means:

Takes one input (x)
Returns x * 2

Examples:
double = lambda x: x * 2
double(5)  → 10
double(3)  → 6
Pattern: lambda parameters: expression - one-line function

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Lambda with Dictionary Access
Question: Write a lambda that takes a student dict and returns their average.
student = {'name': 'Bob', 'average': 90}

get_avg = lambda student: student['average']
get_avg({'name': 'Bob', 'average': 90})  → 90

Pattern: lambda dict: dict['key'] - extracts a value from dictionary
The lambda receives the whole dictionary and returns one value from it.


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    sorted() with key Parameter
students = [
    {'name': 'Bob', 'average': 90},
    {'name': 'Anna', 'average': 85},
    {'name': 'Mike', 'average': 95}
]
Question: Sort students by average (lowest to highest) using sorted() with key=lambda.

L2H = sorted(students, key=lambda x: x['average'])
Result: [{'name': 'Anna', 'average': 85}, {'name': 'Bob', 'average': 90}, {'name': 'Mike', 'average': 95}]
Pattern: sorted(list, key=lambda x: x['key']) - sorts by specific dictionary value
How it works:

Lambda extracts the 'average' from each student
sorted() compares those values
Returns new sorted list

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    sorted() with reverse=True
Question: Sort students by average (HIGHEST to lowest) - add reverse=True.

L2H = sorted(students, key=lambda x: x['average'], reverse=True)

Result: [{'name': 'Mike', 'average': 95}, {'name': 'Bob', 'average': 90}, {'name': 'Anna', 'average': 85}]
Pattern: Add reverse=True for descending order

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    enumerate() with Start Parameter

names = ['Alice', 'Bob', 'Charlie']

Question: Loop through with enumerate() starting at 1 (not 0), printing:
#Output
1 Alice
2 Bob
3 Charlie

for i, name in enumerate(names, 1):
    print(i, name)
Pattern: for index, item in enumerate(list, start):

start parameter sets the starting number (default is 0)
Unpacks into two variables: index and item

Pattern: enumerate(list, start_number) - second parameter sets starting index

for i, student in enumerate(ranked, 1):
    print(f"{i}. {student['name']} - avg {student['average']}")

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Combining sorted() and enumerate()
students = [
    {'name': 'Bob', 'average': 85},
    {'name': 'Anna', 'average': 95},
    {'name': 'Mike', 'average': 90}
]
Question: Sort by average (highest first), then loop with enumerate starting at 1, printing rank and name.

H2L = sorted(students, key=lambda x: x['average'], reverse=True)
for i, student in enumerate(H2L, 1):
    print(i, student['name'])

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    .title() for Name Capitalization
name = 'mike smith'
Question: Convert to title case (first letter of each word capitalized).

name.title() → 'Mike Smith'
Pattern: .title() - capitalizes first letter of each word
Your program uses this for name input:

name = input('Enter name: ').title()
Ensures consistent capitalization regardless of how user types it.


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete view_ranked Function
Question: Write view_ranked() that:

Sorts students by average (highest first)
Loops with enumerate starting at 1
Prints rank, name, average, and grade

students = [
    {'name': 'Bob', 'average': 85},
    {'name': 'Anna', 'average': 95}
]

def get_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    else: return 'C'

def view_ranked():
    H2L = sorted(students, key=lambda x: x['average'], reverse=True)
    for i, student in enumerate(H2L, 1):
        print(i, student['name'], get_grade(student['average']))

Pattern - Complete ranked display:

Sort by specific field (highest first)
Enumerate with rank numbers
Access nested data and call helper functions

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Dictionary .items() for Subject Loop
subjects = {'math': 90, 'english': 85, 'gym': 80}
Question: Loop through and print each subject name and score.

for subject, score in subjects.items():
    print(f"{subject} {score}")

Output:
math 90
english 85
gym 80

Pattern: for key, value in dict.items(): - unpacks both at once

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Getting Dictionary Keys as List
sales = {'January': 100, 'February': 125, 'March': 110}
Question: Convert the keys to a list so you can access by index.

months = list(sales.keys())
Result: ['January', 'February', 'March']
Pattern: list(dict.keys()) - converts keys to indexable list

months = list(sales.keys()) → ['January', 'February', 'March']
Now you can access by index: months[0] → 'January'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Numbered Menu from Keys
sales = {'January': 100, 'February': 125, 'March': 110}
months = list(sales.keys())
Question: Print numbered menu with sales values:

for i, mon in enumerate(months, 1):
    print(i, mon, sales[mon])

Pattern: Enumerate keys list → access values using keys
Output:
1 January 100
2 February 125
3 March 110


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Getting Selected Month Name
User sees menu and types 2 (wants February).
months = ['January', 'February', 'March']
choice = 2  # User input
Question: Get the month name at that position (remember: display is 1-indexed, list is 0-indexed).


    Complete pattern:
choice = int(input('Select: '))  # User types 2
month_name = months[choice - 1]  # 2 - 1 = 1 → 'February'
Pattern: Users 1-indexed choice → subtract 1 → get list item

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete Update Flow
sales = {'January': 100, 'February': 125, 'March': 110}
Question: Write code that:

Gets keys as list
Shows numbered menu
Gets user choice
Converts to index
Gets month name
Updates that months value

months = list(sales.keys())
for i, mon in enumerate(months, 1):
    print(f"{i} {mon}: {sales[mon]}")
choice = int(input('enter a number: ')) - 1
update = months[choice]
print(f'enter new number for {update}')
sales[update] = int(input("enter new value: "))
print(sales)
Pattern - Dynamic dictionary update:

list(dict.keys()) - keys → indexable list
enumerate(list, 1) - numbered display
choice - 1 - convert to 0-indexed
months[index] - get key name
dict[key_name] = new_value - update



------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Applying to Your Employee Code
Question: Rewrite your update_rec() using this pattern for the nested sales dict.
pythonemployees = {
    'emp1': {'name': 'Quimba', 'sales': {'January': 100, 'February': 125}}
}

def find_employee(name):
    for emp_id, emp_data in employees.items():
        if emp_data['name'].lower() == name.lower():
            return emp_data
    return None

def update_rec():
    name = input('enter name: ').title()
    record = find_employee(name)
    if not record:  # Guard clause first
        print('not found')
        return
    months = list(record['sales'])
    for i, mon in enumerate(months, 1):
        print(f"{i}. {mon}: {record['sales'][mon]}")
    choice = int(input("which month #: ")) - 1
    selected_mon = months[choice]
    record['sales'][selected_mon] = int(input("Enter the updated total: "))
    print(f"{record['name']} sales for {selected_mon} has been updated")
    # Show updated values
    for i, mon in enumerate(months, 1):
        print(f"{i}. {mon}: {record['sales'][mon]}")

Pattern - Complete dynamic nested dict update:

Find record
Guard clause
Extract keys to list
Enumerate for menu
Convert choice to index
Get key name
Update nested value: record['sales'][month_name] = new_value
Confirmation

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------
