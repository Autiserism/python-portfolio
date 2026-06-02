    Basic Regex Syntax 1A

    Literal Matching
import re
text = "The cat sat on the mat"
Question: Write a pattern that matches the word "cat" exactly.

import re
pattern = re.compile(r'cat')

Pattern: r'cat' matches the literal string "cat"

The r prefix means "raw string" (treats backslashes literally - important for regex).

Now lets use it:
result = pattern.search("The cat sat")
if result:
    print("Found!")  # This will print

Next: How would you search for "dog" in the same text?

dog_pattern = re.compile(r'dog')
result = dog_pattern.search("The cat dog sat")
if result:
    print("Found dog!")
Pattern: Each search term needs its own pattern (or compile a new one).
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    The . (Dot) Wildcard
Question: What does this pattern match?
pattern = re.compile(r'c.t')
Examples to test: "cat", "cot", "cut", "c9t", "ct"

It matches all EXCEPT "ct".
Pattern r'c.t' breakdown:

c - literal 'c'
. - any single character (but must exist)
t - literal 't'

Matches:

"cat" ✓
"cot" ✓
"cut" ✓
"c9t" ✓
"ct" ✗ (no character between c and t)

Pattern: . matches any ONE character (not zero)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Character Classes [ ]
Question: Write a pattern that matches "cat", "cot", or "cut" but NOT "c9t".

Pattern breakdown:

c - literal 'c'
[aou] - matches ONE of: a, o, or u
t - literal 't'

Character class [...] - matches ONE character from the set.

pattern = re.compile(r'c[aou]t')
Matches: "cat", "cot", "cut"
Doesnt match: "cit", "c9t", "ct"
Pattern: [characters] - match any ONE from the set

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Character Ranges
Question: Write a pattern that matches any lowercase letter followed by "at" (bat, cat, dat, ..., zat).

Works! But Sub optimal r'[a-z][a][t]'
Cleaner: r'[a-z]at' (literal chars dont need brackets)
Pattern: [a-z] - any lowercase letter (range) followed by any literal characters
Common ranges:

[a-z] - lowercase
[A-Z] - uppercase
[0-9] - digits
[a-zA-Z] - any letter
[a-zA-Z0-9] - alphanumeric

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Negated Character Class
Question: Write a pattern that matches any character that is NOT a digit, followed by "at".

Using character class negation:
r'[^0-9]at'
Pattern: [^...] - caret inside brackets means NOT
Both work:

r'\Dat' - shorthand (matches any non-digit)
r'[^0-9]at' - explicit character class

Examples:

[^a-z] - NOT lowercase letter
[^0-9] - NOT digit (same as \D)


Session 1A of regex curriculum.
covered:
✓ Literal matching
✓ . wildcard
✓ [...] character classes
✓ [a-z] ranges
✓ [^...] negation


------------------------------------------------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------

    Quantifiers     1B

Quantifiers specify how many times something should match.


The * (Zero or More)
Question: What does this pattern match?
pattern = re.compile(r'ca*t')
Test strings: "ct", "cat", "caat", "caaaat"

* means zero OR more, so it DOES match "ct"!
Pattern r'ca*t' matches:

"ct" ✓ (zero a s)
"cat" ✓ (one a)
"caat" ✓ (two a s)
"caaaat" ✓ (many a s)

Pattern: * = zero or more of the preceding character
Critical: Zero is included! Thats the difference from +.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    The + (One or More)

Question: What does this pattern match?
pattern = re.compile(r'ca+t')
Test strings: "ct", "cat", "caat", "caaaat"

Pattern r'ca+t' matches:

"ct" ✗ (zero a s - needs at least one)
"cat" ✓ (one a)
"caat" ✓ (two a s)
"caaaat" ✓ (many a s)

Pattern: + = one or more (at least one required)
Key difference:

* = 0 or more (optional)
+ = 1 or more (required)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    The ? (Zero or One)

Question: What does this pattern match?
pattern = re.compile(r'colou?r')
Test strings: "color", "colour", "colouur"

Pattern r'colou?r' matches:

"color" ✓ (zero u s)
"colour" ✓ (one u)
"colouur" ✗ (two u s - too many)

Pattern: ? = zero or one (makes it optional)
Common use: Making characters optional (like British vs American spelling)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Exact Count {n}

Question: Write a pattern that matches exactly 3 digits in a row.

pattern = re.compile(r'{d}{d}{d}') ✗ {d}{d}{d} - curly braces are FOR the quantifier, not around each character
pattern = re.compile(r"d{3}")      ✗ Missing backslash: r"d{3}" - matches "ddd" (literal 'd's)

✓ Correct!
pattern = re.compile(r"\d{3}")
Matches: "123", "999", "007"
Doesnt match: "12" (only 2), "1234" (too many... wait, actually it DOES match the first 3!)
Important: Regex finds matches anywhere - \d{3} would match "123" inside "12345"

r'\d{3}' matches "123", "999"
r'a{5}' matches "aaaaa"
r'[A-Z]{2}' matches "AB", "XY"
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Range {n,m}
Question: Write a pattern that matches 2 to 4 digits in a row

