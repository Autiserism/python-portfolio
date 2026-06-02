    CHARACTER CLASSES [ ] - DEEP DIVE

Part 1: The Basics

Round 1 - What [ ] Does
Core concept: [abc] means "match ONE character that is either a, b, OR c"
pattern = re.compile(r'[aeiou]')
Question: Which of these match?

"cat"
"dog"
"xyz"

Pattern [aeiou] matches any ONE vowel.
Test strings:

"cat" ✓ - contains 'a' (matches)
"dog" ✓ - contains 'o' (matches)
"xyz" ✗ - no vowels (doesnt match)

Key point: [aeiou] matches if the string contains ANY of those characters.
What it matches IN each string:

"cat" → matches the 'a'
"dog" → matches the 'o'

pattern.search() only matches the letter
pattern.findall() matches the whole word that has that letter in it

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 2 - [ ] Matches ONLY ONE Character
pattern = re.compile(r'[abc]')
Question: How many characters does this match in "abcabc"?
A. 1 character
B. 3 characters (abc)
C. 6 characters (all of them)

Depends on the function:
With search() - finds first match:
re.search(r'[abc]', 'abcabc')
# Matches 'a' (first one only)

With findall() - finds all matches:
re.findall(r'[abc]', 'abcabc')
# ['a', 'b', 'c', 'a', 'b', 'c'] - all 6 characters
Key point:

The pattern [abc] matches one character per match
How many total matches depends on the function
Each bracket set [...] = ONE character position

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Part 2: Ranges
Round 3 - Range Shorthand
These are equivalent:
[abcdefghijklmnopqrstuvwxyz]  # Long way
[a-z]                          # Range shorthand
Question: Write character classes for:

Any uppercase letter
Any digit
Any letter (upper or lower)

[A-Z] ✓ uppercase letter
[0-9] or \d ✓ any digit
[A-Z][a-z] ✗ - this is TWO character classes (matches "Ab", "Xy", etc.)

For any letter (one character):

[A-Za-z]  # Combines both ranges in ONE bracket
Pattern: Multiple ranges in one bracket = ONE character from ANY range
Examples:

[A-Za-z] - any letter
[A-Za-z0-9] - any alphanumeric
[0-9a-f] - hex digit (0-9 or a-f)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 4 - Combining Ranges
Question: What does [A-Za-z0-9_] match?

It matches ONE character that is ANY of those (not one of each).
Pattern [A-Za-z0-9_] matches ONE character:

Could be uppercase: A, B, C...
OR lowercase: a, b, c...
OR digit: 0, 1, 2...
OR underscore: _

Matches (single characters):

"A" ✓
"z" ✓
"5" ✓
"_" ✓
"AB" - matches 'A', then 'B' (two separate matches)

Doesnt match:

"!" ✗
"$" ✗
" " (space) ✗

Note: [A-Za-z0-9_] is the same as \w!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Part 3: Negation [^ ]
Round 5 - Caret Inside Brackets
Critical: ^ has different meanings!
r'^cat'   # Start of string (outside brackets)
r'[^cat]' # NOT c, a, or t (inside brackets)
Question: What does [^0-9] match?

Pattern [^0-9] matches any character that is NOT a digit:
Matches:

"a" ✓
"Z" ✓
"!" ✓
" " (space) ✓

Doesnt match:

"5" ✗
"0" ✗

Same as: \D (non-digit)


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 6 - Negation with Ranges
Question: Write a pattern that matches any character that is NOT a letter.

pattern = re.compile(r'[^A-Za-z]')
Matches:

Digits: "5" ✓
Punctuation: "!" ✓
Spaces: " " ✓
Symbols: "@" ✓

Doesnt match:

"a" ✗
"Z" ✗

Pattern: [^range] = NOT anything in this range

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Part 4: Special Characters Inside [ ]
Round 7 - Most Special Chars Lose Meaning
Inside brackets, most special characters are literal!
[.]     # Literal dot (not "any character")
[*]     # Literal asterisk (not "zero or more")
[+]     # Literal plus (not "one or more")
[?]     # Literal question mark (not "optional")
Question: What does [.!?] match?

