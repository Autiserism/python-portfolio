'''
W2P5 — Simple Bank Account W2P5_bank_account.py
Create functions for deposit, withdraw and check balance.
Use a global variable for balance.
Use try/except to handle invalid amounts.
Log all transactions. Prevent withdrawl if balance is too low.
'''
import logging
logging.basicConfig(level=logging.DEBUG)    #filename='bank_log.txt',

checking_balance = 1000.0
savings_balance = 5000.0
savings_password = 'save123'
transactions = []

def verify_savings_password():
    password = input('enter savings password: ')
    if password != savings_password:
        print('access denied')
        return False
    return True

def deposit():
    global checking_balance, savings_balance
    logging.debug('deposit initiated')
    choice = input('Deposit it in \n1 for checking \n2 for savings \nChoose: ')
    dep_amount = get_amount()
    if dep_amount is None:
        return
    if choice == '1':
        checking_balance += dep_amount
        logging.debug(f'deposited {dep_amount} to checking')
        print(f"deposited {dep_amount} to checking")
        transactions.append(f'Deposit checking: +${dep_amount:.2f}')
        return
    elif choice == '2':
        savings_balance += dep_amount
        logging.debug(f'deposited {dep_amount} to savings')
        print(f'deposited {dep_amount} to savings')
        transactions.append(f'Deposit savings: +${dep_amount:.2f}')
        return
    else:
        print('Invalid input')
        return

def get_amount():
    try:
        amount = float(input('Enter amount: '))
        if amount <= 0:
            print('Must be positive')
            return None
        return amount
    except ValueError:
        print('Enter a valid input')

def withdrawl():
    global checking_balance, savings_balance
    logging.debug('withdrawl initiated')
    choice = input('Withdrawl it from \n1 for checking \n2 for savings \nChoose: ')
    if choice == '2':
        if not verify_savings_password():
            return
    withdrawl_amount = get_amount()
    if choice == '1':
        if withdrawl_amount > checking_balance:
            print('insufficient funds')
            logging.warning('insufficient funds checking')
            return
        checking_balance -= withdrawl_amount
        transactions.append(f'withdrawl checking: -${withdrawl_amount:.2f}')
        logging.debug(f'withdrew {withdrawl_amount} from checking')
        print(f"${withdrawl_amount} removed from checkings account\n{checking_balance} remains")
    elif choice == '2':
        if withdrawl_amount > savings_balance:
            print('insufficient funds')
            logging.warning('insufficient funds savings')
            return
        savings_balance -= withdrawl_amount
        transactions.append(f'withdrawl savings: -${withdrawl_amount:.2f}')
        logging.debug(f'withdrew {withdrawl_amount} from savings')
        print(f"${withdrawl_amount} removed from savings account\n{savings_balance} remains")
    return

def check_balance():
    logging.debug('balance check')
    choice = input('1 checking 2 savings 3 both\nChoose: ')
    if choice == '1':
        print(f'checking: ${checking_balance:.2f}')
        logging.debug(f'checking balance displayed: {checking_balance}')
    elif choice == '2':
        if not verify_savings_password():
            return
        print(f'savings: ${savings_balance:.2f}')
    elif choice == '3':
        if not verify_savings_password():
            return
        print(f"Checkings {checking_balance}\nSavings{savings_balance}")

def transfer():
    global checking_balance, savings_balance
    logging.debug('transfer initiated')
    choice = input('1 checking to savings 2 savings to checking')
    if choice == '2':
        if not verify_savings_password():
            return
    amount = get_amount()
    if amount is None:
        return
    if choice == '1':
        if amount > checking_balance:
            print('insufficient funds')
            return
        checking_balance -= amount
        savings_balance += amount
        transactions.append(f'transfer to savings: ${amount:.2f}')
    elif choice == '2':
        if amount > savings_balance:
            print('insufficient funds')
            return
        savings_balance -= amount
        checking_balance += amount
        transactions.append(f'transfer to checking: ${amount:.2f}')
        logging.debug('transfer complete')
        print(f"Transfer complete {checking_balance} is the new balence")

def view_history():
    if not transactions:
        print('no transactions')
    else:
        for transaction in transactions:
            print(transaction)

while True:
    try:
        choice = int(input('''
    1 deposit
    2 withdraw
    3 transfer
    4 check balance
    5 view history
    9 quit
'''))
    except ValueError:
        print('Invalid input')
        continue
    if choice == 1:
        deposit()
    elif choice == 2:
        withdrawl()
    elif choice == 3:
        transfer()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        view_history()
    elif choice == 9:
        break
    else:
        print("invalid input")

logging.disable(logging.CRITICAL)

















