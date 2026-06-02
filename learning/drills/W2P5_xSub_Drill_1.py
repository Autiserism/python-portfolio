'''
Drill 1 — Reusable helper functions
Write a program with three helper functions — get_positive_float(), get_menu_choice(options) and confirm_action(message).
Then write a simple shopping cart that uses all three helpers.
The point is practicing the pattern of building reusable tools first.
'''

import random

options = None
num_to_leave = -1
def get_positive_float():
    try:
        amount = float(input("guess the number to leave \nIts between 0.001 & 83.000 \n"))
        if amount <=0:
            print("cant be Nothing or negative")
            return None
        return amount
    except ValueError:
        print("literally not that hard")
        return None

def get_menu_choice(options):
    try:
        options = int(input("choose an option \n1. Door 1. \n2. Door 2. \n3. Door 3. \n9. quit \n"))
        if options == 1:
            if confirm_action():
                door1()
        elif options == 2:
            if confirm_action():
                door2()
        elif options == 3:
            if confirm_action():
                door3()
        elif options == 9:
            if confirm_action():
                no_escape()
        else:
            print("its 1, 2, 3 or 9 this is a threat")
            return
    except ValueError:
        print ("make gooderer choice")
        return


def confirm_action():
    choice = input("are you sure? \n")
    if choice == 'yes':
        return True
    elif choice == 'no':
        return False
    else:
        print("its either 'yes' or 'no'")
        return False

def door1():
    print("lump of coal!")

def door2():
    print("a wet left sock!")

def door3():
    print("an 11x9 sheet of paper with a hand drawn outline of my hand!")

def no_escape():
    while True:
        print (random.randint(17165,21172))
        print("no escape")

while True:
    print('the never ending game show!')
    illusion_of_choice = get_positive_float()
    if illusion_of_choice is None:
        print("how many loops will it be?")
    if illusion_of_choice == num_to_leave:
        break
    print("better luck next time")
    print("pick a door any door")
    get_menu_choice(options)
    print('try again')












