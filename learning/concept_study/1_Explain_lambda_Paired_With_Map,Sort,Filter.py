                    Lambda Functions - What They Are

A lambda is a tiny, one-line anonymous function. Think of it as a function shortcut for simple operations.

    Key traits:

No name (anonymous)
One line only
Automatically returns the result (no return keyword)
Used when you need a quick function and dont want to write a full def.


                    Regular Function vs Lambda - Side by Side

# REGULAR FUNCTION
def add_ten(x):
    return x + 10

result = add_ten(5)  # 15


# LAMBDA - SAME THING
add_ten = lambda x: x + 10

result = add_ten(5)  # 15
The Pattern
# Regular function
def function_name(parameters):
    return expression

# Lambda equivalent
lambda parameters: expression
No def, no return, no name needed - just the logic.

Breaking Down the Syntax
lambda x: x * 2
  ↓    ↓  ↓
  |    |  └── What to return (the expression)
  |    └── Parameter(s) the function takes
  └── Keyword that says "this is a lambda"
More Examples
 # One parameter
square = lambda x: x ** 2
print(square(4))  # 16

# Two parameters
multiply = lambda x, y: x * y
print(multiply(3, 5))  # 15

# Three parameters
volume = lambda length, width, height: length * width * height
print(volume(2, 3, 4))  # 24

# No parameters (rare but valid)
get_pi = lambda: 3.14159
print(get_pi())  # 3.14159

When Would I Use Lambda?
You almost NEVER use lambda alone like above - that defeats the purpose. You use it when passing a function to another function.
Use Case 1: sorted() with Custom Sorting
 # Sort list of tuples by the second value
pairs = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]

# WITHOUT lambda (need to define a whole function)
def get_second(item):
    return item[1]
sorted_pairs = sorted(pairs, key=get_second)

# WITH lambda (one line)
sorted_pairs = sorted(pairs, key=lambda item: item[1])
print(sorted_pairs)  # [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
Whats happening:

sorted() needs to know HOW to sort
key= expects a function
Lambda creates that function on the spot

 # Sort dictionaries by a specific key
employees = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# Sort by age
sorted_by_age = sorted(employees, key=lambda emp: emp['age'])
print(sorted_by_age)
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Sort by name length
sorted_by_name_len = sorted(employees, key=lambda emp: len(emp['name']))

Use Case 2: map() - Apply Function to Each Item
 numbers = [1, 2, 3, 4, 5]

# WITHOUT lambda
def double(x):
    return x * 2
doubled = list(map(double, numbers))

# WITH lambda
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
Whats happening:

map() applies a function to every item in the list
Lambda is that function

 # More examples
names = ['alice', 'bob', 'charlie']

# Capitalize each name
caps = list(map(lambda name: name.upper(), names))
# ['ALICE', 'BOB', 'CHARLIE']

# Get length of each name
lengths = list(map(lambda name: len(name), names))
# [5, 3, 7]

Use Case 3: filter() - Keep Only Items That Pass a Test
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# WITHOUT lambda
def is_even(x):
    return x % 2 == 0
evens = list(filter(is_even, numbers))

# WITH lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]
Whats happening:

filter() keeps items where the function returns True
Lambda is the test function

 # More examples
words = ['cat', 'elephant', 'dog', 'butterfly']

# Keep words longer than 3 letters
long_words = list(filter(lambda word: len(word) > 3, words))
# ['elephant', 'butterfly']

# Keep words starting with 'c'
c_words = list(filter(lambda word: word[0] == 'c', words))
# ['cat']

Real-World Example - All Together
 # List of products
products = [
    {'name': 'Laptop', 'price': 1200, 'stock': 5},
    {'name': 'Mouse', 'price': 25, 'stock': 0},
    {'name': 'Keyboard', 'price': 75, 'stock': 10},
    {'name': 'Monitor', 'price': 300, 'stock': 3}
]

# Get only in-stock items
in_stock = list(filter(lambda p: p['stock'] > 0, products))

# Sort by price (cheapest first)
sorted_by_price = sorted(in_stock, key=lambda p: p['price'])

# Get just the names
names = list(map(lambda p: p['name'], sorted_by_price))

print(names)  # ['Mouse', 'Keyboard', 'Monitor', 'Laptop']

Lambda vs Regular Function - When to Use Which
Use Lambda When:
✅ The function is ONE simple expression
✅ You need it RIGHT NOW for sorted(), map(), filter()
✅ Youll never use it again
Use Regular Function When:
✅ Logic is multiple lines
✅ You need if/else statements (lambdas can do simple ones but it gets messy)
✅ Youll use the function multiple times
✅ You want a descriptive name for readability

Limitations of Lambda
 # ❌ CAN'T do multiple lines
lambda x:
    result = x * 2
    return result  # SYNTAX ERROR

# ❌ CAN'T have statements (only expressions)
lambda x: print(x)  # Works but bad practice (print is a statement)

# ✅ CAN do simple conditionals (but gets ugly)
lambda x: 'even' if x % 2 == 0 else 'odd'

Common Patterns Cheat Sheet
 # Sort by specific attribute
sorted(items, key=lambda item: item['attribute'])

# Transform each item
list(map(lambda x: x * 2, numbers))

# Filter by condition
list(filter(lambda x: x > 10, numbers))

# Sort descending
sorted(items, key=lambda x: x, reverse=True)

# Sort by multiple criteria (length, then alphabetical)
sorted(words, key=lambda w: (len(w), w))

Practice Translation
Try converting these regular functions to lambdas:
 # 1. Regular
def is_positive(num):
    return num > 0

# Lambda version
lambda num: num > 0


# 2. Regular
def get_last_char(string):
    return string[-1]

# Lambda version
lambda string: string[-1]


# 3. Regular
def calculate_area(width, height):
    return width * height

# Lambda version
lambda width, height: width * height
