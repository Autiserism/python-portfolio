import re
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
match_obj.group()
'415-555-4242'


import re                                          # 1. import the module
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')        # 2. compile pattern → Pattern object
match = pattern.search('My number is 415-555-4242') # 3. search string → Match object
match.group()


# Both of these match the same phone number pattern:
re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # verbose
re.compile(r'\d{3}-\d{3}-\d{4}')         # cleaner
'''Regex strings should use the r prefix (raw string) —
without it, backslashes are interpreted by Python before regex sees them,
so \d becomes just d and the pattern breaks.'''

phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242.')

mo.group(1)    # '415'
mo.group(2)    # '555-4242'
mo.group()     # '415-555-4242'

area, number = mo.groups()   # unpack tuple directly into variables

'''Group numbering starts at 1, not 0 — group(0) is reserved for the entire match, not the first group.'''


# Match a phone number formatted as (415) 555-4242
pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = pattern.search('My number is (415) 555-4242.')

mo.group(1)   # '(415)'
mo.group(2)   # '555-4242'

'''Mixing escaped \( and unescaped ( in the same pattern is a common source of "missing ) " errors —
every unescaped ( opens a group and needs a matching unescaped ) to close it.'''


pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
mo = pattern.search('Catch me if you can.')

mo.group()    # 'Catch'   — full match
mo.group(1)   # 'ch'      — just the matched suffix from the group

'''The pipe matches the first option found in the string,
not the longest — if the string contains multiple alternatives,
only the first one encountered is returned by search(). Use findall() if you need all of them.'''


pattern_no_groups = re.compile(r'\d{3}-\d{3}-\d{4}')
pattern_no_groups.findall('Cell: 415-555-9999 Work: 212-555-0000')
# ['415-555-9999', '212-555-0000']

pattern_groups = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
pattern_groups.findall('Cell: 415-555-9999 Work: 212-555-0000')
# [('415', '555', '9999'), ('212', '555', '0000')]

'''findall() does not overlap matches — once characters are consumed by a match,
they can't be part of the next one. r'\d{3}' on '1234' returns ['123'], not ['123', '234'].'''

r'\d{3}-\d{3}-\d{4}'
#  ^^        ← qualifier: any digit
#     ^^^    ← quantifier: exactly 3 times
#        ^   ← qualifier: literal hyphen (no quantifier = match once)

'''A qualifier with no quantifier matches exactly once by default —
it's easy to forget this and assume it matches as many times as possible.'''


vowel_pattern = re.compile(r'[aeiouAEIOU]')
vowel_pattern.findall('RoboCop eats BABY FOOD.')
# ['o', 'o', 'o', 'e', 'a', 'A', 'O', 'O']

# Range example
re.compile(r'[a-zA-Z0-9]')   # matches any letter or digit

'''Special regex characters like . and () lose their special meaning inside square brackets
you don't need to escape them there.'''


consonant_pattern = re.compile(r'[^aeiouAEIOU]')
consonant_pattern.findall('RoboCop eats.')
# ['R', 'b', 'C', 'p', ' ', 't', 's', '.']

'''A negative class matches everything not listed — including spaces, punctuation, and digits.
It's rarely as clean as it looks unless you account for that.'''


pattern = re.compile(r'\d+\s\w+')
pattern.findall('12 drummers, 11 pipers, 10 lords')
# ['12 drummers', '11 pipers', '10 lords']
'''
\d / \D — digit 0–9 / anything that is not a digit
\w / \W — letter, digit, or underscore / anything that is not those
\s / \S — space, tab, or newline / anything that is not whitespace

There is no shorthand for letters only — \w also matches digits and underscores, which can cause unintended matches.
Use [a-zA-Z] when you strictly need letters.'''


at_re = re.compile(r'.at')
at_re.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat']
'''
The dot matches exactly one character —
flat only returned lat because the dot consumed just the l. To match a literal period, escape it: \.'''


'''
Key pitfalls:
python# [A-Za-z] misses accented letters — 'Sinéad' matches only up to 'Sin'
# \w catches accented letters but also digits and underscores
# "O'Connor" — \w+ stops at the apostrophe, returning only 'O'
# Smart quotes (' ") and straight quotes (' ") are different characters entirely
[A-Z] and [a-z] are separate
forgetting to combine them into [A-Za-z] means your pattern silently misses half the alphabet.'''


# Single character optional
re.compile(r'42!?').search('42')    # matches '42'
re.compile(r'42!?').search('42!')   # matches '42!'

# Group optional — area code may or may not be present
pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
pattern.search('415-555-4242').group()   # '415-555-4242'
pattern.search('555-4242').group()       # '555-4242'
'''
? applies only to the character directly before it —
r'42?!' makes the 2 optional, not 42. Wrap in () to make a multi-character sequence optional.'''


pattern = re.compile(r'Eggs( and spam)*')
pattern.search('Eggs').group()                      # 'Eggs'
pattern.search('Eggs and spam and spam').group()    # 'Eggs and spam and spam'
'''
Because * allows zero matches, it will never cause search() to return None on its own —
it always "succeeds" even if it matches nothing.'''


