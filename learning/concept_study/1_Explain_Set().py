set() - What It Is

A set is a collection type like lists and dictionaries, but with two key rules:

No duplicates - automatically removes repeated values
No order - items dont have positions (no indexing like [0])


                    Black Box View

Input: Any iterable (list, string, tuple)
Output: A set with only unique values, no specific order
# From a list with duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4}

# From a string
letters = set("mississippi")
print(letters)  # {'m', 'i', 's', 'p'} - only unique letters


                    Key Behaviors

# Creating sets
empty_set = set()  # Must use set(), not {} (that's a dict)
my_set = {1, 2, 3}  # Can use curly braces with values

# Adding/removing
my_set.add(4)      # {1, 2, 3, 4}
my_set.add(2)      # Still {1, 2, 3, 4} - no duplicate added
my_set.remove(3)   # {1, 2, 4}

# NO indexing
my_set[0]  # ERROR - sets don't have positions


# Check membership (fast)
if 2 in my_set:
    print("Found it")


                    When Would I Use This?

1. Remove duplicates from a list:

emails = ["bob@email.com", "alice@email.com", "bob@email.com"]
unique_emails = list(set(emails))  # Convert back to list


2. Check if lists have common elements:

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)  # {3, 4}

3. Fast membership testing (checking if something exists):

# Checking 'in' is faster with sets than lists for large collections
valid_users = set(['alice', 'bob', 'charlie'])  # Fast lookup
if username in valid_users:  # Quicker than list
    print("Valid")


                    Set vs List vs Dict

Feature         List            Set             Dict
Order           Yes [0], [1]    No              No (keys)
Duplicates      Yes             No              No (keys)
Syntax          [1, 2]          {1, 2}          {'a': 1}
Use case        Ordered items   Unique items    Key-value pairs




                    Set Operations - Visual Examples

# Setup two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# ----- DIFFERENCE (-) -----
# "What's in set1 but NOT in set2?"
print(set1 - set2)  # {1, 2, 3}

# "What's in set2 but NOT in set1?"
print(set2 - set1)  # {6, 7, 8}


# ----- INTERSECTION (&) -----
# "What do they have in common?"
print(set1 & set2)  # {4, 5}


# ----- UNION (|) -----
# "Everything from both sets, no duplicates"
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}


# ----- SYMMETRIC DIFFERENCE (^) -----
# "What's in one or the other, but NOT both?"
print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}

                    Real-World Example

# Monday's customers
monday = {'Alice', 'Bob', 'Charlie', 'Dana'}

# Tuesday's customers
tuesday = {'Charlie', 'Dana', 'Eve', 'Frank'}

# Who came ONLY on Monday?
monday - tuesday  # {'Alice', 'Bob'}

# Who came ONLY on Tuesday?
tuesday - monday  # {'Eve', 'Frank'}

# Who came BOTH days?
monday & tuesday  # {'Charlie', 'Dana'}

# Who came AT LEAST once?
monday | tuesday  # {'Alice', 'Bob', 'Charlie', 'Dana', 'Eve', 'Frank'}

# Who came EXACTLY one day (not both)?
monday ^ tuesday  # {'Alice', 'Bob', 'Eve', 'Frank'}


                    Quick Reference

Operator            Name                    What it gives you

set1 - set2         Difference              Items in set1 but not set2
set2 - set1         Difference              Items in set2 but not set1
set1 & set2         Intersection            Items in BOTH
set1 | set2         Union                   Combines items
set1 ^ set2         Symmetric Difference    Items in ONE but not BOTH


                    Union - Both Methods

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Method 1: Using | operator
result = set1 | set2
print(result)  # {1, 2, 3, 4, 5}

# Method 2: Using .union() method
result = set1.union(set2)
print(result)  # {1, 2, 3, 4, 5}


                    Operator + Method Chart

What You Want           Operator            Method Version

Difference              set1 - set2         set1.difference(set2)
Intersection            set1 & set2         set1.intersection(set2)
Union                   set1 | set2         set1.union(set2)
Symmetric Diff          set1 ^ set2         set1.symmetric_difference(set2)











