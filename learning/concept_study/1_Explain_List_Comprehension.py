
   Intro to List Comprehension

Regular loop way (Typical):
doubled = []
for num in numbers:
    doubled.append(num * 2)

List comprehension way (shorthand):

doubled = [num * 2 for num in numbers]
Pattern: [expression for item in list]

num * 2 is what goes in the new list
for num in numbers loops through the original

Read it like: "Give me num * 2, for each num in numbers"

doubled = [num * 2 for num in numbers] → [2, 4, 6, 8, 10]
Pattern: [expression for item in list] creates new list by transforming each item

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    List Comprehension - Complete Breakdown
What Is List Comprehension?
List comprehension is a shortcut for creating lists.
Instead of writing a full for loop with .append(), you write everything in one line inside square brackets.

Key benefit: Faster to write, easier to read (once you learn the pattern)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    The Basic Pattern - Side by Side
Long Way (Traditional Loop)
# Create list of squares
squares = []
for num in range(5):
    squares.append(num ** 2)

print(squares)  # [0, 1, 4, 9, 16]
List Comprehension Way
# Same result, one line
squares = [num ** 2 for num in range(5)]

print(squares)  # [0, 1, 4, 9, 16]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Breaking Down the Syntax
[expression for item in iterable]
     ↓          ↓         ↓
     |          |         └── What youre looping through
     |          └── Variable name for each item
     └── What to do with each item
Visual Step-by-Step
[num ** 2 for num in range(5)]
    ↓         ↓       ↓
    |         |       └── Loop through 0, 1, 2, 3, 4
    |         └── Each number is called 'num'
    └── Square each num


# How it works internally:
# num = 0 → 0 ** 2 = 0
# num = 1 → 1 ** 2 = 1
# num = 2 → 2 ** 2 = 4
# num = 3 → 3 ** 2 = 9
# num = 4 → 4 ** 2 = 16
# Result: [0, 1, 4, 9, 16]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Basic Examples - Many Patterns
Double Each Number
# ❌ LONG WAY
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)
# [2, 4, 6, 8, 10]

# ✅ LIST COMPREHENSION
numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
# [2, 4, 6, 8, 10]


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Convert to Uppercase
# ❌ LONG WAY
words = ['hello', 'world', 'python']
upper_words = []
for word in words:
    upper_words.append(word.upper())
# ['HELLO', 'WORLD', 'PYTHON']

# ✅ LIST COMPREHENSION
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
# ['HELLO', 'WORLD', 'PYTHON']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Get Lengths
# ❌ LONG WAY
words = ['cat', 'elephant', 'dog']
lengths = []
for word in words:
    lengths.append(len(word))
# [3, 8, 3]

# ✅ LIST COMPREHENSION
words = ['cat', 'elephant', 'dog']
lengths = [len(word) for word in words]
# [3, 8, 3]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Extract Values from Dictionary
# ❌ LONG WAY
products = [
    {'name': 'laptop', 'price': 1200},
    {'name': 'mouse', 'price': 25},
    {'name': 'keyboard', 'price': 75}
]

prices = []
for product in products:
    prices.append(product['price'])
# [1200, 25, 75]

# ✅ LIST COMPREHENSION
prices = [product['price'] for product in products]
# [1200, 25, 75]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Adding Conditions (if statements)
Pattern with IF
[expression for item in iterable if condition]
     ↓          ↓         ↓           ↓
     |          |         |           └── Only include if True
     |          |         └── What to loop through
     |          └── Variable name
     └── What to do with items that pass the condition

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Filter Even Numbers
# ❌ LONG WAY
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
# [2, 4, 6, 8, 10]

# ✅ LIST COMPREHENSION
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
# [2, 4, 6, 8, 10]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Get Long Words
# ❌ LONG WAY
words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
long_words = []
for word in words:
    if len(word) > 3:
        long_words.append(word)
# ['elephant', 'butterfly']