pattern = re.compile(r"\d{2,4}")
Pattern: {min,max} - between min and max repetitions
Matches:

"12" ✓ (2 digits)
"123" ✓ (3 digits)
"1234" ✓ (4 digits)
"1" ✗ (only 1)
"12345" - matches first 4

Common ranges:

{2,} - 2 or more (no max)
{,5} - 0 to 5 (no min)
{3,6} - 3 to 6


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Combining Patterns
Question: Write a pattern that matches a phone number format: exactly 3 digits, dash, exactly 4 digits (like "123-4567")

pattern = re.compile(r"\d{3}-\d{4}")
Matches: "123-4567", "999-0000"
Doesnt match: "1234567" (no dash), "12-4567" (wrong count)

Pattern: Combine quantifiers with literals

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Quick Quiz
Match these to patterns:
A. r'a*'
B. r'a+'
C. r'a?'
D. r'a{3}'

Zero or one 'a'
One or more 'a's
Exactly three 'a's
Zero or more 'a's

Correct matches:

A. r'a*' → Zero or MORE (4)
B. r'a+' → One or more (2) ✓
C. r'a?' → Zero or ONE (1)
D. r'a{3}' → Exactly three (3) ✓

Memory trick:

* = star = sero or more
+ = plus = Must be Positive (One or more)
? = question = maybe (0 or 1)

------------------------------------------------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------

                                                    Anchors (Position Matchers) 1C

Anchors match positions, not characters. Theyre zero-width.

Round 1 - Start Anchor ^
Question: Whats the difference between these two patterns?

pattern1 = re.compile(r'cat')
pattern2 = re.compile(r'^cat')
Test string: "The cat sat.cat is here."

^ has different meanings in different contexts:

Inside brackets [^...] = NOT (negation)
Outside brackets ^ = START of string
Pattern r'cat': matches "cat" anywhere
Pattern r'^cat': matches "cat" only at the START
Test: "The cat sat"

r'cat' ✓ matches (finds "cat" in middle)
r'^cat' ✗ doesnt match (string starts with "The", not "cat")

Test: "cat is here"

r'cat' ✓ matches
r'^cat' ✓ matches (starts with "cat")

Pattern: ^ = must be at beginning of string

to match it must start with the character(s) following ^xyz123

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    End Anchor $
Question: Write a pattern that matches "cat" only at the END of a string.

pattern = re.compile(r'cat$')
Test: "I have a cat"

r'cat' ✓ matches
r'cat$' ✓ matches (ends with "cat")

Test: "cat is here"

r'cat' ✓ matches
r'cat$' ✗ doesnt match (ends with "here", not "cat")

Pattern: $ = must be at end of string

to match it must end with the character(s) placed Befor $ , xyz123$

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Combining ^ and $
Question: What does this pattern match?
pattern = re.compile(r'^cat$')
Test strings: "cat", "my cat", "cat!", "cats"

Pattern r'^cat$' matches:

"cat" ✓ (entire string is exactly "cat")
"my cat" ✗ (has text before)
"cat!" ✗ (has text after)
"cats" ✗ (has 's' after)

Pattern: ^...$ = entire string must match exactly (nothing before or after)
Use case: Form validation (exact match required)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Word Boundary \b

Question: Whats the difference?
pattern1 = re.compile(r'cat')
pattern2 = re.compile(r'\bcat\b')
Test string: "The cat in concatenate"

Answer: r'cat' matches "cat" anywhere, including inside other words
r'\bcat\b' matches "cat" only as a complete word

Pattern r'cat': matches "cat" anywhere

"The cat in concatenate" (2 matches)

Pattern r'\bcat\b': matches "cat" as whole word only

"The cat in concatenate" (1 match)

Pattern: \b = word boundary (edge between word and non-word character)
Word characters: letters, digits, underscore [a-zA-Z0-9_]
Non-word: everything else (spaces, punctuation, etc.)
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Partial Word Boundaries
Question: Write a pattern that matches words STARTING with "cat" (cat, cats, category, but not concatenate).

pattern = re.compile(r'\bcat')
Matches words STARTING with "cat":

"The cat sat" ✓
"category" ✓
"concatenate" ✗ (cat not at word start)

Pattern: \bcat = word starts with "cat"

pattern = re.compile(r'^cat') ✗ ^ is for STRING start, not WORD start.

r'^cat' - string must START with "cat"
For words: r'\bcat' - word boundary at start only
Test: "The cat and category"

r'^cat' ✗ (string starts with "The")
r'\bcat' ✓ (matches "cat" in both words)

Test: "concatenate"

r'^cat' ✗ (string starts with "con")
r'\bcat' ✗ (no word boundary before "cat")

Pattern: \b at start only = word starts with pattern

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Practical Example
Question: Write a pattern that matches a complete 3-digit number (not part of a larger number).
Examples:

"Room 123" ✓
"12345" ✗ (123 is part of larger number)
"Code: 999" ✓

