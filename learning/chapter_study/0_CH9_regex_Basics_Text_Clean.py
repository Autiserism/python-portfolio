

W3P2 - Text Cleaner Pattern Prep

Session: Text Cleaning Patterns

    Round 1 - Removing Extra Spaces
Problem: Multiple spaces between words.
text = "Hello    world     test"
Question: Write pattern to replace multiple spaces with single space.
'''
Sub-Optimal
pattern = re.sub(r'[\s]+', ' ', text)
result = pattern.replace(text, '\s')
'''
re.sub() returns the result directly - no second step needed.
Correct:
result = re.sub(r'\s+', ' ', text)
# "Hello world test"
Pattern breakdown:

\s+ - one or more whitespace chars
' ' - replacement (single space)
Returns cleaned text

Your confusion:

re.sub() IS the replacement - dont call .replace() after
No need for [\s] - just \s works

Pattern: re.sub(pattern, replacement, text) returns new string

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 2 - Removing Leading/Trailing Spaces

text = "   Hello world   "
Question: Two ways to clean this:
A. Using regex
B. Using string method
'''
Sub-Optimal
result = re.sub(r'\s{2,}', '', text)
text = text.strip()
'''
B is correct! text.strip() ✓
A has an issue:
re.sub(r'\s{2,}', '', text)
# Only removes 2+ spaces, leaves single spaces

For regex approach:
result = re.sub(r'^\s+|\s+$', '', text)
# "Hello world"
Pattern breakdown:

^\s+ - whitespace at start
| - OR
\s+$ - whitespace at end

But for leading/trailing, string method is simpler:
text.strip()    # Both ends
text.lstrip()   # Left only
text.rstrip()   # Right only
Pattern: Use .strip() for edges, regex for middle

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 3 - Removing Special Characters

Problem: Remove everything except letters, numbers, and spaces.
text = "Hello! World? 123... test@#$"
Question: Write pattern to keep only alphanumeric and spaces.

pattern = re.compile(r'[\w\s]+')#(r'[A-Za-z1-9\s]+')
#result = pattern.findall(text)

findall() returns a list of matches, not cleaned text.
Your result would be:
['Hello', 'World', '123', 'test']  # List, not string

For cleaning, use sub() with negation:
result = re.sub(r'[^\w\s]', '', text)
# "Hello World 123 test"

Pattern breakdown:

[^\w\s] - NOT word char or space (the ^ inside brackets = NOT)
'' - replace with nothing (remove it)

Key difference:

findall(r'[\w\s]+') - FIND good parts (returns list)
sub(r'[^\w\s]', '') - REMOVE bad parts (returns cleaned string)

For text cleaning, use sub() with [^...] negation!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 4 - Censoring Banned Words
Problem: Replace banned words with asterisks.

text = "This is bad and very bad behavior"
banned = ['bad', 'very']
Question: Write pattern to censor "bad" (replace with "***").

Issue: Without word boundaries, "bad" matches in "badge" → "***ge"

for word in banned:
    text = re.sub(rf'\b{word}\b', '*' * len(word), text)
Pattern breakdown:

\b{word}\b - word boundaries (whole word only)

rf'...' - f-string + raw string for variable insertion

'*' * len(word) - asterisks matching word length

Complete censoring function:
def censor_words(text, banned_words):
    for word in banned_words:
        # Case-insensitive option
        text = re.sub(rf'\b{word}\b', '*' * len(word), text, flags=re.IGNORECASE)
    return text

result = censor_words(text, banned)
# "This is *** and **** *** behavior"
Key: \b ensures "bad" doesnt match "badge" or "badminton"


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 5 - Fixing Capitalization
Problem: Fix inconsistent capitalization.
text = "hELLo WOrLD. hoW ARE yOu?"
Question: Two approaches - which would you use?
A. Regex with function
B. String methods

pattern = re.compile(r'[A-Z]')
def clean_upper(text):
    result = pattern.findall(text)
    for letter in result:
        text = re.sub(rf'{letter}' , letter.lower() , text)
    return text
regex_clean = clean_upper(text)
OR
text = text.lower()

Your regex approach works but is way too complex for simple case conversion!
String methods are much simpler:
# All lowercase
text.lower()
# "hello world. how are you?"

# Title Case (first letter of each word)
text.title()
# "Hello World. How Are You?"

# Sentence case (capitalize after periods)
text.capitalize()
# "Hello world. how are you?"

