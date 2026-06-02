'''Write a function called is_palindrome that takes a string
and returns True if it's a palindrome
(reads the same forwards and backwards), False if not. Ignore case and spaces.
Test it with:

"racecar" → True
"hello" → False
"A man a plan a canal Panama" → True

Hint — you can reverse a string with [::-1].'''
"racecar"
"hello"



text = "A man a plan a canal Panama"

def is_palindrome(text):
    text = text.split()
    text = ''.join(text)
    text = text.lower()
    text2 = text
    text2 = text2[::-1]
    if text == text2:
        return True
    else:
        return False
result = is_palindrome(text)
print(result)