✓ Perfect!
pattern = re.compile(r'\b\d{3}\b')
Matches:

"Room 123" ✓ (complete 3-digit number)
"Code: 999" ✓
"12345" ✗ (123 is part of 12345, no word boundary)
"12" ✗ (only 2 digits)

Pattern: \b\d{3}\b - exactly 3 digits as complete word
This combines:

\b - word boundary
\d{3} - exactly 3 digits
\b - word boundary

1C Summary:
✓ ^ - start of string
✓ $ - end of string
✓ ^...$ - exact match (entire string)
✓ \b - word boundary
✓ \bword\b - complete word match
Key distinction:

^ and $ = string positions
\b = word edge positions

------------------------------------------------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------

                                                    Special Sequences, Groups & re Module

Session 2A: Special Sequences (Shortcuts)
Special sequences are shortcuts for common character classes.

    Round 1 - \d (Digit)
Question: These are equivalent. Which is shorter?
pattern1 = re.compile(r'[0-9]')
pattern2 = re.compile(r'\d')

Pattern: \d = [0-9] (digit shorthand)
Matches: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
Use case: r'\d{3}' matches 3 digits (like "123")



------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 2 - \D (Non-Digit)
Question: What does \D match?

Pattern: \D = [^0-9] (NOT a digit)
Matches: letters, spaces, punctuation, special chars - anything except 0-9
Example:

r'\D+' matches "abc!" in "abc!123"

Pattern pair:

\d = digit
\D = NOT digit (opposite)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 3 - \w (Word Character)
Question: What does \w match?
Hint: Letters, digits, and one special character.

Pattern: \w = [a-zA-Z0-9_]
Matches:

Letters (a-z, A-Z) ✓
Digits (0-9) ✓
Underscore (_) ✓

Doesnt match:

Spaces ✗
Punctuation ✗ (except underscore)
Special chars ✗

Example:

r'\w+' matches "hello_123" but stops at space or punctuation

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 4 - \W (Non-Word Character)
Question: Write a pattern that matches any character that is NOT a letter, digit, or underscore.

pattern = re.compile(r'\W')
Pattern: \W = [^a-zA-Z0-9_] (NOT word character)
Matches: spaces, punctuation, special chars
Example:

r'\W+' matches "   !@#" in "hello   !@# world"

Pattern pair:

\w = word character
\W = NOT word character

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 5 - \s (Whitespace)
Question: What does \s match?

 It matches all whitespace:
Pattern: \s matches:

Space   ✓
Tab \t ✓
Newline \n ✓
Carriage return \r ✓

Example:

r'\s+' matches all whitespace in "hello    world\n"

Use case: Cleaning up extra spaces

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 6 - \S (Non-Whitespace)
Question: Write a pattern that matches any non-whitespace character.

pattern = re.compile(r'\S')
Pattern: \S = NOT whitespace
Matches: anything except space, tab, newline, etc.
Example:

r'\S+' matches "hello" and "world" in "hello    world"

Pattern pair:

\s = whitespace
\S = NOT whitespace

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 7 - Quick Reference Table
Fill in the opposites:

Lowercase       Matches     Uppercase       Matches
\d              digit       \D              Not Digits
\w              word char   \W              Not Word
\s              whitespace  \S              Not Spaces

Memory trick: Uppercase = opposite (NOT)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Combining Special Sequences
Question: Write a pattern that matches a "word" of 3-5 letters followed by a space and 2 digits.
Example: "abc 12", "hello 99"

pattern = re.compile(r'\w{3,5}\s\d{2}')
Pattern breakdown:

\w{3,5} - 3 to 5 word chars
\s - one whitespace
\d{2} - exactly 2 digits

Matches: "abc 12", "hello 99", "test_ 45"
Doesnt match: "ab 12" (only 2 letters), "hello99" (no space)

Session 2A Summary:
✓ \d / \D - digit / not digit
✓ \w / \W - word char / not word
✓ \s / \S - whitespace / not whitespace
✓ Uppercase = opposite (NOT)
✓ Combining sequences with quantifiers

------------------------------------------------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------

                                                    Session 2B: Capturing Groups

Groups let you extract parts of a match and apply quantifiers to multiple characters.

    Round 1 - Basic Grouping
Question: Whats the difference?
pattern1 = re.compile(r'cat+')
pattern2 = re.compile(r'(cat)+')
Test: "catcatcat"

The difference is about what the + applies to:
Pattern r'cat+':

Means: "ca" followed by one or more "t"
Matches: "cat", "catt", "cattt"
In "catcatcat": matches "cat" (three separate times)

Pattern r'(cat)+':

Means: entire group "cat" repeated one or more times
Matches: "cat", "catcat", "catcatcat"
In "catcatcat": matches entire "catcatcat" (ONE match)

Key difference:

Without (): quantifier applies to last character only
With (): quantifier applies to entire group

the quantifier in this case + only grabs whats to the left of it so the 't' in cat+
so with the (brackets) the + will grab everything within it 'cat'as many times with the +

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 2 - Capturing Groups Extract Data
Question: What do the parentheses capture here?
pattern = re.compile(r'(\d{3})-(\d{4})')
match = pattern.search("Call 555-1234 today")

