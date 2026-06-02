def is_phone_number(text):
    if len(text) != 12:  # Phone numbers have exactly 12 characters.
        return False
    for i in range(0, 3):  # The first three characters must be numbers.
        if not text[i].isdecimal():
            return False
    if text[3] != '-':  # The fourth character must be a dash.
        return False
    for i in range(4, 7): # The next three characters must be numbers.
        if not text[i].isdecimal():
            return False
    if text[7] != '-':  # The eighth character must be a dash.
        return False
    for i in range(8, 12):  # The next four characters must be numbers.
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?', is_phone_number('415-555-4242'))
print(is_phone_number('415-555-4242'))
print('Is Moshi moshi a phone number?', is_phone_number('Moshi moshi'))
print(is_phone_number('Moshi moshi'))


'''
When this program is run, the output looks like this:

Is 415-555-4242 a phone number?
True
Is Moshi moshi a phone number?
False
The is_phone_number() function has code that does several checks to determine whether the string in text is a valid phone number.
If any of these checks fail, the function returns False. First,
the code checks that the string is exactly 12 characters long ❶.
Then, it checks that the area code (that is, the first three characters in text) consists of only numeric characters
❷ by calling the isdecimal() string method. The rest of the function checks that the string follows the pattern of a phone number:
the number must have the first hyphen after the area code ❸, three more numeric characters ❹, another hyphen
❺, and finally, four more numeric characters ❻. If the program execution manages to get past all the checks,
it returns True ❼.

Calling is_phone_number() with the argument '415-555-4242' will return True. Calling is_phone_number() with
'Moshi moshi' will return False; the first test fails because 'Moshi moshi' is not 12 characters long.

If you wanted to find a phone number within a larger string, you would have to add even more code to locate the pattern.
Replace the last four print() function calls in isPhoneNumber.py with the following:

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
  ❶ segment = message[i:i+12]
  ❷ if is_phone_number(segment):
        print('Phone number found: ' + segment)
print('Done')
When this program is run, the output will look like this:

Phone number found: 415-555-1011
Phone number found: 415-555-9999
Done
On each iteration of the for loop, a new segment of 12 characters from message is assigned to the variable segment ❶.
For example, on the first iteration, i is 0, and segment is assigned message[0:12] (that is, the string 'Call me at 4').
On the next iteration, i is 1, and segment is assigned message[1:13] (the string 'all me at 41').
In other words, on each iteration of the for loop, segment takes on the following values

'Call me at 4'
'all me at 41'
'll me at 415'
'l me at 415-'
and so on, until its last value is 's my office.'

The loop’s code passes segment to is_phone_number() to check whether it matches the phone number pattern ❷,
and if so, it prints the segment. Once it has finished going through message, we print Done.

While the string in message is short in this example, the program would run in less than a second even if it were millions of characters long.
A similar program that finds phone numbers using regular expressions would also run in less than a second; however,
regular expressions make writing these programs much quicker.
'''
