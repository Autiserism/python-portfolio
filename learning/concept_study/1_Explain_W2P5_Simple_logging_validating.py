    Basic Logging Setup
Question: Write the import and basicConfig line to set up logging at DEBUG level.

Pattern: logging.basicConfig(level=logging.DEBUG) - its a function call with level= parameter

logging.basicConfig(level=logging.DEBUG)
Pattern: logging.basicConfig(level=logging.LEVEL_NAME)

Common levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Writing a Debug Log
Question: Write a logging statement that logs "deposit initiated" at DEBUG level.

logging.debug('deposit initiated')
Pattern: logging.debug('message') - logs at DEBUG level

Other levels: logging.info(), logging.warning(), logging.error(), logging.critical()

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Logging with Variables
amount = 50.0
account = 'checking'
Question: Write a logging statement that logs "deposited 50.0 to checking" using f-string.

logging.debug(f'deposited {amount} into {account}')
Pattern: logging.debug(f'text {variable} text {variable}') - f-strings work in logging

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Logging Warning
balance = 100
withdrawal = 200
Question: Write a logging statement at WARNING level that says "insufficient funds checking".

logging.warning('insufficient funds checking')
Pattern: logging.warning('message') - logs at WARNING level (higher priority than DEBUG/INFO)

Warnings are for things that arent errors but need attention (like insufficient funds).

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Global Variables Declaration
balance = 1000.0
Question: Write a function called deposit that modifies the global balance variable by adding 100.

def deposit():
    global balance
    balance += 100
Pattern: global variable_name at top of function before modifying

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Multiple Global Variables
pythonchecking = 1000.0
savings = 5000.0
Question: Write a function that declares both as global and adds 50 to checking.

def MGV():
    global checking, savings
    checking += 50
Pattern: global var1, var2, var3 - comma-separated list to declare multiple globals

You only need to list the ones youll modify, but declaring both is safe even if you only change one.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Try/Except with Float Input
Question: Write a try/except block that gets a float input. If ValueError, print "Invalid input" and return None.

try:
    amount = float(input('Enter Amount: '))
    return amount
except ValueError:
    print('Invalid input')
    return None
Pattern: Try to convert input → return value on success → catch ValueError → return None on failure

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Validating Positive Numbers
Question: Expand the try/except to also check if amount is positive. If not, print "Must be positive" and return None.

try:
    amount = float(input('Enter amount: '))
    if amount <= 0:  # Check bad case first
        print('Must be positive')
        return None
    return amount  # Good case
except ValueError:
    print('Enter a valid input')

Pattern: Try to convert input -> checks amount returns amount on success -> catch ValueError → return None on failure

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete get_amount() Function
Question: Write the complete get_amount() function that validates float input and ensures its positive.

def get_amount():
    try:
        amount = float(input("Enter Amount: "))
        if amount <= 0:
            print('Must be positive')
            return None
        else:
            return amount
    except ValueError:
        print("invalid input")
        return None

Pattern: Validation function returns value or None - caller checks the result
Note: The else is optional - you could just return amount after the if block. Both work.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Using get_amount() in Another Function
Question: Write a function that calls get_amount(), and only proceeds if it returns a valid amount (not None).

def if_valid():
    amount = get_amount()
    if amount == None:
        return
    else:
        print(amount)

More Pythonic: if amount is None: (use is for None checks, not ==)

Note: The else is optional since you return in the if block:
def if_valid():
    amount = get_amount()
    if amount is None:
        return
    print(amount)  # Only runs if amount is valid
Both work!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    List Append for Transaction History
transactions = []
amount = 50.0
Question: Append a transaction string "Deposit: +$50.00" to the transactions list.

transactions.append("Deposit: +$50.00")

(with f-string formatting):

transactions.append(f'Deposit checking: +${amount:.2f}')

The .2f formats the float to 2 decimal places.
Pattern: list.append('string') or list.append(f'text {variable:.2f}')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Formatting Float to 2 Decimals
amount = 50.5
account = 'savings'
Question: Create a formatted string "Deposit savings: +$50.50" using f-string with 2 decimal formatting.

f'Deposit in {account}: +${amount:.2f}'

Pattern: f'{variable:.2f}' - formats float to 2 decimal places

The parentheses aren't needed unless you're using this in an expression.
format: f'Deposit savings: +${amount:.2f}'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Looping Through List and Printing
transactions = ['Deposit: +$50.00', 'Withdrawal: -$20.00']
Question: Write a for loop that prints each transaction.

for transaction in transactions:
    print(transaction)

Pattern: for item in list: - loops through each element

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Check if List is Empty Before Looping
pythontransactions = []
Question: Write code that checks if transactions is empty. If empty, print "no transactions". Otherwise, loop and print each one.

if not transactions:
    print("no transactions")
else:
    for transaction in transactions:
        print(transaction)

Pattern: if not list: checks if list is empty (empty lists are falsy)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Password Verification Function
Question: Write a function verify_password() that:

Takes password input
Compares to 'secret123'
Returns False and prints "Access denied" if wrong
Returns True if correct

def verify_password():
    password = input("enter the password: ")
    if password != 'secret123':
        print("Access denied")
        return False
    return True
Pattern: Get input → check condition → return False early if bad → return True if good (implicit else)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Using Password Verification
Question: Write code that calls verify_password() and returns early from the current function if verification fails.

