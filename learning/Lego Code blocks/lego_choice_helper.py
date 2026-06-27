# ======================================================================
# LEGO CODE BLOCKS — CHOICE HELPERS
# lego_choice_helpers.py
# ======================================================================
# PURPOSE : Reusable input validation, enumerate pickers, and menu loops
# USE     : Open in Mu, find your block, copy what you need
# FILL-IN : string_var1, list_var1, dict_var1 etc. = rename to match
#           your data + follow the #<<<< comment on that line
# NOTE    : No imports needed for most blocks — all standard library
#           Add  import logging  at the top of your file to use the
#           logging lines (shown as optional comments inside blocks)
# ======================================================================


# ======================================================================
# SECTION 1 — INPUT VALIDATORS
# ======================================================================
# These are standalone functions — drop whichever ones you need into
# your project and call them anywhere you take user input.
# ======================================================================


# ======================================================================
# BLOCK CHOICE-1 — Yes / No Confirmation
# ======================================================================
# DESCRIPTION : Asks a yes/no question and loops until the user types
#               'yes' or 'no'. Returns True for yes, False for no.
#               Useful before any destructive or important action.
# FEEDS       : a prompt string describing what you're confirming
# RETURNS     : True (yes) or False (no)
# TAGS        : confirm, yes, no, validation, bool, input
# ======================================================================

def confirm(prompt_var1):   #<<<< rename prompt_var1 or hardcode the message below
    while True:
        answer = input(f'{prompt_var1} (yes/no): ').strip().lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("Type 'yes' or 'no'.")

# — Usage
if confirm('Are you sure you want to delete this?'):   #<<<< your message
    print('Confirmed.')
else:
    print('Cancelled.')


# ======================================================================
# BLOCK CHOICE-2 — Validated String Input (Not Blank)
# ======================================================================
# DESCRIPTION : Keeps asking until the user types something non-empty.
#               Optional: enforce a minimum and/or maximum character length.
#               Returns the cleaned string (stripped, lowercased).
# FEEDS       : a prompt string
# RETURNS     : a non-empty string, stripped and lowercased
# TAGS        : string, input, validate, not blank, length, strip
# ======================================================================

def get_string(prompt_var1, min_len=1, max_len=None):   #<<<< set min/max or leave defaults
    while True:
        value = input(prompt_var1).strip().lower()
        if len(value) < min_len:
            print(f'Must be at least {min_len} character(s).')
            continue
        if max_len and len(value) > max_len:
            print(f'Must be {max_len} characters or fewer.')
            continue
        return value

# — Usage
string_var1 = get_string('Enter a name: ')                       # just not blank
string_var1 = get_string('Enter a name: ', min_len=3)            # at least 3 chars
string_var1 = get_string('Enter a tag: ',  min_len=2, max_len=10)# between 2 and 10


# ======================================================================
# BLOCK CHOICE-3 — Validated Integer Input (Optional Range)
# ======================================================================
# DESCRIPTION : Keeps asking until the user enters a valid integer.
#               Optional: enforce a minimum and/or maximum value.
#               try/except catches anything that isn't a whole number.
# FEEDS       : a prompt string
# RETURNS     : a valid integer within the optional range
# TAGS        : int, integer, input, validate, range, try except
# ======================================================================

def get_int(prompt_var1, min_val=None, max_val=None):   #<<<< set range or leave as None
    while True:
        try:
            value = int(input(prompt_var1).strip())
        except ValueError:
            print('Enter a whole number.')
            continue
        if min_val is not None and value < min_val:
            print(f'Must be {min_val} or higher.')
            continue
        if max_val is not None and value > max_val:
            print(f'Must be {max_val} or lower.')
            continue
        return value

# — Usage
int_var1 = get_int('Enter a number: ')                         # any integer
int_var1 = get_int('Enter a number (1-10): ', min_val=1, max_val=10)
int_var1 = get_int('Enter your age: ',        min_val=0)       # 0 or higher only


