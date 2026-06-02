
    Basic Dictionary in List Access
pythontasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'}
]
Question: How would you access the task name of the first item ('clean')?

tasks[0]['task'] → 'clean'
Pattern: list[index]['key'] - list position first, then dictionary key

for item in tasks:
    if item['task'] == 'clean':
        print(item['task'])

use a for loop when you dont know the index
Pattern: for item in list -> if item['key'] equal to 'value' -> print list-key name

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Accessing Nested Value
tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'}
]
Question: How would you access the status of the second item ('completed')?

tasks[1]['status'] → 'completed'
Pattern: list[index]['key'] - same pattern, different key

for item in tasks:
    if item['status'] == 'completed':
        print(item['task'])

use a for loop when you dont know the index
Pattern: for item in list -> if item['key'] equal to 'value' -> print list-key name

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Looping Through List of Dictionaries
tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'}
]
Question: Write a loop that prints each task name.

for item in tasks:
    print(item['task'])

Output:
clean
cook

Pattern: for item in list_of_dicts: then access item['key']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Finding Specific Dictionary
tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'}
]
Question: Write a loop that finds and returns the dictionary where task equals 'cook'. Return None if not found.

for item in tasks:
    if item['task'] == 'cook':
        return item
return None

Pattern:Loop through all items → return immediately when found → return None only if loop completes without finding
if the return None is inside the loop, so it would return None after checking only the first item.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete find_task Function
Question: Write a function called find_task that takes a list of tasks and a task_name, searches for it, and returns the dictionary or None.
tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'}
]

def find_task(tasks, task_name):
    for item in tasks:
        if item['task'] == task_name:
            return item
    return None

Pattern: Search function returns the found dictionary or None

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Checking if find_task Returned Something
task_name = 'clean'

task = find_task(tasks, task_name)  # Assume this returned a dictionary
Question: Write an if statement to check if task was NOT found (is None), and if so, print "Not found" and return.

if task is None:
    print('Not found')
    return
Pattern: if variable is None: - early return if search failed
if result is None: checks if find function returned nothing

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Modifying Status in Found Dictionary
tasks = [
    {'task': 'clean', 'status': 'pending'}
]
Question: Find the 'clean' task and change its status to 'completed'.

for item in tasks:
    if item['task'] == task_name:
        item['status'] = 'completed'

Pattern: find item then update its 'status'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Modifying Dictionary in List
tasks = [
    {'task': 'clean', 'status': 'pending'}
]
task = tasks[0]  # Reference to the dictionary
Question: Change the status to 'completed'.

task['status'] = 'completed'

Important concept: task is a reference to the dictionary in the list, not a copy. When you modify task, you modify the original in the list.
So after this, tasks[0]['status'] is also 'completed'.

Pattern: Modify dictionary reference to change original in list

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete mark_complete Pattern
Question: Write a function mark_complete that:

Gets task_name from input
Finds the task using find_task
Returns if not found
Changes its status to 'completed'
Prints confirmation

tasks = [
    {'task': 'clean', 'status': 'pending'}
]

def mark_complete():
    task_name = input("enter task: ")
    task = find_task(task_name)
    if task is None:
        print('Not Found')
        return
    task['status'] = 'completed'
    print(f"{task['task']} completed")

Pattern breakdown:
Get input
Find using helper function
Guard clause (early return if not found)
Modify dictionary reference (changes original)
Confirmation

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    List Comprehension Basics
numbers = [1, 2, 3, 4, 5]
Question: Use a list comprehension to create a new list with each number doubled.
Result should be: [2, 4, 6, 8, 10]

doubled = [num * 2 for num in numbers] → [2, 4, 6, 8, 10]
Pattern: [expression for item in list] creates new list by transforming each item

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    List Comprehension with Condition
numbers = [1, 2, 3, 4, 5, 6]
Question: Use list comprehension to get only the even numbers.
Result should be: [2, 4, 6]

even = [num for num in numbers if num % 2 == 0] → [2, 4, 6]
Pattern: [item for item in list if condition] - filters items that meet the condition

Regular loop equivalent:
even = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)

List comprehension is just shorthand!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    List Comprehension with Dictionaries
tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'},
    {'task': 'laundry', 'status': 'pending'}
]
Question: Use list comprehension to get just the task names (result: ['clean', 'cook', 'laundry'])

task_names = [item['task'] for item in tasks] → ['clean', 'cook', 'laundry']

Pattern: [item['key'] for item in list_of_dicts] - extract specific key from each dictionary

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    List Comprehension with Dictionary Filter
tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'},
    {'task': 'laundry', 'status': 'pending'}
]
Question: Use list comprehension to get only the task names where status is 'pending'.
Result should be: ['clean', 'laundry']

task_name = [item['task'] for item in tasks if item['status'] == 'pending'] → ['clean', 'laundry']
Pattern: [item['key'] for item in list_of_dicts if item['other_key'] == value]

    Regular loop equivalent:
task_name = []
for item in tasks:
    if item['status'] == 'pending':
        task_name.append(item['task'])

List comprehension does it in one line!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    List Comprehension Returning Whole Dictionaries
tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'},
    {'task': 'laundry', 'status': 'pending'}
]
Question: Use list comprehension to get all dictionaries where status is 'pending'.
Result should be the full dictionaries, not just task names.

task_name = [item for item in tasks if item['status'] == 'pending']
Result:
[
    {'task': 'clean', 'status': 'pending'},
    {'task': 'laundry', 'status': 'pending'}
]
Pattern: [item for item in list_of_dicts if condition] - keeps whole dictionaries that match

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Complete view_pending Function
Question: Write view_pending() function that:

Uses list comprehension to get pending task names
Checks if list is empty
Prints each task name

to_do = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'}
]

def view_pending():
    pending = [item['task'] for item in to_do if item['status'] == 'pending']
    if not pending:
        print('No pending tasks')
        return
    for task in pending:
        print(task)
Pattern - Complete function:

List comprehension filters
Check if empty (guard clause)
Loop and process


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
