if verify_password() is False: # works But theres a better way
    return

More Pythonic:

if not verify_password():
    return

Both work identically:

if verify_password() is False: - explicit comparison
if not verify_password(): - more concise (idiomatic Python)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Menu with try/except
Question: Write a while True loop that:

Prints "1. Deposit  2. Quit"
Gets input as int
Catches ValueError and continues
Breaks on 2

while True:
    try:
        choice = int(input("1. Deposit  2. Quit"))
    except ValueError:
        print('invalid')
        continue
    if choice == 1:
        Deposit()
    elif choice == 2:
        break

Pattern: Try input conversion → catch ValueError → continue (restarts loop) → process valid input

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Insufficient Funds Check
balance = 100.0
withdrawal = 150.0
Question: Write code that checks if withdrawal exceeds balance. If yes, print "insufficient funds", log a warning, and return.

import logging
logging.basicConfig(level=logging.DEBUG)

if withdrawal > balance:
    print("insufficient funds")
    logging.warning("insufficient funds")
    return

Pattern: Check condition → user message → log warning → early return

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete Withdrawal Function Structure
Question: Write a function withdraw() that:

Declares balance as global
Gets amount using get_amount()
Returns early if amount is None
Checks insufficient funds (prints, logs warning, returns if true)
Otherwise subtracts amount and prints remaining balance

balance = 1000.0

def withdraw():
    global balance
    amount = get_amount()
    if amount is None:
        return
    if amount > balance:
        logging.warning("insufficient funds")
        print("insufficient funds")
        return
    balance -= amount
    print(f"{balance} remaining")
    logging.debug(f"{amount} withdrawn")

Pattern breakdown:

global declaration
Get validated input
Early return if invalid
Guard clause for business rule (insufficient funds)
Modify global state
User feedback + logging

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete Deposit Function
Question: Write a function deposit() that:

Declares balance as global
Logs "deposit initiated"
Gets amount using get_amount()
Returns early if amount is None
Adds amount to balance
Logs the deposit with amount
Prints confirmation

balance = 1000.0

def deposit():
    global balance
    logging.debug("Deposit initiated")
    amount = get_amount()
    if amount is None:
        return
    balance += amount
    logging.debug(f"{amount} deposited")
    print(f"{amount} deposited \nNew balance is {balance}")

Pattern - Complete function flow:

Global declaration
Log function entry
Get/validate input
Guard clause (early return)
Modify state
Log action
User feedback

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Transfer Between Accounts
pythonchecking = 1000.0
savings = 5000.0
Question: Write code that transfers 100 from checking to savings (subtract from checking, add to savings).

amount = 100
if amount > checking:
    print("insufficient funds")
    return
checking -= amount
savings += amount

Pattern: Guard clause (check sufficiency) → modify source account → modify destination account

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Disable Logging at the end

logging.disable(logging.CRITICAL)

kills all logging code

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Complete Transfer Function
Question: Write a function transfer_to_savings() that:

Declares both accounts as global
Gets amount
Returns if None
Checks if checking has enough funds
Transfers from checking to savings
Logs and prints confirmation

checking = 1000.0
savings = 5000.0

def transfer_to_savings():
    global checking, savings
    amount = get_amount()
    if amount is None:
        return
    if amount > checking:
        print("insufficient funds")
        logging.warning("insufficient funds")
        return
    checking -= amount
    savings += amount
    print(f"deposited ${amount} into savings")
    logging.debug(f"deposited ${amount} into savings")
    return
Pattern - Multi-account function:

Multiple global declarations
Input validation
Guard clause on source account
Modify both accounts atomically
Logging + feedback

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Building Complete Program Structure
Question: Write a complete mini bank program with:

One global balance (start at 100)
get_amount() function (validation)
deposit() function
withdraw() function
Simple menu loop (1=deposit, 2=withdraw, 9=quit)
Logging setup


import logging
logging.basicConfig(level=logging.DEBUG)
account = 100

def get_amount():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("must be positive")
            return None
        return amount
    except ValueError:
        print("invalid input")
        return None

def deposit():
    logging.debug("deposit initiated")
    global account
    amount = get_amount()
    if amount is None:
        return
    account += amount
    print(f"Deposited {amount} into account")
    print(f"new account balance is {account}")
    logging.debug(f"Deposited {amount} into account")
    return

def withdraw():
    logging.debug("withdraw initiated")
    global account
    amount = get_amount()
    if amount is None:
        return
    if amount > account:
        print(f"insufficient funds")
        logging.warning(f"insufficient funds")
        return
    account -= amount
    print(f"Withdrew {amount} from account")
    print(f"new account balance is {account}")
    logging.debug(f"Withdrew {amount} from account")
    return

while True:
    try:
        choice = int(input("1. deposit \n2. withdraw \n9. quit \n"))
        if choice == 1:
            deposit()
        elif choice == 2:
            withdraw()
        elif choice == 9:
            break
        else:
            print('its 1, 2 or 9 this is a threat')
    except ValueError:
        print("pick option gooderer")

✓ Logging setup and usage
✓ Global variable modification
✓ Input validation with try/except
✓ Early returns for None
✓ Guard clauses (insufficient funds)
✓ Menu loop with error handling
✓ Clean function structure

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------













































