# ======================================================================
# BLOCK CHOICE-4 — Validated Float Input (Positive Amount)
# ======================================================================
# DESCRIPTION : Keeps asking until the user enters a valid positive number.
#               Pattern from W2P5 bank account get_amount().
#               Returns None if you want the caller to handle a cancel case
#               — swap the return None for a continue if you want hard retry.
# FEEDS       : a prompt string
# RETURNS     : a positive float, or None if input was invalid
# TAGS        : float, amount, positive, input, validate, try except, money
# ======================================================================

def get_amount(prompt_var1='Enter amount: '):   #<<<< change default prompt if needed
    try:
        amount = float(input(prompt_var1).strip())
        if amount <= 0:
            print('Must be a positive number.')
            return None
        return amount
    except ValueError:
        print('Invalid input — enter a number.')
        return None

# — Hard retry version (keeps looping until valid, no None return)
def get_amount_strict(prompt_var1='Enter amount: '):
    while True:
        try:
            amount = float(input(prompt_var1).strip())
            if amount <= 0:
                print('Must be a positive number.')
                continue
            return amount
        except ValueError:
            print('Invalid input — enter a number.')


# ======================================================================
# BLOCK CHOICE-5 — Attempt-Limited Input (Lockout After N Tries)
# ======================================================================
# DESCRIPTION : Gives the user a fixed number of attempts before locking
#               them out. Returns the valid value on success, or None when
#               attempts are exhausted. Pattern from W2P4 login system.
# FEEDS       : a prompt string and a dict/list to check the input against
# RETURNS     : the entered value if valid, or None after too many failures
# TAGS        : attempts, lockout, login, limit, retry, tries
# ======================================================================

MAX_ATTEMPTS = 3   #<<<< change the attempt limit here

def limited_input(prompt_var1, valid_options):
    #<<<< valid_options = list or dict of accepted values
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        value = input(prompt_var1).strip().lower()
        if value in valid_options:
            return value
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f'Invalid. {remaining} attempt(s) remaining.')
        else:
            print('Too many failed attempts. Locked out.')
    return None   # caller checks for None to handle the lockout

# — Usage
result = limited_input('Enter your PIN: ', ['1234', '0000'])   #<<<< your valid options
if result is None:
    print('Access denied.')
else:
    print(f'Accepted: {result}')


# ======================================================================
# SECTION 2 — ENUMERATE PICKERS
# ======================================================================
# These blocks display a numbered list and return what the user picked.
# The key pattern: build a tmp list in parallel while printing so you can
# map a number back to the item — needed when iterating a dict (dicts
# don't support index access directly).
# ======================================================================


# ======================================================================
# BLOCK CHOICE-6 — Print a Numbered List (Standalone Display Utility)
# ======================================================================
# DESCRIPTION : Prints any list or dict with numbers beside each item.
#               Use this any time you want to show options before asking
#               the user to pick. Works standalone or paired with the
#               picker blocks below.
# FEEDS       : a list or dict
# RETURNS     : nothing — prints to terminal; also works returning the tmp list
# TAGS        : enumerate, print, numbered, list, display, menu
# ======================================================================

# — Print from a list
list_var1 = ['Option A', 'Option B', 'Option C']   #<<<< your list

for num, item in enumerate(list_var1, 1):
    print(f'{num}. {item}')

# — Print from a dict (keys only)
dict_var1 = {'apples': 3, 'bananas': 5, 'oranges': 2}   #<<<< your dict

for num, key in enumerate(dict_var1, 1):
    print(f'{num}. {key}')

# — Print from a list of dicts (show specific fields)
records = [{'name': 'Alice', 'score': 92}, {'name': 'Bob', 'score': 85}]   #<<<< your records

for num, item in enumerate(records, 1):
    print(f"{num}. {item['name']} — {item['score']}")   #<<<< your field names

# — Print with a header and divider
print(f"\n{'— Options ':-<30}")
for num, item in enumerate(list_var1, 1):
    print(f'  {num}. {item}')
print()


# ======================================================================
# BLOCK CHOICE-7 — Pick From a List by Number (choice_helper pattern)
# ======================================================================
# DESCRIPTION : Displays a numbered list, asks for a number, and returns
#               the selected item. Validates with try/except so a bad
#               entry just loops — no crash.
#               This is the choice_helper() you wrote in M1P6, formalized.
# FEEDS       : list_var1 — any list of items to choose from
# RETURNS     : the item at the chosen index
# TAGS        : enumerate, pick, list, choice, number, try except, selection
# ======================================================================

