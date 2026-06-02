
    Creating a Dictionary Literal
Question: Create a dictionary with keys 'task' and 'status', where task is 'exercise' and status is 'pending'.

{'task': 'exercise', 'status': 'pending'}

Pattern: {'key': value, 'key': value} - dictionary literal

This is what youll append to the list.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Appending Dictionary to List

to_do = [
    {'task': 'clean', 'status': 'pending'}
]

Question: Append a new dictionary with task='cook' and status='pending' to the to_do list.

new = {'task': 'cook', 'status': 'pending'}
to_do.append(new)

Also works inline (your programs pattern):

to_do.append({'task': 'cook', 'status': 'pending'})

Both are identical - the inline version just skips the intermediate variable.
Pattern: list.append({dictionary_literal}) - adds new dictionary to end of list

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Inline Append with Variable
to_do = []
task_name = 'exercise'
Question: Append a dictionary to to_do where task equals task_name and status is 'pending'
(use the variable, not the string 'exercise').

to_do.append({'task': task_name, 'status': 'pending'})

Pattern: list.append({'key': variable, 'key': 'literal'}) - mix variables and literals
This is for the add_task() function pattern

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Checking for Duplicates Before Adding
to_do = [
    {'task': 'clean', 'status': 'pending'}
]
task_name = 'clean'
Question: Write code that checks if task_name already exists (using find_task).
If it does, print "already exists" and return. Otherwise, append it.

find_task should just find (not print messages) - keep it pure

def find_task(task_name):
    for item in to_do:
        if item['task'] == task_name:
            return item  # Found it
    return None  # Not found

task_name = 'clean'
existing = find_task(task_name)
if existing is not None:  # If it WAS found
    print('already exists')
    return
# Only runs if NOT found
to_do.append({'task': task_name, 'status': 'pending'})
Key: find_task returns dictionary if found, None if not found. So is not None means "already exists".

Pattern:

Search for existing
If found (not None) → reject duplicate
If not found (None) → safe to add

Key logic: is not None = exists, so DONT add

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete add_task Function
Question: Write the complete add_task() function that:

Gets task name from input (lowercase it)
Checks if it already exists
If exists, print message and return
Otherwise, append new dictionary with 'pending' status
Print confirmation

to_do = []

def find_task(task_name):
    for item in to_do:
        if item['task'] == task_name:
            return item
    return None

def add_task():
    task_name = input('enter a task: ').lower()
    new_task = find_task(task_name)
    if new_task is not None:
        print('already exists')
        return
    to_do.append({'task': task_name, 'status': 'pending'})
    print('task added')

Pattern - Complete add flow:
Get input (normalized with .lower())
Check for duplicate using helper function
Guard clause: if exists, reject and return
.append({dictionary}) - add new item
Confirmation

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Adding with Different Default Status
tasks = []
Question: Write a function add_completed_task() that adds a task with status='completed' instead of 'pending'.
(Skip duplicate check for this drill)

def add_completed_task():
    task_name = input('enter task: ')
    tasks.append({'task': task_name, 'status': 'completed'})

Pattern: Same structure, just change the value in the dictionary literal

You could even make it flexible:
def add_task_with_status(status):
    task_name = input('enter task: ')
    tasks.append({'task': task_name, 'status': status})

Then call: add_task_with_status('pending') or add_task_with_status('completed')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Adding Multiple Keys
tasks = []
Question: Create a dictionary with keys 'task', 'status', 'priority' (values: 'exercise', 'pending', 'high') and append it to tasks.

tasks.append({'task': 'exercise', 'status': 'pending', 'priority': 'high'})

Pattern: list.append({'key': value, 'key': value, 'key': value}) - as many keys as needed

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Building Dictionary from Multiple Inputs
tasks = []
Question: Write code that:

Gets task name from input
Gets priority from input ('high' or 'low')
Appends dictionary with those values plus status='pending'

task_name = input('enter a task: ')
priority = input('enter the priority high/low: ')
tasks.append({'task': task_name, 'status': 'pending', 'priority': priority})

Pattern: Collect multiple inputs → append dictionary with mix of variables and literals

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Printing with Numbers (1-indexed)
pending = ['clean', 'laundry', 'exercise']
Question: Write a loop that prints:
1 clean
2 laundry
3 exercise

for i in range(len(pending)):
    index = i + 1
    item = pending[i]
    print(index, item)

Pattern: Loop through indices → create display number (i + 1) → print with actual item

Alternative (using enumerate):
for i, item in enumerate(pending, start=1):
    print(i, item)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Getting User Selection
The user sees:
1 clean
2 laundry
Question: Get their selection as int, then convert it back to 0-indexed to access the list.

user_input = int(input('make a selection: ')) - 1

Pattern: User picks 1-indexed number → subtract 1 → get 0-indexed position
Example: User types 2 → 2 - 1 = 1 → access pending[1]

Important: Should validate range, but the conversion pattern is right.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Complete Selection Flow
pending_tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'laundry', 'status': 'pending'}
]
Question:

Print numbered list
Get user selection
Convert to 0-indexed
Print the selected tasks name

for i in range(len(pending_tasks)):
    index = i + 1
    items = pending_tasks[i]['task']
    print(index, items)
user_input = int(input('make a selection: ')) - 1
print(pending_tasks[user_input]['task'])
Pattern: Display numbered → get selection → convert to index → access list

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