# ✅ LIST COMPREHENSION
words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
long_words = [word for word in words if len(word) > 3]
# ['elephant', 'butterfly']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Filter by Dictionary Value
products = [
    {'name': 'laptop', 'price': 1200, 'stock': 5},
    {'name': 'mouse', 'price': 25, 'stock': 0},
    {'name': 'keyboard', 'price': 75, 'stock': 10}
]

# ❌ LONG WAY
in_stock = []
for product in products:
    if product['stock'] > 0:
        in_stock.append(product['name'])
# ['laptop', 'keyboard']

# ✅ LIST COMPREHENSION
in_stock = [product['name'] for product in products if product['stock'] > 0]
# ['laptop', 'keyboard']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Transform AND Filter - Both Together
Double Only Even Numbers
numbers = [1, 2, 3, 4, 5, 6]

# ❌ LONG WAY
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num * 2)
# [4, 8, 12]

# ✅ LIST COMPREHENSION
result = [num * 2 for num in numbers if num % 2 == 0]
# [4, 8, 12]

# Breakdown:
# num = 2 (even) → 2 * 2 = 4 ✅ included
# num = 4 (even) → 4 * 2 = 8 ✅ included
# num = 6 (even) → 6 * 2 = 12 ✅ included
# 1, 3, 5 are odd → skipped

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Uppercase Only Long Words
words = ['cat', 'elephant', 'dog', 'butterfly']

# ❌ LONG WAY
result = []
for word in words:
    if len(word) > 3:
        result.append(word.upper())
# ['ELEPHANT', 'BUTTERFLY']

# ✅ LIST COMPREHENSION
result = [word.upper() for word in words if len(word) > 3]
# ['ELEPHANT', 'BUTTERFLY']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Get Expensive Product Names
products = [
    {'name': 'laptop', 'price': 1200},
    {'name': 'mouse', 'price': 25},
    {'name': 'monitor', 'price': 300}
]

# ✅ LIST COMPREHENSION
expensive = [p['name'] for p in products if p['price'] > 100]
# ['laptop', 'monitor']

If-Else in List Comprehension
Pattern with IF-ELSE (different from just IF!)
[expression_if_true if condition else expression_if_false for item in iterable]
        ↓                  ↓                ↓                    ↓
        |                  |                |                    └── Loop
        |                  |                └── What to do if False
        |                  └── Condition to check
        └── What to do if True
IMPORTANT: When using if-else, it goes BEFORE the for, not after!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Label Even/Odd
numbers = [1, 2, 3, 4, 5]

# ❌ LONG WAY
labels = []
for num in numbers:
    if num % 2 == 0:
        labels.append('even')
    else:
        labels.append('odd')
# ['odd', 'even', 'odd', 'even', 'odd']

# ✅ LIST COMPREHENSION
labels = ['even' if num % 2 == 0 else 'odd' for num in numbers]
# ['odd', 'even', 'odd', 'even', 'odd']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Cap Values at Maximum
numbers = [5, 15, 25, 35, 45]
max_value = 30

# ❌ LONG WAY
capped = []
for num in numbers:
    if num > max_value:
        capped.append(max_value)
    else:
        capped.append(num)
# [5, 15, 25, 30, 30]

# ✅ LIST COMPREHENSION
capped = [max_value if num > max_value else num for num in numbers]
# [5, 15, 25, 30, 30]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Pass/Fail Grades
scores = [85, 92, 67, 73, 95, 55]

