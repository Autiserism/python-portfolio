#Write a while loop that asks the user to type a word and keeps looping until they type "quit"
#Print each word they enter. When they type "quit" print "Goodbye" and stop.
answer = ''
while answer != 'quit':
    print('type a word')
    answer =input('>')
    if answer != 'quit':
        print(answer)
print('Goodbye')

