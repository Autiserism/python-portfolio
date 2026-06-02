"""
Win condition with not in
Write a program that has a hidden list of 5 items all set to '?'.
Each loop ask the user to guess an item.
If correct replace '?' with the item. If all '?' are gone print 'you win'.
Use '?' not in list as the win check.
"""
ML = 'gorts'
MLS = []
HL = ['?'] * len(ML)
#print(HL)
while True:
    for i in range(len(ML)):
        MLS.append(ML[i])
        guess = input('take a guess: ')
        if len(guess) != 1 or not guess.isalpha():
            print('invalid input')
        if ML[i] == guess:
            HL[i] = guess
            print(' '.join(MLS))
        if not '?' in HL:
            print('win')
            break
        print(HL)






