def pick_from_list(list_var1, prompt_var1='Enter a number: '):
    #<<<< list_var1 = your list of options | prompt_var1 = question to ask
    for num, item in enumerate(list_var1, 1):
        print(f'{num}. {item}')
    while True:
        try:
            value = list_var1[int(input(prompt_var1).strip()) - 1]
        except ValueError:
            print('Invalid — enter a number.')
            continue
        except IndexError:
            print(f'Enter a number between 1 and {len(list_var1)}.')
            continue
        return value

# — Usage
list_var1   = ['Small', 'Medium', 'Large']          #<<<< your options
prompt_var1 = 'Pick a size: '                       #<<<< your prompt
selected    = pick_from_list(list_var1, prompt_var1)
print(f'You chose: {selected}')

# — One-liner version (compact, no function needed for simple cases)
options = ['easy', 'normal', 'hard']
for i, o in enumerate(options, 1): print(f'{i}. {o}')
choice = options[int(input('Pick: ')) - 1]   # wrap in try/except if user input is unpredictable


# ======================================================================
# BLOCK CHOICE-8 — Pick From a Dict by Number (tmp list pattern)
# ======================================================================
# DESCRIPTION : Dicts don't support index access — you can't do dict[1].
#               The fix: build a tmp list of keys in parallel while printing
#               so you can map a number back to the key after the user picks.
#               Pattern from M1P2 expense tracker add_expense_menu().
# FEEDS       : dict_var1 — any dict where you want to pick a key by number
# RETURNS     : the key (string) the user selected
# TAGS        : enumerate, dict, pick, tmp list, number, selection, key
# ======================================================================

def pick_from_dict(dict_var1, prompt_var1='Enter a number: '):
    #<<<< dict_var1 = your dict | prompt_var1 = question to ask
    tmp = []
    for num, key in enumerate(dict_var1, 1):
        print(f'{num}. {key}')
        tmp.append(key)   # tmp mirrors the print order — tmp[0] = what printed as "1."
    while True:
        try:
            selected_key = tmp[int(input(prompt_var1).strip()) - 1]
        except ValueError:
            print('Invalid — enter a number.')
            continue
        except IndexError:
            print(f'Enter a number between 1 and {len(tmp)}.')
            continue
        return selected_key   # returns the KEY — use dict_var1[selected_key] to get the value

# — Usage
dict_var1    = {'Groceries': {}, 'Rent': {}, 'Transport': {}}   #<<<< your dict
prompt_var1  = 'Select a category: '                            #<<<< your prompt
selected_key = pick_from_dict(dict_var1, prompt_var1)
print(f'Selected: {selected_key}')
print(f'Value: {dict_var1[selected_key]}')   # get the value at that key


# ======================================================================
# BLOCK CHOICE-9 — Pick From a List + Keyword Options (quit / new / back)
# ======================================================================
# DESCRIPTION : Enumerate picker that also accepts special keyword commands
#               like 'quit', 'new', or 'back' alongside numbered choices.
#               Returns the selected item, or a keyword string so the caller
#               can decide what to do.
#               Pattern from M1P2 add_expense_menu() — the 'new' / 'quit'
#               handling you wrote there, generalized.
# FEEDS       : list_var1 — options to display | keywords — accepted commands
# RETURNS     : selected item from the list, or one of the keyword strings
# TAGS        : enumerate, keywords, quit, new, back, pick, menu, combined
# ======================================================================

# keywords the user can type instead of a number — add/remove as needed
KEYWORDS = ['quit', 'new', 'back']   #<<<< edit this list to match your commands