pattern = re.compile(r'Eggs( and spam)+')
pattern.search('Eggs') == None          # True — no match, needs at least one
pattern.search('Eggs and spam').group() # 'Eggs and spam'
'''
* and + look nearly identical but behave very differently on absent input — * silently succeeds, + fails.
Swapping one for the other is an easy typo with a hard-to-spot bug.'''


re.compile(r'(Ha){3}').search('HaHaHa').group()   # 'HaHaHa'
re.compile(r'(Ha){3}').search('HaHa') == None     # True — only 2, needs 3
'''
re.compile(r'(Ha){3,5}').search('HaHaHaHa').group()  # 'HaHaHaHa'
Gotcha: Curly bracket ranges use a comma, not a colon like Python slices — and both bounds are inclusive,
so {3,5} includes 5, unlike slice notation where the end is exclusive.
more controlled than * or + when you know the expected count.'''


re.compile(r'(Ha){3,5}').search('HaHaHaHaHa').group()    # 'HaHaHaHaHa' — greedy
re.compile(r'(Ha){3,5}?').search('HaHaHaHaHa').group()   # 'HaHaHa'     — lazy
'''
The ? has two unrelated meanings in regex —
after a character/group it means optional (zero or one); after a quantifier it means lazy.
Context is the only way to tell them apart.'''


# Greedy — matches as far right as possible
re.compile(r'<.*>').search('<tag> extra >').group()    # '<tag> extra >'

# Lazy — stops at the first closing >
re.compile(r'<.*?>').search('<tag> extra >').group()   # '<tag>'

# Capture text between known labels
pattern = re.compile(r'First Name: (.*?) Last Name: (.*)')
m = pattern.search('First Name: Al Last Name: Sweigart')
m.group(1)   # 'Al'
m.group(2)   # 'Sweigart'
'''
.* stops at newlines —
it won't cross a \n unless you explicitly enable re.DOTALL.'''


text = 'Line one.\nLine two.\nLine three.'

re.compile(r'.*').search(text).group()              # 'Line one.'
re.compile(r'.*', re.DOTALL).search(text).group()  # 'Line one.\nLine two.\nLine three.'
'''
Forgetting re.DOTALL on multiline text is a silent failure —
the pattern matches but only returns the first line, with no error to alert you.'''


re.compile(r'\bcat\b').findall('the cat found a catapult')
# ['cat'] — only the standalone word

re.compile(r'\Bcat\B').findall('certificate')
# ['cat'] — matches only when embedded mid-word
'''
\b is a word boundary, not a space —
it triggers between any word/non-word character transition,
including punctuation and string edges.'''


re.compile(r'^\d+$').search('1234567890')    # match — all digits
re.compile(r'^\d+$').search('123abc')  == None  # True — extra chars fail

re.compile(r'^Hello').search('Hello, world!')   # match
re.compile(r'^Hello').search('Say Hello')       # None — not at start
'''
Without ^ and $, search() will match the pattern anywhere inside the string —
a common source of false positives during input validation.'''


pattern = re.compile(r'robocop', re.I)

pattern.search('RoboCop is part man.').group()   # 'RoboCop'
pattern.search('ROBOCOP protects.').group()       # 'ROBOCOP'
pattern.search('Have you seen robocop?').group()  # 'robocop'
'''
re.I is a flag passed to re.compile(), not part of the pattern string —
putting it inside the regex itself (like r'(?i)robocop') is valid
but the re.I argument form is cleaner and easier to read.'''


agent_pattern = re.compile(r'Agent \w+')
agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob.')
# 'CENSORED contacted CENSORED.'
'''
.sub() returns a new string —
it doesn't modify the original.
If you don't capture the return value, the result is lost.'''


# Capture just the first letter of each agent name, replace the rest with ****
agent_pattern = re.compile(r'Agent (\w)\w*')
agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.')
# 'A**** contacted B****.'
'''
The back reference in the replacement string uses \1 syntax, not group(1) —
using Python's group() method notation here will not work and will produce wrong output silently.'''


pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # Area code (optional)
    (\s|-|\.)?           # Separator
    \d{3}                # First three digits
    (\s|-|\.)            # Separator
    \d{4}                # Last four digits
)''', re.VERBOSE)
'''
Because whitespace is ignored inside a verbose pattern,
you can't match a literal space with   — use \s or \  (escaped space) instead.'''


# Two flags
pattern = re.compile(r'foo', re.IGNORECASE | re.DOTALL)

# All three
pattern = re.compile(r'''
    foo   # match foo
''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
'''
The | here is the bitwise OR operator —
it has nothing to do with the regex pipe used for alternation inside a pattern string.
Same symbol, completely different context.'''

'''
re.VERBOSE enables comments (#) and ignored whitespace inside a pattern —
# use triple-quoted strings to spread complex patterns across multiple lines
Literal spaces inside a verbose pattern must be written as \s or \  —
bare spaces are stripped out
Combine multiple flags with | between them in the second argument to re.compile()
— re.I | re.DOTALL | re.VERBOSE is valid and common'''