Pattern r'(\d{3})-(\d{4})' has 2 capture groups:

(\d{3}) - first group: 3 digits
(\d{4}) - second group: 4 digits

How to access them:

match.group(0)  # Entire match: "555-1234"
match.group(1)  # First group: "555"
match.group(2)  # Second group: "1234"

Pattern: Parentheses () capture for later extraction

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 3 - Accessing Groups
pattern = re.compile(r'(\w+)@(\w+)\.com')
match = pattern.search("Email: john@example.com")
Question: What do these return?

match.group(0)  # "john@example.com" - full match
match.group(1)  # "john" - first capture group
match.group(2)  # "example" - second capture group

Pattern:
group(0) = entire match
group(1), group(2), etc. = captured groups (numbered by opening parenthesis)


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 4 - Multiple Groups Practice
Question: Write a pattern that captures:

First name
Last name

From: "Name: John Smith"
Use \w+ for names.

pattern = re.compile(r'(\w+)\s(\w+)')

\w+ does NOT match : (colon is not a word character).
So in "Name: John Smith":

r'(\w+)\s(\w+)' would skip "Name:" and match "John Smith" ✓
First group: "John"
Second group: "Smith"

Pattern: \w+ stops at non-word characters (like : or spaces)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 5 - Non-Capturing Groups (?:)
Sometimes you want grouping for quantifiers but DONT want to capture.
Question: Whats the difference?

pattern1 = re.compile(r'(cat)+')
pattern2 = re.compile(r'(?:cat)+')

(?: is special syntax, not literal characters.
Both patterns match the same text - the difference is in capturing:
Pattern r'(cat)+':

Matches: "cat", "catcat", "catcatcat"
Creates capture group - accessible with match.group(1)

Pattern r'(?:cat)+':

Matches: "cat", "catcat", "catcatcat" (same matches)
No capture group - grouping is only for the + quantifier

When to use (?:):

You need grouping for quantifiers
But dont need to extract that data
Slightly more efficient (doesnt allocate memory for capture)

Example:
# With capture
match = re.search(r'(cat)+', 'catcat')
match.group(1)  # 'cat' (last repetition)

# Non-capturing
match = re.search(r'(?:cat)+', 'catcat')
match.group(1)  # Error! No group 1

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 6 - Practical Groups
Question: Write a pattern to extract area code and number from: "(555) 123-4567"
Capture:

Area code (555)
First part (123)
Second part (4567)

Complete pattern:
pythonpattern = re.compile(r'\((\d{3})\)\s(\d{3})-(\d{4})')
Pattern breakdown:

\( - literal ( (escaped)
(\d{3}) - capture group 1: area code
\) - literal ) (escaped)
\s - space
(\d{3}) - capture group 2: first part
- - literal dash
(\d{4}) - capture group 3: second part

Remember: \( and \) are literal parentheses, () are capture groups!

Your version: r'(\(\d{3}\))\s(\d{3})-(\d{4})'

group(1) = "(555)" (includes parentheses)
group(2) = "123"
group(3) = "4567"

Alternative: r'\((\d{3})\)\s(\d{3})-(\d{4})'

group(1) = "555" (just digits)
group(2) = "123"
group(3) = "4567"

Difference: Where you place the capturing () determines what gets captured.
Both are valid - depends if you want the parentheses in the captured data or not!

    Session 2B Summary:
✓ () - capturing groups
✓ match.group(0) - full match
✓ match.group(1), group(2) - captured groups
✓ (?:) - non-capturing groups (grouping without capture)
✓ Escaping literal parentheses \( \)
✓ Groups for extraction vs groups for quantifiers

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Session 2B Extended: Real-World Group Usage

Round 1 - Email Extraction
Scenario: Extract username and domain from email addresses.
text = "Contact: john.doe@example.com for info"
Question: Write a pattern that captures:

Username (john.doe)
Domain (example.com)

pattern = re.compile(r'(\w+\.\w+)@(\w+\.\w+)')
Works for this example!

But only matches emails with exactly one dot in each part.
More flexible:
pattern = re.compile(r'([\w.]+)@([\w.]+)')
Pattern breakdown:

([\w.]+) - group 1: word chars or dots (username)
@ - literal @
([\w.]+) - group 2: word chars or dots (domain)

Matches:

"john@example.com" ✓
"john.doe@example.com" ✓
"j.d.smith@mail.example.com" ✓

Usage:
match = pattern.search(text)
username = match.group(1)  # "john.doe"
domain = match.group(2)     # "example.com"

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 2 - Phone Number Parsing

Scenario: Parse phone number into components.
text = "Call (555) 123-4567 or (555) 987-6543"
Question: Write a pattern to extract all phone numbers, capturing area code separately from the rest.

pattern = re.compile(r'(\(\d{3}\))\s(\d{3}-\d{4})')
Captures:

group(1): "(555)"
group(2): "123-4567"

To get ALL matches:
matches = pattern.findall(text)
# [('(555)', '123-4567'), ('(555)', '987-6543')]

for area, number in matches:
    print(f"Area: {area}, Number: {number}")

Even more detailed breakdown:
pattern = re.compile(r'\((\d{3})\)\s(\d{3})-(\d{4})')
# group(1): 555 (area code without parens)
# group(2): 123 (prefix)
# group(3): 4567 (suffix)
Use case: Formatting phone numbers differently based on captured parts.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 3 - Date Extraction

Scenario: Extract date components from different formats.
text = "Event on 2024-03-15"
Question: Capture year, month, day separately.

Your pattern: r'([1-2]\d\d{2})-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])'

Validates year range (1000-2999)
Validates month (01-12)
Validates day (01-31)

Simpler extraction (if you trust the format):
pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
Usage:
match = pattern.search(text)
year = match.group(1)   # "2024"
month = match.group(2)  # "03"
day = match.group(3)    # "15"

# Convert to different format
print(f"{month}/{day}/{year}")  # 03/15/2024
Use case: Parse dates from logs, convert formats, validate input.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 4 - Log Entry Parsing
Scenario: Extract components from log entries.
log = "[2024-01-15 14:30:22] ERROR: Connection failed"
Question: Capture:

Date (2024-01-15)
Time (14:30:22)
Level (ERROR)
Message (Connection failed)

pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2})\s(\d{2}:\d{2}:\d{2})\]\s([A-Z]+):\s(.+)')

