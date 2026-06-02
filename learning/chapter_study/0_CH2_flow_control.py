# CH2 - Flow Control
# Input -> compare -> decide -> output

print("Welcome to the grade checker.")
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

if grade == "F":
    print(f"You scored {score}. Grade: {grade}. You need to retake the exam.")
elif grade in ["A", "B"]:
    print(f"You scored {score}. Grade: {grade}. Great work!")
else:
    print(f"You scored {score}. Grade: {grade}. Keep it up.")
'''
Plain English logic walk through:

1 Ask user for a score, convert to integer
2 Check score against grade boundaries from highest to lowest
3 Assign the correct grade letter
4 Check the grade and print an appropriate message
5 Uses in to check if grade is in a list instead of writing two separate conditions
'''

Examples


"1. If / Elif / Else"
if _______:
    _______
elif _______:
    _______
else:
    _______


if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
'''
Plain English:
Check a condition. If it's True run the first block. If not check the next condition.
If nothing matches run the else block. Only one block ever runs.

Use cases:
Checking user input against valid options
Categorizing values into groups
Any decision the program needs to make
'''


"2. Comparison Operators"
_______ == _______   # equal to
_______ != _______   # not equal to
_______ > _______    # greater than
_______ < _______    # less than
_______ >= _______   # greater than or equal to
_______ <= _______   # less than or equal to


if score == 100:
if name != "admin":
if age >= 18:
if price <= 50:
'''
Plain English:
Compare two values. Returns True or False. = assigns a value, == compares two values — never mix these up.

Use cases:
Any condition inside an if statement
'''


"3. Boolean Operators"
if _______ and _______:
if _______ or _______:
if not _______:


if age >= 18 and has_id == True:
    print("Allowed")

if is_admin or is_moderator:
    print("Access granted")

if not is_banned:
    print("Welcome")
'''
Plain English:
and — both conditions must be True
or — at least one condition must be True
not — flips True to False and False to True

Use cases:
Checking multiple conditions at once
Simplifying complex if statements
'''


"4. Checking Membership"
if _______ in _______:
if _______ not in _______:


if name in valid_users:
    print("Welcome")


if item not in inventory:
    print("Out of stock")
'''
Plain English:
Check if a value exists inside a list, string or dictionary. Returns True or False.

Use cases:
Checking if a user is in a list
Checking if a word is in a string
Checking if a key is in a dictionary
'''


"5. Nested If Statements"
if _______:
    if _______:
        _______
    else:
        _______
else:
    _______


if has_ticket:
    if age >= 18:
        print("Enter adult section")
    else:
        print("Enter general section")
else:
    print("No ticket, no entry")
'''
Plain English:
An if statement inside another if statement. The inner block only runs if the outer condition is True first.

Use cases:
Checking multiple layered conditions
Access control with multiple requirements
'''









