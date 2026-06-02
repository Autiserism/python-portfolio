'''
Compound input validation
Write a function called get_single_letter that keeps asking until the user enters exactly one alphabetic character.
Reject anything that's more than one character, a number, or a symbol. Use len() and .isalpha() combined.
'''

def get_single_letter():
    while True:
        choice = input('enter a single letter: ')
        if len(choice) != 1 or not choice.isalpha():
            print("invalid input")
            continue
        return choice

get_single_letter()
















