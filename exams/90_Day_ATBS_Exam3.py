'''
Section 3: Strings + Text (Ch 8)
Test: Build this in 20 minutes:
Build a text formatter:
- Take messy user input
- Strip whitespace, fix capitalization
- Count words and characters
- Check if it contains an email address (basic check)
Pass: String methods feel natural, no major issues
Fail: Constantly looking up string methods
'''

messy_input = '''  rs  the the the to work throughout the  8v remaining
days to complete the full 95 ,ch1-9 seamed like the main foundation
of code. the rest look. like(from reading titles alone)    odules   and functions
that ser   ve outside of just   the terminal then ( probably me at the peak of mo
unt stupid) see. about how  tacocat@glort.coi  to formally   build some !things? or at the very
least put into motion what i want'''

import re
pattern = re.compile(r'\w+@\w+\.\w+')


cleaned = messy_input.strip().lower().split()
#
word_count = len(cleaned)

print(f"{word_count} total words")
count_letters = ''.join(cleaned)
print(f"{len(count_letters)} Total letters")
amount_appered = {}
for i in range(len(count_letters)):
    if count_letters[i] not in amount_appered:
        amount_appered[count_letters[i]] = 0
    if count_letters[i] in amount_appered:
        amount_appered[count_letters[i]] += 1
for item in amount_appered:
    print(f"{item}- {amount_appered[item]} Times")
cleaned = ' '.join(cleaned)
cleaned = cleaned.capitalize()
cleaned = re.sub(r'(?<=[.!?])\s+(\w)', lambda m: m.group(0).upper(), cleaned)
match = pattern.findall(cleaned)
print(match)

print(cleaned)