def pick_or_keyword(list_var1, prompt_var1='Enter a number or command: '):
    tmp = []
    for num, item in enumerate(list_var1, 1):
        print(f'{num}. {item}')
        tmp.append(item)
    print()
    for kw in KEYWORDS:
        print(f"  Type '{kw}' to {kw}")   #<<<< adjust the description per keyword if needed
    print()
    while True:
        raw = input(prompt_var1).strip().lower()
        if raw in KEYWORDS:
            return raw   # caller checks: if result == 'quit': break
        try:
            selected = tmp[int(raw) - 1]
        except ValueError:
            print('Enter a number or a valid command.')
            continue
        except IndexError:
            print(f'Enter a number between 1 and {len(tmp)}.')
            continue
        return selected

# — Usage
list_var1   = ['Category A', 'Category B', 'Category C']   #<<<< your options
result      = pick_or_keyword(list_var1, 'Pick a category: ')

if result == 'quit':
    print('Exiting.')
elif result == 'new':
    print('Creating new item...')   #<<<< call your new-item function here
elif result == 'back':
    print('Going back.')
else:
    print(f'You selected: {result}')   # it's a real list item


# ======================================================================
# SECTION 3 — MENU LOOPS
# ======================================================================
# Full while True menu loops — show options, get input, route to a function.
# ======================================================================


# ======================================================================
# BLOCK CHOICE-10 — Simple Numbered Menu Loop (if / elif dispatch)
# ======================================================================
# DESCRIPTION : The standard menu loop. Prints options, reads a number,
#               routes to the right function with if/elif. Loops until
#               the user picks quit.
#               Clean for 3–5 options — use the dispatch dict (CHOICE-11)
#               when you have more.
# FEEDS       : nothing — the loop drives itself
# RETURNS     : nothing — calls functions based on user choice
# TAGS        : menu, loop, while True, if elif, numbered, dispatch, quit
# ======================================================================

# — Your action functions (replace with real ones)
def action_one():
    print('Running action one...')   #<<<< replace with your function body

def action_two():
    print('Running action two...')   #<<<< replace

def action_three():
    print('Running action three...')   #<<<< replace

# — The menu loop
def main_menu():
    while True:
        print('\n--- MENU ---')         #<<<< your menu title
        print('1. Do thing one')        #<<<< your option labels
        print('2. Do thing two')
        print('3. Do thing three')
        print('4. Quit')
        choice = input('\nEnter a number: ').strip()
        if choice == '1':
            action_one()
        elif choice == '2':
            action_two()
        elif choice == '3':
            action_three()
        elif choice == '4':
            print('Goodbye.')
            break
        else:
            print('Invalid choice — enter 1, 2, 3, or 4.')

main_menu()


# ======================================================================
# BLOCK CHOICE-11 — Menu Loop With Dispatch Dict (scales cleanly)
# ======================================================================
# DESCRIPTION : Instead of a long if/elif chain, maps each menu number
#               to a function in a dict. Adding a new option means adding
#               one line to the dict — no restructuring the if/elif chain.
#               Better than CHOICE-10 once you have 5+ options.
# FEEDS       : nothing — the loop and dispatch dict drive themselves
# RETURNS     : nothing — routes to functions based on user choice
# TAGS        : menu, loop, dispatch, dict, function, scalable, numbered
# ======================================================================

# — Your action functions (replace with real ones)
def view_all():
    print('Viewing all...')    #<<<< replace

def add_item():
    print('Adding item...')    #<<<< replace

def delete_item():
    print('Deleting item...')  #<<<< replace

def show_stats():
    print('Stats...')          #<<<< replace

# — Dispatch dict: maps option number (as string) to (label, function)
menu_options = {
    '1': ('View all',    view_all),     #<<<< ('label', function_name) — no () on the function
    '2': ('Add item',    add_item),
    '3': ('Delete item', delete_item),
    '4': ('Stats',       show_stats),
    '5': ('Quit',        None),         # None = the quit signal
}

def main_menu():
    while True:
        print('\n--- MENU ---')
        for key, (label, _) in menu_options.items():
            print(f'{key}. {label}')
        choice = input('\nEnter a number: ').strip()
        if choice not in menu_options:
            print(f'Enter a number between 1 and {len(menu_options)}.')
            continue
        label, func = menu_options[choice]
        if func is None:     # it's the quit option
            print('Goodbye.')
            break
        func()               # call the function mapped to that number

main_menu()