Pattern breakdown:

\[ - literal [
(\d{4}-\d{2}-\d{2}) - group 1: date
\s - space
(\d{2}:\d{2}:\d{2}) - group 2: time
\] - literal ]
\s - space
([A-Z]+) - group 3: log level (uppercase letters)
:\s - colon and space
(.+) - group 4: message (everything else)

Usage:
pythonmatch = pattern.search(log)
date = match.group(1)     # "2024-01-15"
time = match.group(2)     # "14:30:22"
level = match.group(3)    # "ERROR"
message = match.group(4)  # "Connection failed"

Use case: Your W3P3 Log Analyzer project!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 5 - URL Parsing
Scenario: Extract components from URLs.
url = "https://www.example.com:8080/path/to/page?id=123"
Question: Capture:

Protocol (https)
Domain (www.example.com)
Port (8080)
Path (/path/to/page)

pattern = re.compile(r'(\w+:)//(\w{3}\.\w+\.\w{2,}):(\d{4})(\/\w+\/\w+\/\w+)')

Good attempt! But too rigid. More flexible:
Issues with your pattern:

\w{3} - requires exactly 3 chars (only matches "www")
\d{4} - requires exactly 4 digits (port 80 wouldnt match)
\/\w+\/\w+\/\w+ - requires exactly 3 path segments


pattern = re.compile(r'(https?)://([\w.-]+):(\d+)(\/[\w/]+)')

Better pattern breakdown:

(https?) - group 1: http or https
:// - literal
([\w.-]+) - group 2: domain (word chars, dots, dashes)
: - literal colon
(\d+) - group 3: port (1+ digits)
(\/[\w/]+) - group 4: path (slash, word chars, more slashes)

Usage:
match = pattern.search(url)
protocol = match.group(1)  # "https"
domain = match.group(2)    # "www.example.com"
port = match.group(3)      # "8080"
path = match.group(4)      # "/path/to/page"
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 6 - Name Extraction
Scenario: Extract first and last names, handling middle initials.
text = "Author: John Q. Smith"
Question: Capture first name and last name, optionally skipping middle initial.

For optional middle initial, use non-capturing group:
pattern = re.compile(r'(\w+)\s(?:\w\.\s)?(\w+)')
Pattern breakdown:

(\w+) - group 1: first name
\s - space
(?:\w\.\s)? - optional non-capturing: middle initial + dot + space
(\w+) - group 2: last name

Matches both:

"John Smith" → groups: ("John", "Smith")
"John Q. Smith" → groups: ("John", "Smith")

The ?: makes it non-capturing, and the ? after makes it optional!
Usage:
match = pattern.search("Author: John Q. Smith")
first = match.group(1)  # "John"
last = match.group(2)   # "Smith"
# Middle initial not captured

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 7 - Password Validation Components
Scenario: Check if password contains required components.
password = "MyP@ss123"
Question: Write patterns to check for:

At least one uppercase letter
At least one digit
At least one special character

Sub-Optimal
pattern1 = re.compile(r'[A-Z]')    # Uppercase ✓
pattern2 = re.compile(r'\W+')      # Non-word (includes spaces)
pattern3 = re.compile(r'\d+')      # Digits ✓

For password special chars, more specific:
pattern2 = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
Usage:
password = "MyP@ss123"

has_upper = bool(re.search(r'[A-Z]', password))       # True
has_digit = bool(re.search(r'\d', password))          # True
has_special = bool(re.search(r'[!@#$%^&*]', password)) # True

if has_upper and has_digit and has_special:
    print("Strong password!")
