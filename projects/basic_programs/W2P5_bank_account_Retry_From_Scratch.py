'''
W2P5 — Simple Bank Account W2P5_bank_account.py
Create functions for deposit, withdraw and check balance.view balance transfer between accounts,  savings account password get_amount ,log_transaction
Use a global variable for balance.
Use try/except to handle invalid amounts.
Log all transactions. Prevent withdraw if balance is too low.
'''

import logging, datetime
logging.basicConfig(level=logging.DEBUG) #filename='bank_log.txt',

transactions = []
checking = 1000
savings = 5000
savings_password = 'save123'

def get_amount():
    try:
        amount = float(input("Enter Amount: "))
        if amount <= 0:
            print("Amount must be positive")
            logging.debug("Invalid Number rejected")
            return False
        #amount = {amount.2f}
        return amount
    except ValueError:
        print("Invalid user Input")
        return False

def log_transaction(activity, amount, account):
    global checking, savings
    time = datetime.datetime.now()
    entry = f"{activity},${amount} updated balance ${account}, at {time}"
    logging.debug(entry)
    transactions.append(entry)
    return

def verify_pass():
    pass_check = input("enter the account password: ")
    if pass_check == savings_password:
        logging.debug("verify password succses")
        return True
    print('Invalid password')
    return

def deposit():
    logging.debug("Deposit initiated")
    global checking, savings
    amount = get_amount()
    if amount is False:
        return
    try:
        choice = int(input(f"Select the account to deposit ${amount} in \n1. Checking \n2. Savings \n"))
        if choice == 1:
            checking += amount
            print(f"${amount} Deposited into checking new balance is {checking}")
            log_transaction(f'Deposit into checking',{amount}, {checking})
            return
        elif choice == 2:
            savings += amount
            print(f"${amount} Deposited into savings")
            log_transaction(f'Deposit into savings', {amount}, {savings})
            return
        else:
            print("Invalid Choice")
            return
    except ValueError:
        print("Invalid Input")
        return

def withdraw():
    logging.debug("Withdraw initiated")
    global checking, savings
    amount = get_amount()
    if amount is False:
        return
    try:
        choice = int(input(f"select account to withdraw ${amount} from \n1. Checking \n2. Savings \n"))
        if choice == 1:
            if amount > checking:
                print("insuffisient Funds \nTransaction Declined")
                logging.warning("Attempt withdraw Too much from checking")
                return
            checking -= amount
            print(f"withdraw Complete Updated balance remaining \n${checking}")
            log_transaction(f'withdraw from checking', {amount}, {checking})
            return
        if choice == 2:
            if verify_pass():
                if amount > savings:
                    print("insuffisient Funds \nTransaction Declined")
                    logging.warning("Attempt withdraw Too much from savings")
                savings -= amount
                print(f"withdraw Complete Updated balance remaining \n${savings}")
                log_transaction(f'Withdraw from savings', {amount}, {savings})
                return
            print("Password Authentication Failed \nTransaction Cancelled")
            return
        print("Invalid Input")
        return
    except ValueError:
        print("Invalid Input")
        return

def view_balance():
    logging.debug("view balance initiated")
    global checking, savings
    try:
        choice = int(input("Which account would you like to view balance \n1. Checking \n2. Savings \n3. Both \n"))
        if choice == 1:
            print(f"Checking Account balance is ${checking}")
            return
        if choice == 2:
            if verify_pass():
                print(f"Savings Account balance is ${savings}")
                return
            print("Password Authentication Failed")
            return
        if choice == 3:
            if verify_pass():
                print(f"Account balance's are \nChecking ${checking} \nSavings ${savings}")
                return
            print("Password Authentication Failed")
            return
        print("Invalid Selection")
        return
    except ValueError:
        print("invalid Input")
        return

def transfer():
    logging.debug("Transfer Between accounts initiated")
    global checking, savings
    choice = int(input("Would you like to transfer funds from: \n1.Checking to savings \n2.Savings to Checking \n"))
    try:
        if choice == 1:
            amount = get_amount()
            if amount > checking:
                print("insuffisient Funds")
                logging.warning("Attempted To Transfer into savings more then checking had")
                return
            checking -= amount
            savings += amount
            print(f"Sucsessfully transfered {amount} from Checking to Savings")
            log_transaction(f'Transfer, Checking to Savings', {amount}, {savings})
            return
        if choice == 2:
            if verify_pass():
                amount = get_amount()
                if amount > savings:
                    print("insuffisient Funds")
                    logging.warning("Attempted To Transfer into savings more then checking had")
                    return
                savings -= amount
                checking += amount
                print(f"Sucsessfully transfered {amount} from Savings to Checking")
                log_transaction(f'Transfer, Savings to Checking', {amount}, {checking})
                return
            print("Password Authentication Failed")
            return
        print("Invalid Selection")
        return
    except ValueError:
        print("invalid Input")
        return

def view_history():
    if not transactions:
        print('no transactions')
        return
    else:
        if verify_pass():
            for transaction in transactions:
                print(transaction)
                return
        print("Password Authentication Failed")
        return
while True:
    try:
        choice = int(input('''
1 deposit
2 withdraw
3 transfer
4 View balance
5 view history
9 quit
'''))
    except ValueError:
        print('Invalid input')
        continue
    if choice == 1:
        deposit()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        transfer()
    elif choice == 4:
        view_balance()
    elif choice == 5:
        view_history()
    elif choice == 9:
        break
    else:
        print("invalid input")

logging.disable(logging.CRITICAL)
















