# ✅ LIST COMPREHENSION
results = ['Pass' if score >= 70 else 'Fail' for score in scores]
# ['Pass', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Common Patterns - Quick Examples
Create Range-Based Lists
# First 10 squares
squares = [n ** 2 for n in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# First 5 cubes
cubes = [n ** 3 for n in range(1, 6)]
# [1, 8, 27, 64, 125]

# Multiples of 5 up to 50
multiples = [n * 5 for n in range(1, 11)]
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    String Operations
sentence = "hello world python"

# Get first letter of each word
words = sentence.split()
first_letters = [word[0] for word in words]
# ['h', 'w', 'p']

# Capitalize each word
capitalized = [word.capitalize() for word in words]
# ['Hello', 'World', 'Python']

# Get word lengths
lengths = [len(word) for word in words]
# [5, 5, 6]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Working with Strings
text = "Hello World"

# Each character
chars = [char for char in text]
# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# Only vowels
vowels = [char for char in text if char.lower() in 'aeiou']
# ['e', 'o', 'o']

# Only consonants (uppercase)
consonants = [char.upper() for char in text if char.isalpha() and char.lower() not in 'aeiou']
# ['H', 'L', 'L', 'W', 'R', 'L', 'D']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Using enumerate()
fruits = ['apple', 'banana', 'cherry']

# Get indices where length > 5
long_indices = [i for i, fruit in enumerate(fruits) if len(fruit) > 5]
# [1, 2]  (banana and cherry)

# Create formatted strings
formatted = [f'{i}: {fruit}' for i, fruit in enumerate(fruits)]
# ['0: apple', '1: banana', '2: cherry']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Nested List Comprehension
Flatten a 2D List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# ❌ LONG WAY
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ✅ LIST COMPREHENSION
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Read it as: "for each row, then for each num in that row"

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Create Multiplication Table
# ❌ LONG WAY
table = []
for i in range(1, 4):
    for j in range(1, 4):
        table.append(i * j)
# [1, 2, 3, 2, 4, 6, 3, 6, 9]

# ✅ LIST COMPREHENSION
table = [i * j for i in range(1, 4) for j in range(1, 4)]
# [1, 2, 3, 2, 4, 6, 3, 6, 9]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Create Coordinate Pairs
# ❌ LONG WAY
coords = []
for x in range(3):
    for y in range(3):
        coords.append((x, y))
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

# ✅ LIST COMPREHENSION
coords = [(x, y) for x in range(3) for y in range(3)]
# Same result

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Dictionary Comprehension
Create Dictionary from Two Lists
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'NYC']

# ❌ LONG WAY
person = {}
for i in range(len(keys)):
    person[keys[i]] = values[i]
# {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# ✅ DICT COMPREHENSION (using zip)
person = {k: v for k, v in zip(keys, values)}
# {'name': 'Alice', 'age': 30, 'city': 'NYC'}

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Square Numbers as Dict
# ❌ LONG WAY
squares_dict = {}
for num in range(1, 6):
    squares_dict[num] = num ** 2
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ✅ DICT COMPREHENSION
squares_dict = {num: num ** 2 for num in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Filter Dictionary
prices = {'apple': 1, 'banana': 2, 'cherry': 5, 'date': 3}

# Get items over $2
expensive = {k: v for k, v in prices.items() if v > 2}
# {'cherry': 5, 'date': 3}

# Swap keys and values
swapped = {v: k for k, v in prices.items()}
# {1: 'apple', 2: 'banana', 5: 'cherry', 3: 'date'}

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Set Comprehension
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]

# ❌ LONG WAY
unique_squares = set()
for num in numbers:
    unique_squares.add(num ** 2)
# {1, 4, 9, 16, 25}

# ✅ SET COMPREHENSION
unique_squares = {num ** 2 for num in numbers}
# {1, 4, 9, 16, 25}


# Get unique vowels from text
text = "hello world"
vowels = {char for char in text if char in 'aeiou'}
# {'e', 'o'}

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    When to Use List Comprehension
✅ USE List Comprehension When:

Creating a new list from an existing one
Simple transformation (multiply, uppercase, extract field)
Simple filtering (keep evens, keep long words)
One-line logic
You want cleaner, more readable code

❌ DONT USE When:

Logic is complex (multiple if-else branches)
Need multiple statements per item
Transforming in place (modifying original list)
Debugging complex logic (hard to add print statements)
It makes code harder to read


Examples - Good vs Bad Use
# ✅ GOOD - Simple and clear
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]