Use case: Your W3P4 Password Checker project!
Note: No need for + - just checking if it exists at all.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 8 - Address Parsing
Scenario: Extract components from a mailing address.
address = "123 Main Street, Apt 4B, Springfield, IL 62701"
Question: Capture:

Street number (123)
Street name (Main Street)
City (Springfield)
State (IL)
ZIP (62701)

Sub-optimal
pattern = re.compile(r'(\d+)\s(\w+\s\w+).\s(?:\w+.\s\w+).\s(\w+).\s(\w+)\s(\d+)')
Issues:
. matches ANY character (should be , for comma)
Street name assumes exactly 2 words
Apt pattern uses . instead of literal chars

Better pattern:
pattern = re.compile(r'(\d+)\s([\w\s]+),\s(?:Apt\s\w+,\s)?(\w+),\s([A-Z]{2})\s(\d{5})')
Pattern breakdown:

(\d+) - group 1: street number
\s - space
([\w\s]+) - group 2: street name (words + spaces)
,\s - comma + space
(?:Apt\s\w+,\s)? - optional non-capturing: apartment
(\w+) - group 3: city
,\s - comma + space
([A-Z]{2}) - group 4: state (2 uppercase letters)
\s - space
(\d{5}) - group 5: ZIP (5 digits)

Usage:
match = pattern.search(address)
street_num = match.group(1)   # "123"
street_name = match.group(2)  # "Main Street"
city = match.group(3)         # "Springfield"
state = match.group(4)        # "IL"
zip_code = match.group(5)     # "62701"
Use case: Your W3P5 Address Book project!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Real-World Groups Summary:
✓ Email parsing (username, domain)
✓ Phone number breakdown (area, prefix, suffix)
✓ Date extraction (year, month, day)
✓ Log parsing (timestamp, level, message)
✓ URL components (protocol, domain, port, path)
✓ Name handling (with optional middle initial)
✓ Password component checking
✓ Address parsing (street, city, state, ZIP)
Key patterns:

(...) - capture for extraction
(?:...) - group without capturing
(?:...)? - optional non-capturing group
Combine with match.group(1), group(2) to extract


------------------------------------------------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------

                                                            Session 2C: re Module Functions
Different functions for different tasks. Lets drill when to use each.

Round 1 - search() vs match()
Question: Whats the difference?
text = "The cat sat"
pattern = re.compile(r'cat')

result1 = pattern.search(text)
result2 = pattern.match(text)
Which one finds "cat"?

The difference is WHERE they look:
search() - looks ANYWHERE in string
match() - only looks at the START of string
text = "The cat sat"
pattern = re.compile(r'cat')

result1 = pattern.search(text)  # ✓ Found! (searches anywhere)
result2 = pattern.match(text)   # ✗ None (string doesn't START with "cat")
Pattern:

search() = find anywhere
match() = must be at beginning (like implicit ^)

When to use match():

Validating format from start (like form inputs)
"Does this string START with this pattern?"

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 2 - match() Practical Use
Question: Which function would you use to validate that a string is ONLY digits?
user_input = "12345"
A. search(r'\d+')
B. match(r'\d+')
C. fullmatch(r'\d+')

re.fullmatch(r'\d+', "12345")  # Match! (entire string is digits)
re.fullmatch(r'\d+', "12345a") # None (has non-digit)
Why not the others?

search(r'\d+') - matches "12345a" (finds digits, ignores 'a')
match(r'\d+') - matches "12345a" (starts with digits, doesnt check end)

Pattern:

fullmatch() = entire string must match exactly
Use for validation: "Is this ONLY digits/letters/valid format?"

Equivalent patterns:

fullmatch(r'\d+') = match(r'^\d+$')

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 3 - findall() Basics

Question: What does findall() return?
text = "Call 555-1234 or 555-5678"
numbers = re.findall(r'\d{3}-\d{4}', text)

depends on capturing groups:

Without capturing groups:
re.findall(r'\d{3}-\d{4}', text)
# ['555-1234', '555-5678'] - list of strings

With capturing groups:

re.findall(r'(\d{3})-(\d{4})', text)
# [('555', '1234'), ('555', '5678')] - list of tuples
Pattern:

findall() always returns a list
Items are strings if no groups
Items are tuples if pattern has groups


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 4 - findall() with Groups
text = "john@example.com and jane@test.org"
Question: Write code to extract all email addresses and separate usernames from domains.

Sub-Optimal
pattern = re.compile(r'(\w+)@(\w+\.\w{2,})')
results = pattern.findall(text)
# [('john', 'example.com'), ('jane', 'test.org')]

for username, domain in results:
    print(f"User: {username}, Domain: {domain}")

More flexible domain pattern:
pattern = re.compile(r'(\w+)@([\w.]+)') # [\w.]+ allows for multiple segments of . word
# Allows multiple dots in domain
Pattern: Use findall() with groups to extract multiple pieces from each match.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 5 - finditer() for Match Objects
Question: Whats the difference between findall() and finditer()?
pythontext = "cat at 0, dog at 10, bird at 20"
pattern = re.compile(r'\w+')

