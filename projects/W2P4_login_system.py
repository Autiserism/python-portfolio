'''
Store usernames and passwords in a dictionary.
Menu options: login, register, quit.
Limit login attempts to 3 before locking out.
Use assertions to validate registration input.
'''


def register(users):
    new_user = input('enter username: ')
    try:
        assert len(new_user) >= 3
    except AssertionError:
        print('username must be minimum 3 characters')
        return
    new_user = new_user.lower()
    if new_user in users:
        print('user already exists')
        return
    new_pass = input(f'Create a Password for {new_user}: ')
    confirm_pass = input('To Confirm password re enter it: ')
    if confirm_pass != new_pass:
        print('error passwords dont match')
        return
    try:
        assert len(new_pass) >= 6
    except AssertionError:
        print('password must be minimum 6 characters')
        return
    try:
        assert new_user != new_pass.lower()
    except AssertionError:
        print('username cannot be the same as password')
        return
    users[new_user] = new_pass
    print('registered successfully')

def login(users):
    global attempts, current_user
    if attempts >= 3:
        print('locked out')
        return
    username = input('enter your user name: ').lower()
    password = input('enter your password: ')
    if username in users and users[username] == password:
        print(f'welcome {username}')
        current_user = username
        attempts = 0
    elif username not in users:
        print(f'cannot find {username} try again')
    else:
        attempts += 1
        print('invalid credentials')
        print(f'{3 - attempts} attempts remaining')
        if attempts >= 3:
            print('account locked')

def logout():
    global current_user, attempts
    current_user = None
    attempts = 0
    print('logged out')

def logged_in_menu():
    while True:
        print("options: \n1 view account \n2 logout")
        try:
            choice = int(input('make a selection: '))
        except ValueError:
            print('invalid input')
            continue
        if choice == 1:
            print(f'Username: {current_user}')
            print(f'Password: {users[current_user]}')
        if choice == 2:
            logout()
            break

users = {'tomuser': 'TomPass', 'gmanuser': 'GmanPass'}
attempts = 0
current_user = None

while True:
    if current_user is not None:
        logged_in_menu()
    else:
        print ('menu: \n1 login \n2 register \n9 quit')
        try:
            choice = int(input('make a selection: '))
        except ValueError:
            print('invalid input')
            continue
        if choice == 1:
            login(users)
        elif choice == 2:
            register(users)
        elif choice == 9:
            break














'''
import re

define login
    case sensitive
    if user name and pass equal too user_name_pass
        print welcome {name}
        logged in()
    if username and or password not
        print uncorrect user or password
        global log in attempts +=1


define logged in
set global variable attempts zero
    have option to view file thats indexed from a list
    corisponding to the user login that takes the name into a number (ex tom-hex=847977) variable and
    un encrypts it shifts ord() by number with the % roll over?
    log out



define registar
    ask for name
    if name already in list as them to add an initial
    assert username not == password
    assert password not == username
    add name to the list
    case sesitive
    set default key username as user input
    set value as user password return and add items to the list

define locked out loop
    while true if input
        print locked out


user_name_Pass nested list with the persons name attached to key username and password as value

attempts variable reset to zero after succsesful login?
if attempts <=4
    locked out






# define word_count(text_split)
#     return len(text_split)  # len() does the counting automatically

# define unique_word_count(text_split)
#     return len(set(text_split))  # set() removes duplicates automatically

# define words_appearing_once(text_split)
#     counts = {}
#     for word in text_split
#         counts.setdefault(word, 0)
#         counts[word] += 1
#     once = []
#     for word, count in counts.items()
#         if count == 1
#             once.append(word)
#     return once

# define av_word_len(text_split)
#     lengths = []
#     for word in text_split
#         lengths.append(len(word))
#     return sum(lengths) / len(lengths)

# define longest_word(text_split)
#     longest = text_split[0]
#     for word in text_split
#         if len(word) > len(longest)
#             longest = word
#     return longest

# define most_common_word(text_split)
#     counts = {}
#     for word in text_split
#         counts.setdefault(word, 0)
#         counts[word] += 1
#     most_common = ''
#     highest = 0
#     for word, count in counts.items()
#         if count > highest
#             highest = count
#             most_common = word
#     return most_common, highest

# pasted_text = input('paste a paragraph: ')
# text_split = pasted_text.lower().split()

# total = word_count(text_split)
# unique = unique_word_count(text_split)
# once = words_appearing_once(text_split)
# average = av_word_len(text_split)
# longest = longest_word(text_split)
# common_word, common_count = most_common_word(text_split)

# print formatted report
'''
