# ❌ BAD - Too complex, use regular loop
# Don't do this:
result = [x * 2 if x % 2 == 0 else x * 3 if x % 3 == 0 else x for x in range(100) if x > 10]

# ✅ BETTER - Use regular loop for complex logic
result = []
for x in range(100):
    if x <= 10:
        continue
    if x % 2 == 0:
        result.append(x * 2)
    elif x % 3 == 0:
        result.append(x * 3)
    else:
        result.append(x)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Common Errors to Avoid
# ❌ ERROR - Forgetting brackets
squares = num ** 2 for num in range(5)  # This creates a generator, not a list

# ✅ FIX
squares = [num ** 2 for num in range(5)]


# ❌ ERROR - Wrong order with if-else
result = [num for num in range(10) if num % 2 == 0 else num * 2]  # SYNTAX ERROR

# ✅ FIX - if-else goes BEFORE for
result = [num if num % 2 == 0 else num * 2 for num in range(10)]


# ❌ ERROR - Trying to use multiple statements
result = [print(num), num * 2 for num in range(5)]  # Doesn't work

# ✅ FIX - Use regular loop
for num in range(5):
    print(num)
    result.append(num * 2)

# ❌ ERROR - Modifying list while iterating
numbers = [1, 2, 3, 4, 5]
result = [numbers.remove(n) for n in numbers]  # DANGEROUS

# ✅ FIX - Create new list instead
numbers = [1, 2, 3, 4, 5]
result = [n for n in numbers if n != 3]  # [1, 2, 4, 5]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Practice Conversion
Try converting these loops to list comprehension:
# 1. Basic transformation
numbers = [1, 2, 3, 4, 5]
tripled = []
for num in numbers:
    tripled.append(num * 3)

# Answer:
tripled = [num * 3 for num in numbers]


# 2. With filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = []
for num in numbers:
    if num % 2 != 0:
        odds.append(num)

# Answer:
odds = [num for num in numbers if num % 2 != 0]


# 3. Transform and filter
words = ['cat', 'elephant', 'dog', 'butterfly']
long_upper = []
for word in words:
    if len(word) > 3:
        long_upper.append(word.upper())

# Answer:
long_upper = [word.upper() for word in words if len(word) > 3]


# 4. With if-else
numbers = [10, 25, 30, 15, 40]
adjusted = []
for num in numbers:
    if num > 20:
        adjusted.append(num - 5)
    else:
        adjusted.append(num + 5)

# Answer:
adjusted = [num - 5 if num > 20 else num + 5 for num in numbers]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Quick Reference
# Basic pattern
[expression for item in iterable]

# With filtering (if only)
[expression for item in iterable if condition]

# With if-else (transform)
[expr_true if condition else expr_false for item in iterable]

# Nested (flatten 2D list)
[item for sublist in list_of_lists for item in sublist]

# Dictionary comprehension
{key: value for item in iterable}

# Set comprehension
{expression for item in iterable}

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


List comprehension practice
Rewrite these four loops as list comprehensions:
# Loop 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [n for n in numbers if n % 2 == 0]
print(even)

# Loop 2
words = ['hello', 'world', 'python', 'code']
upper = []
for word in words:
    upper.append(word.upper())

words = ['hello', 'world', 'python', 'code']
upper = [word.upper() for word in words]
print(upper)

# Loop 3
scores = [45, 72, 88, 35, 91, 60]
passing = []
for score in scores:
    if score >= 60:
        passing.append(score)

scores = [45, 72, 88, 35, 91, 60]
passing = [score for score in scores if score >= 60]
print(passing)


# Loop 4
pairs = [('Tyler', 92), ('Bob', 65), ('Sarah', 78)]
names = []
for name, score in pairs:
    if score >= 70:
        names.append(name)

pairs = [('Gman', 92), ('Bob', 65), ('Sarah', 78)]
names = [name for name, score in pairs if score >= 70]
print(names)



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




































































































