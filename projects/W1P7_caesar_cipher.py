'''
Ask for a message and a shift number.
Encode the message by shifting each letter by that number using ord() and chr().
Add a decode option.
'''

# define cipher(text, shift, direction)
#   result = []
#   for char in text
#       if direction == 'decode' shift = -shift
#       if char is uppercase
#           shift using uppercase formula with % 26
#           append to result
#       elif char is lowercase
#           shift using lowercase formula with % 26
#           append to result
#       else
#           append char unchanged
#   return ''.join(result)

# ask encode or decode
# ask for message
# ask for shift number, convert to int
# print cipher(message, shift, direction)

'''
def cipher(text, shift, direction):
    result = []
    if direction == 'decode':
        shift = -shift
    for char in text:
        if direction == 'encode':
            shift = +shift
        if char is char.uppercase:
            chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char is char.lowercase:
            chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            char.append()
    return ''.join(result)

direction = input("'encode' or 'decode' : ")
text = input("Type your message: ")
shift = int(input("Enter a number"))
print (cipher(text, shift, direction))
'''


def cipher(text, shift, direction):
    result = []
    if direction == 'decode':
        shift = -shift

    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)
while True:
    direction = input("'encode' or 'decode'\nor 'quit' to exit: ").lower()
    if direction == 'quit':
        break
    text = input("Type your message: ")
    shift = int(input("Enter a number: "))
    print(cipher(text, shift, direction))
















