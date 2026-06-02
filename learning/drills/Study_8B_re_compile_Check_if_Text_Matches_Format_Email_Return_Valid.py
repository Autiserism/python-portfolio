'''
Write a program that uses regex to find all email addresses in a string and prints them as a list.
Test it with:
text = "Contact us at support@example.com or sales@company.org for help. Invalid ones like @nouser.com or nodomain@ should not match."
Expected output: ['support@example.com', 'sales@company.org']
Hint — an email pattern has:

One or more word characters before @
One or more word characters after @
A dot then 2-4 letters for the domain extension'''


import re

email_pattern = re.compile(r'[a-zA-Z0-9%+\-_.]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')

text = 'Contact us at support@example.com or sales@company.org for help. Invalid ones like @nouser.com or nodomain@ should not match.'

emails = email_pattern.findall(text)
print(emails)