result1 = pattern.findall(text)
result2 = pattern.finditer(text)

finditer() returns an iterator of match objects, not strings.
findall() - returns list of strings:
result1 = pattern.findall(text)
# ['cat', 'at', 'dog', 'at', 'bird', 'at']

finditer() - returns iterator of match objects:
result2 = pattern.finditer(text)
# <callable_iterator object...>

for match in result2:
    print(match.group(), match.start(), match.end())
# cat 0 3
# at 4 6
# dog 12 15
# ...
When to use finditer():

Need position info (start/end)
Need match objects (not just strings)
Processing large text (iterator is memory-efficient)

When to use findall():

Just need the matched text
Want a simple list

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 6 - sub() for Replacement
Question: What does this do?
text = "Call 555-1234 or 555-5678"
result = re.sub(r'\d', 'X', text)
# "Call XXX-XXXX or XXX-XXXX"

Pattern: re.sub(pattern, replacement, text) - substitutes matches
More examples:

# Replace all spaces with underscores
re.sub(r'\s', '_', "hello world")  # "hello_world"

# Remove all digits
re.sub(r'\d', '', "abc123")  # "abc"

# Censor words
re.sub(r'bad', '***', "bad word")  # "*** word"

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 7 - sub() with Groups
Scenario: Swap first and last name format.
text = "Smith, John"
Question: Convert to "John Smith" using sub() with groups.

sub() has built-in group references:
Correct:
result = re.sub(r'(\w+), (\w+)', r'\2 \1', text)
# "John Smith"
Pattern breakdown:

(\w+), (\w+) - captures: (1) last name, (2) first name
r'\2 \1' - replacement: group 2, space, group 1

Backreferences in replacement:

\1 = first captured group
\2 = second captured group
\3 = third, etc.

More examples:
python# Format phone numbers
re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', '5551234567')
# "(555) 123-4567"

# Add dashes to dates
re.sub(r'(\d{4})(\d{2})(\d{2})', r'\1-\2-\3', '20240315')
# "2024-03-15"

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 8 - sub() with Function
Advanced: You can pass a function to sub() for complex replacements.
def censor(match):
    word = match.group()
    return '*' * len(word)

text = "This is bad and ugly"
result = re.sub(r'bad|ugly', censor, text)
What does this produce?

result = "This is *** and ****"
Pattern:

bad → *** (3 asterisks)
ugly → **** (4 asterisks)

How it works:

Pattern finds each match
Passes match object to function
Function returns replacement string
Original text updated with replacement

Use cases:

Dynamic replacements (based on match length, content)
Complex transformations
Your W3P2 Text Cleaner project!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 9 - split() with Regex
Question: Whats the difference?
text = "apple,banana;cherry orange"

result1 = text.split(',')
result2 = re.split(r'[,;\s]+', text)

String split() - one delimiter:
result1 = text.split(',')
# ['apple', 'banana;cherry orange']
# Only splits on comma

Regex split() - multiple delimiters:
result2 = re.split(r'[,;\s]+', text)
# ['apple', 'banana', 'cherry', 'orange']
# Splits on comma, semicolon, or spaces

Pattern: re.split(pattern, text) - split on any match
Use cases:
# Split on any whitespace
re.split(r'\s+', "hello  world\t\ntest")
# ['hello', 'world', 'test']

# Split on punctuation
re.split(r'[,.!?]+', "Hello, world! How are you?")
# ['Hello', ' world', ' How are you', '']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 10 - compile() Benefits
Question: When should you use compile()?
# Option 1 - compile first
pattern = re.compile(r'\d+')
for text in texts:
    result = pattern.search(text)

# Option 2 - don't compile
for text in texts:
    result = re.search(r'\d+', text)

compile() is about efficiency, not what it matches.
Use compile() when:

Using same pattern multiple times
Pattern gets compiled once, reused many times
More efficient

Dont compile when:

Using pattern only once
Not worth the extra line of code

Example:
python# GOOD - compile for reuse
pattern = re.compile(r'\d+')
for line in file:
    match = pattern.search(line)  # Reuses compiled pattern

# LESS EFFICIENT - compiles every iteration
for line in file:
    match = re.search(r'\d+', line)  # Recompiles each time
Pattern:

One pattern, many uses → compile()
One-time search → direct re.search()

Also: Compiled patterns are more readable if pattern is complex.

------------------------------------------------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------

                                                    Character Class Cheat Sheet
# Basic
[abc]           # a, b, or c
[^abc]          # NOT a, b, or c

# Ranges
[a-z]           # Any lowercase
[A-Z]           # Any uppercase
[0-9]           # Any digit
[a-zA-Z]        # Any letter
[a-zA-Z0-9]     # Alphanumeric

# Common patterns
[aeiou]         # Vowels
[^aeiou]        # Consonants
[0-9a-fA-F]     # Hex digit
[\w-]           # Word char or dash
[.!?]           # Sentence punctuation
[\s\S]          # ANY character (whitespace or non-whitespace)