Answer: . ! ?

pattern = re.compile(r'[.!?]')
Matches any ONE of:

"." ✓
"!" ✓
"?" ✓

Use case: Match sentence-ending punctuation

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 8 - Characters That Still Need Escaping
Three characters still need escaping inside [ ]:

] - closing bracket
\ - backslash
^ - caret (if at start)
- - dash (if between characters)

Question: How would you match a literal dash?
[a-z]   # Range from a to z
[a\-z]  # Literal: a, dash, or z

Answer: \-

[a\-z]  # Matches: 'a', '-', or 'z'
Alternative (dash at start or end):
[-az]   # Also matches: 'a', '-', or 'z'
[az-]   # Same thing

Pattern: Escape with \- or place at start/end

More examples:
[\[\]]    # Matches '[' or ']'
[\\]      # Matches '\'
[\^abc]   # Matches '^', 'a', 'b', or 'c'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Part 5: Real-World Use Cases
Round 9 - Phone Number Validation
Scenario: Match phone numbers that can have dots OR dashes.
pythontext = "Call 555-1234 or 555.1234"
Question: Write a pattern to match both formats.

pattern = re.compile(r'(?:\+?[0-9][\s\-\.]?)?(\(?\d{3}\)?)?[\s\-\.]?(\d{3})[\s\-\.]?(\d{4})')

But for just matching "555-1234" or "555.1234", simpler:
pattern = re.compile(r'\d{3}[-\.]\d{4}')
Pattern breakdown:

\d{3} - 3 digits
[-\.] - dash OR dot (one character from this set)
\d{4} - 4 digits

Key point: [-\.] means "match a dash or a dot"
Your pattern handles:

Country codes
Area codes with/without parentheses
Multiple separator styles
Much more robust!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 10 - File Extension Matching
Scenario: Match image files (jpg, jpeg, png, gif).
filename = "photo.jpg"
Question: Write a pattern for the file extension.

pattern = re.compile(r'\.(jpg|jpeg|png|gif)$')
OR using alternation in character class for j-p-e-g:
pythonpattern = re.compile(r'\.jpe?g$|\.png$|\.gif$')
Best for this case - character class for extension letters:

pattern = re.compile(r'\.[a-z]{3,4}$')
# Matches any 3-4 letter extension
But for SPECIFIC extensions, first pattern is clearest.


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 11 - Username Validation
Scenario: Username must be:

3-16 characters
Letters, numbers, underscore, dash only
Cannot start with number

Question: Write the validation pattern.

pattern = re.compile(r'^[A-Za-z][\w\-]{2,15}$')
# Remove the + inside brackets - it's literal, not needed
Your pattern breakdown:

^ - start
[A-Za-z] - first char must be letter ✓
[\w\-]{2,15} - 2-15 more chars (letters, digits, underscore, dash) ✓
$ - end

Total length: 1 + (2 to 15) = 3 to 16 ✓
The + in [\w+\-] is literal plus sign (not "one or more"). Remove it!
Corrected:
pattern = re.compile(r'^[A-Za-z][\w-]{2,15}$')
# Dash at end doesn't need escape

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 12 - Hex Color Codes
Scenario: Match valid hex colors (#RGB or #RRGGBB).
Examples: #F00, #FF0000, #a1b2c3
Question: Write the pattern.

pattern = re.compile(r'^\#[\w]{6}')
Close! Issues:

\w includes underscore (hex doesnt allow that)
Only matches 6 chars (#RRGGBB), not 3 (#RGB)
Missing $ anchor

Better:
pythonpattern = re.compile(r'^#[0-9A-Fa-f]{6}$')
# Only 6-char format
For both 3 and 6 char:
pythonpattern = re.compile(r'^#[0-9A-Fa-f]{3}([0-9A-Fa-f]{3})?$')
Pattern breakdown:

^# - must start with #
[0-9A-Fa-f]{3} - 3 hex digits (required)
([0-9A-Fa-f]{3})? - optional 3 more hex digits
$ - end

Character class: [0-9A-Fa-f] = hex digit (not \w)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

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
