# CH6 - Lists
# Create -> modify -> loop -> build -> return

def add_student(students, name, score):
    students.append({'name': name, 'score': score})
    return students

def get_passing(students):
    passing = []
    for student in students:
        if student['score'] >= 60:
            passing.append(student['name'])
    return passing

def get_top_score(students):
    top = students[0]
    for student in students:
        if student['score'] > top['score']:
            top = student
    return top['name'], top['score']

students = []
students = add_student(students, "Gman", 92)
students = add_student(students, "Bob", 55)
students = add_student(students, "Sarah", 78)
students = add_student(students, "Mike", 45)
students = add_student(students, "Jess", 88)

passing = get_passing(students)
print(f"Passing students: {passing}")

top_name, top_score = get_top_score(students)
print(f"Top student: {top_name} with {top_score}")
'''
Plain English logic walk through:

1 add_student() — appends a dictionary to the list and returns the updated list
2 get_passing() — builds a new list of names where score is 60 or above
3 get_top_score() — loops through finding the highest score, returns both name and score
4 Main block — builds the student list using add_student() then calls both functions
5 Multiple return values unpacked into two variables
'''


Examples

"1. Creating and Accessing Lists"
_______ = [_______, _______, _______]
_______[_______]    # access by index
_______[-1]         # last item
_______[_______:_______]  # slice


fruits = ["apple", "banana", "mango", "grape"]
fruits[0]     # "apple"
fruits[-1]    # "grape"
fruits[1:3]   # ["banana", "mango"]
fruits[:2]    # ["apple", "banana"]
fruits[2:]    # ["mango", "grape"]
'''
Plain English:
A list stores multiple values in order inside square brackets.
Access items by their index position starting at 0. Negative indexes count from the end.
Slicing grabs a range — start index up to but not including the end index.

Use cases:
Storing a collection of related items
Any time you need an ordered group of values
'''


"2. Modifying Lists"
_______.append(_______)      # add to end
_______.insert(_______, _______) # insert at index
_______.remove(_______)      # remove by value

del _______[_______]         # remove by index
_______[_______] = _______   # change item at index
_______.sort()               # sort in place


fruits = ["apple", "banana", "mango"]
fruits.append("grape")          # ["apple", "banana", "mango", "grape"]
fruits.insert(1, "cherry")      # ["apple", "cherry", "banana", "mango", "grape"]
fruits.remove("banana")         # ["apple", "cherry", "mango", "grape"]

del fruits[0]                   # ["cherry", "mango", "grape"]
fruits[0] = "kiwi"              # ["kiwi", "mango", "grape"]
fruits.sort()                   # ["grape", "kiwi", "mango"]
'''
Plain English:
Lists are mutable — you can change them after creation. append() adds to the end.
insert() adds at a specific position. remove() finds and removes the first matching value.
del removes by position. sort() reorders in place.

Use cases:
Building a list gradually with append()
Removing items that are no longer needed
Keeping a list in alphabetical or numerical order
'''


"3. Checking Lists"
len(_______)              # number of items
_______ in _______        # check if value exists
_______ not in _______    # check if value missing
_______.index(_______)    # find position of value


fruits = ["apple", "banana", "mango"]
len(fruits)              # 3
"apple" in fruits        # True
"grape" not in fruits    # True
fruits.index("banana")   # 1
'''
Plain English:
len() counts items. in and not in check if a value exists — returns True or False.
index() returns the position of the first match.

Use cases:
Checking before accessing to avoid errors
Finding where an item is in a list
'''


"4. Looping Through Lists"
# Loop through items
for _______ in _______:
    _______

# Loop through with index
for i in range(len(_______)):
    _______[i]

# Loop through two lists together
for _______, _______ in zip(_______, _______):
    _______


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

names = ["Gman", "Bob"]
scores = [95, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
'''
Plain English:
Loop directly through items when you just need each value.
Loop with range(len()) when you need the index too.
Use zip() to pair two lists together item by item.

Use cases:
Processing every item in a list
Displaying numbered lists
Pairing related data from two lists
'''


"5. Building New Lists"
def _______(_______):
    result = []
    for _______ in _______:
        if _______:
            result.append(_______)
    return result


def get_positives(numbers):
    result = []
    for number in numbers:
        if number > 0:
            result.append(number)
    return result

numbers = [3, -1, 4, -2, 5]
positives = get_positives(numbers)
print(positives)  # [3, 4, 5]
'''
Plain English:
Start with an empty list. Loop through the source list. Check each item.
Append items that meet the condition. Return the new list.
This pattern builds filtered or transformed versions of existing lists.

Use cases:
Filtering a list by a condition
Transforming every item in a list
Removing duplicates
'''


"6. Copying Lists"
import copy
_______ = copy.copy(_______)       # copy outer list
_______ = copy.deepcopy(_______)   # copy everything including nested lists


import copy

original = [1, 2, 3]
shallow = copy.copy(original)      # independent copy
shallow.append(4)                  # doesn't affect original

nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)       # fully independent copy
deep[0].append(99)    # doesn't affect nested
'''
Plain English:
Assigning a list to a new variable just copies the reference —
both variables point to the same list. Use copy.copy() to make an independent copy.
Use copy.deepcopy() when the list contains other lists inside it.

Use cases:
Any time you need to modify a list without affecting the original
Working with nested lists
'''


"7. Tuples"
_______ = (_______, _______, _______)
tuple(_______)    # convert list to tuple
list(_______)     # convert tuple to list
(_______, )       # single item tuple - needs trailing comma


dimensions = (1920, 1080)
dimensions[0]     # 1920
# dimensions[0] = 1280  # ERROR - tuples are immutable

single = (42,)    # single item tuple
coords = tuple([10, 20])  # convert list to tuple
points = list((10, 20))   # convert tuple to list
'''
Plain English:
Tuples are like lists but immutable — you can't change them after creation.
Use parentheses instead of square brackets.
A single item tuple needs a trailing comma or Python thinks it's just parentheses around a value.

Use cases:
Storing data that should never change like coordinates or RGB values
Returning multiple values from a function
'''