When to use regex for capitalization:
Capitalize after periods:
def capitalize_sentences(text):
    # Lowercase everything first
    text = text.lower()
    # Capitalize after period + space
    text = re.sub(r'(^|[.!?]\s+)([a-z])', lambda m: m.group(1) + m.group(2).upper(), text)
    return text

result = capitalize_sentences(text)
# "Hello world. How are you?"

Pattern for W3P2:

Use string methods for simple case changes (.lower(), .title())
Use regex only for complex patterns (sentence boundaries)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 6 - Removing Extra Newlines
Problem: Multiple blank lines.
text = "Line 1\n\n\n\nLine 2\n\nLine 3"
Question: Replace multiple newlines with max 2 (one blank line).

This replaces ALL newlines (including single) with double.

Your pattern:
re.sub(r'[\n]+', '\n\n', text)
# Turns single newlines into double too!

For "max 2 newlines" (one blank line):
result = re.sub(r'\n{3,}', '\n\n', text)
# OR
result = re.sub(r'\n\n+', '\n\n', text)
Pattern breakdown:

\n{3,} - 3 or more newlines
\n\n - replace with exactly 2

Preserves single newlines, collapses 3+ to 2.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 7 - Complete Text Cleaner Pipeline
Question: Build a complete cleaning function that:

Removes leading/trailing spaces
Collapses multiple spaces to one
Removes special characters (keep letters, numbers, spaces, periods)
Capitalizes sentences
Censors banned words

text = "  hELLo!!!   WoRLD???    This  is   bad  text...   "
banned = ['bad']

text = re.sub(r'[^A-Za-z\d\s.]', '',text)
text = text.capitalize()
text = text.split()
text = ' '.join(text)
for word in banned:
    result = re.sub(rf'\b{word}\b', '*'*len(word), text)

Good approach! A few issues:

✓ Special char removal works
.capitalize() only capitalizes first letter of entire string (not sentences)
✓ split() + join() trick collapses spaces - clever!
Banned loop doesnt save result back to text

Corrected complete function:
def clean_text(text, banned_words):
    # 1. Remove special characters (keep letters, numbers, spaces, periods)
    text = re.sub(r'[^A-Za-z\d\s.]', '', text)

    # 2. Collapse multiple spaces to one (your trick!)
    text = ' '.join(text.split())

    # 3. Strip leading/trailing spaces
    text = text.strip()

    # 4. Fix capitalization - lowercase then capitalize sentences
    text = text.lower()
    text = re.sub(r'(^|[.!?]\s+)([a-z])',
                  lambda m: m.group(1) + m.group(2).upper(),
                  text)

    # 5. Censor banned words
    for word in banned_words:
        text = re.sub(rf'\b{word}\b', '*' * len(word), text, flags=re.IGNORECASE)

    return text

# Test
text = "  hELLo!!!   WoRLD???    This  is   bad  text...   "
banned = ['bad']
result = clean_text(text, banned)
print(result)
# "Hello world. This is *** text."


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

W3P2 Pattern Cheat Sheet
# Remove extra spaces
re.sub(r'\s+', ' ', text)

# Remove special characters (keep alphanumeric + spaces)
re.sub(r'[^\w\s]', '', text)

# Remove specific characters
re.sub(r'[!@#$%]', '', text)

# Collapse multiple newlines
re.sub(r'\n{3,}', '\n\n', text)

# Remove leading/trailing spaces
text.strip()

# Collapse spaces (no regex needed!)
' '.join(text.split())

# Censor words with boundaries
for word in banned:
    text = re.sub(rf'\b{word}\b', '*' * len(word), text, flags=re.IGNORECASE)

# Capitalize sentences (complex)
text = text.lower()
text = re.sub(r'(^|[.!?]\s+)([a-z])',
              lambda m: m.group(1) + m.group(2).upper(),
              text)

# Simple case changes
text.lower()      # all lowercase
text.upper()      # ALL UPPERCASE
text.title()      # Title Case
text.capitalize() # First letter only

Key Patterns for W3P2
✓ re.sub(r'[^\w\s]', '', text) - remove special chars
✓ re.sub(r'\s+', ' ', text) - collapse spaces
✓ ' '.join(text.split()) - collapse spaces (no regex)
✓ re.sub(rf'\b{word}\b', replacement, text, flags=re.IGNORECASE) - word censoring
✓ .strip(), .lower(), .title() - string methods
✓ lambda in re.sub() - dynamic replacements



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
