    Basic List Remove
colors = ['red', 'blue', 'green', 'yellow']
Question: Remove 'blue' from the list.

colors.remove('blue')

Pattern: list.remove(value) - finds and removes first occurrence of that value
Important: If value doesn't exist, it raises a ValueError. That's why you often check first.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Remove with Dictionary Reference
tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'}
]
task = tasks[0]  # Reference to first dictionary
Question: Remove the task dictionary from the tasks list.

tasks.remove(task)

#Output >>> tasks = [{'task': 'cook', 'status': 'completed'}]

Pattern: list.remove(dictionary_reference) - removes the dictionary object from the list

Key concept: When you do task = find_task(task_name), task holds a reference to the actual dictionary in the list.
When you call list.remove(task), Python removes that same dictionary object.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete Delete Pattern
tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'}
]
Question: Write code that:

Finds the task named 'clean' (assume find_task exists)
Checks if it was found
If found, removes it from tasks list
Prints confirmation

input_clean = 'clean'
remove_item = find_task(input_clean)
if remove_item is None:
    print('not found')
    return
tasks.remove(remove_item)
print('task removed')

Pattern:

Find using helper function
Guard clause - check if None
Early return if not found
Remove reference from list
Confirmation

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete delete_task Function
Question: Write the complete delete_task() function that:

Gets task name from input
Finds it using find_task
Returns if not found
Removes from to_do list
Prints confirmation

to_do = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'}
]

def find_task(task_name):
    for item in to_do:
        if item['task'] == task_name:
            return item  # Returns dictionary reference
    return None

def delete_task():
    task_name = input('enter name: ')
    remove_item = find_task(task_name)
    if remove_item is None:
        print('not found')
        return
    to_do.remove(remove_item)  # Removes using reference
    print('task removed')
Pattern breakdown:

Helper function returns dictionary reference (or None)
Get user input
Find using helper
Guard clause - early return if not found
.remove(reference) - removes the actual object
Confirmation

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    What Happens with .remove()
Quick concept check:
tasks = [
    {'task': 'clean', 'status': 'pending'},
    {'task': 'cook', 'status': 'completed'}
]
task = tasks[0]
tasks.remove(task)

tasks still contains a list with one item:
python[{'task': 'cook', 'status': 'completed'}]
The square brackets matter - its a list containing one dictionary, not just a dictionary.
Key concept: .remove() modifies the original list in place. It doesnt create a new list.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Removing While Looping (Common Mistake)
tasks = [
    {'task': 'clean', 'status': 'completed'},
    {'task': 'cook', 'status': 'completed'}
]
Question: Is this code safe? Why or why not?
for task in tasks:
    if task['status'] == 'completed':
        tasks.remove(task)

Problem: When you remove an item during iteration, the list shifts and you skip items.
Example walkthrough:

Loop at index 0: removes 'clean' → 'cook' shifts to index 0
Loop moves to index 1: but theres nothing there! 'cook' was skipped

Safe alternatives:
Option 1 - List comprehension (rebuild without completed):
tasks = [task for task in tasks if task['status'] != 'completed']

Option 2 - Loop backwards by index:
for i in range(len(tasks) - 1, -1, -1):
    if tasks[i]['status'] == 'completed':
        del tasks[i]

Option 3 - Use a copy for iteration (what you probably meant):
for task in tasks[:]:  # [:] creates a copy
    if task['status'] == 'completed':
        tasks.remove(task)

Your delete_task() is safe because it only removes ONE item then returns - not looping through and removing multiple.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

tasks = [task for task in tasks if task['status'] != 'completed']
Step by step:

The right side reads through the ORIGINAL tasks list (no modifications during this)
Builds a COMPLETELY NEW list with only items that match
The = assigns the NEW list to the variable name tasks

The original list is never modified during iteration - youre reading from one list and building another.
Compare to the broken version:
for task in tasks:
    tasks.remove(task)  # Modifying SAME list you're iterating
This modifies the list AS you loop through it - thats the problem.
Visual:
# Before
tasks = [{'task': 'clean', 'status': 'completed'},
         {'task': 'cook', 'status': 'pending'}]

# List comprehension reads original, builds new
new_list = [{'task': 'cook', 'status': 'pending'}]

# Then assigns
tasks = new_list
Safe because: read original → build new → replace pointer.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Adding Confirmation Before Delete
to_do = [
    {'task': 'clean', 'status': 'pending'}
]
Question: Write code that:

Gets a yes/no confirmation from user
Only proceeds if they type 'yes'
Returns early otherwise

confirm = input('are you sure yes/no: ')
if confirm != 'yes':
    return

Pattern: Negative check with early return - if NOT 'yes', stop here
Your program uses this in both delete_task() and mark_complete():

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete delete_task with Confirmation
Question: Write the complete delete_task() function that:

Gets task name
Finds it
Returns if not found
Gets confirmation
Returns if not 'yes'
Removes from list
Confirms deletion

to_do = [
    {'task': 'clean', 'status': 'pending'}
]

def find_task(task_name):
    for item in to_do:
        if item['task'] == task_name:
            return item
    return None

def remove_item():
    task_name = input('enter a task: ')
    delete_task = find_task(task_name)
    if delete_task is None:
        print('error not found')
        return
    confirmation = input('confirm choice yes/no: ')
    if confirmation != 'yes':
        return
    to_do.remove(delete_task)
    print('task removed')
Pattern - Complete delete flow:

Get input
Find using helper
Guard clause #1: not found
Get confirmation
Guard clause #2: not confirmed
.remove(reference) - actual deletion
User feedback

Two-stage guard clauses protect against both missing items AND accidental deletions.

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
