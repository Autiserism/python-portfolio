'''
enumerate()
Write a program that takes a list of tasks and displays them numbered starting at 1.
Ask the user to pick a number.
Print the selected task.
Use enumerate() for the display and index-based access for the selection.
'''
tasks = ['do laundry', 'wash dishes', 'vacuum', 'cook dinner', 'walk dog']

for i, item in enumerate(tasks,1) :
    print(f"{i} {item}")

user_num = int(input("pick a task number: ")) -1
print(tasks[user_num])


















