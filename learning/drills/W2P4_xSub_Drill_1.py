'''
Drill 1 — Global state tracking
Write a program with a global variable called logged_in
set to False and a global variable called current_user set to None.
Write two functions — login() that sets both and logout() that resets both.
Write a while loop that shows different menus depending on whether logged_in is True or False.
'''

def login():
    global logged_in
    logged_in = True
    global current_user
    current_user = 'gman'
    print(f'Logged in as {current_user}')
    while logged_in == True:
        choice = input("would you like to logout? 'yes' or 'no' ")
        if choice not in ['yes','no']:
            print('invalid input')
            continue
        if choice == 'yes' :
            logout()
        elif choice == 'no':
            print('theres no other options')
            continue

def logout():
    global logged_in
    logged_in = False
    global current_user
    current_user = None
    print(f'logged in? {logged_in} \nCurrent user = {current_user}')
    return


logged_in = False
current_user = None

while logged_in == False:
    choice = input("would you like to login? 'yes or 'no'")
    if choice == 'yes':
        login()
    else:
        print ('no other options')



