# Escaping inside brackets
[\.]            # Literal dot
[\-]            # Literal dash (or put at start/end)
[\[]            # Literal [
[\]]            # Literal ]
[\\]            # Literal backslash

------------------------------------------------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------------------------------------------------------------

                                                    DAY 3: Advanced Patterns & Behavior

    Session 3A: Greedy vs Non-Greedy Quantifiers
Understanding how regex engines consume text is critical.

Round 1 - Greedy by Default
Question: How much does this match?
text = "<div>Hello</div>"
pattern = re.compile(r'<.*>')
match = pattern.search(text)
Does it match:
A. <div>
B. <div>Hello</div>

match.group()  # "<div>Hello</div>"
Why? .* is greedy - matches as much as possible.
Step by step:

< matches the first <
.* matches "div>Hello</div" (as much as possible)
> matches the last >

Pattern: By default, *, +, ?, {n,m} are greedy (match maximum)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 2 - Making it Non-Greedy
Question: How do you make * match as little as possible?
Hint: Add one character after *

pattern = re.compile(r'<.*?>')
Now it matches:
text = "<div>Hello</div>"
match = pattern.search(text)
match.group()  # "<div>" (stops at first >)
Pattern: Add ? after quantifier to make it non-greedy (lazy)
Greedy vs Non-greedy:

* - greedy (maximum)
*? - non-greedy (minimum)
+ - greedy
+? - non-greedy
{n,m} - greedy
{n,m}? - non-greedy


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 3 - Practical Example
Scenario: Extract text between quotes.
text = 'He said "hello" and "goodbye"'
Question: What do these patterns match?
pattern1 = re.compile(r'".*"')
pattern2 = re.compile(r'".*?"')

Greedy ".*":
nmatch = pattern1.search(text)
match.group()  # '"hello" and "goodbye"'
# From FIRST quote to LAST quote (everything)

Non-greedy ".*?":
match = pattern2.search(text)
match.group()  # '"hello"'
# From FIRST quote to NEXT quote (minimal)

With findall():
re.findall(r'".*"', text)    # ['"hello" and "goodbye"'] (one match)
re.findall(r'".*?"', text)   # ['"hello"', '"goodbye"'] (two matches)
Pattern: Non-greedy stops at first valid match point.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 4 - When Non-Greedy Fails
Tricky case:
text = "<div>Hello</div><span>World</span>"
pattern = re.compile(r'<.*?>')
Question: What does the first match return
match = pattern.search(text)
match.group()  # "<div>"
Pattern <.*?> breakdown:

< - literal
.*? - minimal characters
> - next >

Stops at first >, giving "<div>"

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 5 - HTML Tag Extraction Problem
Common mistake: Trying to parse HTML with regex.
html = "<div class='container'>Content</div>"
pattern = re.compile(r'<.*?>')
Question: What does this match? Is it useful?

It matches: <div class='container'>
Why this matters for YOUR projects:
Your W3P2 Text Cleaner might encounter:

HTML tags in scraped text
XML-like structures
Markdown formatting

The lesson: <.*?> works for simple cases but breaks with:

Nested tags: <div><span>text</span></div>
Attributes with >: <div data="x>y">
Comments: <!-- comment -->

Better approach for your projects:
# Remove simple HTML tags
re.sub(r'<[^>]+>', '', text)
# [^>]+ means "anything except >"
Key takeaway: Non-greedy helps, but character classes are often better!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 6 - Greedy with Boundaries
Question: Write a pattern to extract everything between START and END (non-greedy).
pythontext = "START content here END more START other END"
Want: "content here" and "other"

pattern = re.compile(r'START.*?END')
matches = pattern.findall(text)
# ['START content here END', 'START other END']

To get just the content (without START/END):
pattern = re.compile(r'START(.*?)END')
matches = pattern.findall(text)
# ['content here', 'other']

Pattern: (.*?) in a group captures minimal content between markers.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 7 - Greedy Until Specific End
Scenario: Extract everything until first occurrence of "END".
pythontext = "Some text END more text END final"
Question: Write pattern to get "Some text" (stop at first END).

pattern = re.compile(r'(.*?)END')
match = pattern.search(text)
match.group(1)  # "Some text "
Pattern: (.*?)END captures everything up to first END.
Key concept: Non-greedy stops at FIRST valid match point.

Session 3A Summary:
✓ Greedy (default): *, +, ?, {n,m} - match maximum
✓ Non-greedy: *?, +?, ??, {n,m}? - match minimum
✓ Greedy looks ahead for last valid end point
✓ Non-greedy stops at first valid end point
✓ Character classes often better than non-greedy (e.g., [^>]+ vs .*?)
Common patterns:

".*?" - quoted strings (non-greedy)
<.*?> - simple tags (non-greedy)
[^>]+ - content without character (better than non-greedy)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

# findall() - returns list of strings
# finditer() - returns iterator of match objects
# use finditer() when you need .group() on each match

for match in pattern.finditer(text):
    print(match.group(1))  # first captured group
    print(match.group(2))  # second captured group



------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------






------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------





------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------


































