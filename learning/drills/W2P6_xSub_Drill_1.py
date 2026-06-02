'''
List replication and display
Write a program that asks for a word and a character.
Create a list thats the same length as the word filled with that character.
Print it joined with spaces.
Then ask the user to type the word one letter at a time — reveal each letter as its guessed correctly.
Same core mechanic as hangman.
'''

word = 'bird'
character = 'i'
display = [character] * len(word)
print(' '.join(display))
while True:
    for i in range(len(word)):
        guess = input("guess: ")
        if word[i] == guess:
            display[i] = guess
            print(' '.join(display))
            continue
        print("try again")
























