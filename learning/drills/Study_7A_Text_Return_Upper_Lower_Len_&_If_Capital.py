'''Write a program that asks the user for a sentence and then:

Prints it in all uppercase
Prints it in all lowercase
Prints the number of characters in it using len()
Prints whether it starts with a capital letter using startswith()'''

sentence = input('Type a sentence ')
print (sentence.upper())
print (sentence.lower())
print (len(sentence))
if sentence[0].istitle():
    print('That sentence starts with a capital')
else:
    print('That sentence doesnt start with a capital')


if sentence[0].isupper():  # checks if first character is uppercase
    print('Starts with a capital')
