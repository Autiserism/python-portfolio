'''
Write a program that uses re.sub() to censor all numbers in a string by replacing them with # characters,
where the number of # matches the number of digits.
Test it with:
python text = "Call 555-1234 or 800-555-9876 for more info. Code is 42."
Expected output: "Call ###-#### or ###-###-#### for more info. Code is ##."

Hint — re.sub() can take a function as the replacement argument instead of a string.
That function receives the match object and returns the replacement string:

python def replace(match):
    return '#' * len(match.group())

re.sub(pattern, replace, text)'''

#pattern = re.compile(r'[0-9]')
#newtext = pattern.sub('#', text)
#print(newtext)

import re

text = "Call 555-1234 or 800-555-9876 for more info. Code is 42."
pattern = re.compile(r'\d')

def replace(match):
    return '#' * len(match.group())

result = re.sub(pattern, replace, text)
print(result)
