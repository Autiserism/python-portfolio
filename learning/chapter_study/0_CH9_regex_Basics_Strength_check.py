W3P4 - Password Strength Checker Pattern Prep
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Your project: Check password strength against multiple criteria, score it, give feedback.

Session: Password Validation Patterns

Round 1 - Basic Character Checks
Password requirements:

At least one uppercase letter
At least one lowercase letter
At least one digit
At least one special character

Question: Write patterns to check if password contains:

An uppercase letter
A digit

Your pattern:
r'[A-Za-z0-9!@#$%^&*+]+'
# Matches sequences of these characters
# Doesn't tell you if password HAS uppercase or digits
For checking presence, use search():
password = "Test123!"

# Check for uppercase
has_upper = re.search(r'[A-Z]', password)
if has_upper:
    print("Has uppercase ✓")

# Check for digit
has_digit = re.search(r'\d', password)
if has_digit:
    print("Has digit ✓")
Pattern: Use search() to CHECK if pattern exists in string.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 2 - Multiple Checks Function
Question: Write a function that checks all requirements:
def check_password(password):
    # Check: uppercase, lowercase, digit, special char
    # Return True if all present

Option 1 - Using and:
  def check_password(password):
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*]', password)

    return has_upper and has_lower and has_digit and has_special
Option 2 - Using all() (most elegant):
  def check_password(password):
    checks = [
        re.search(r'[A-Z]', password),      # uppercase
        re.search(r'[a-z]', password),      # lowercase
        re.search(r'\d', password),         # digit
        re.search(r'[!@#$%^&*]', password)  # special
    ]
    return all(checks)
all() returns True only if all items are truthy.
Test:
  print(check_password("Test123!"))   # True
print(check_password("test123!"))   # False (no uppercase)
print(check_password("Test123"))    # False (no special char)

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 3 - Lookahead Assertions

New concept: Check requirements WITHOUT consuming characters.
Problem with basic search:
# Want to check: starts with letter AND contains digit
pattern = r'^[A-Z]\d'  # This requires letter THEN digit
# Matches: "A1..."
# Doesn't match: "Ab1..." (has both but not adjacent)
Lookahead solution:
pattern = r'^(?=.*[A-Z])(?=.*\d)'
# Checks: has uppercase AND has digit (anywhere)
Lookahead syntax: (?=...) - assert that pattern ahead exists
Question: What does this pattern check?
r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'

Password: "Test123!"
Position:  ^

(?=.*[A-Z])  - Look ahead, see 'T' ✓ (dont move)
(?=.*[a-z])  - Look ahead, see 'e','s','t' ✓ (dont move)
(?=.*\d)     - Look ahead, see '1','2','3' ✓ (dont move)
.{8,}        - NOW consume 8 characters ✓
Result: Password must have uppercase AND lowercase AND digit AND be 8+ chars.

Key point: Lookaheads DONT consume characters - they just check.
Pattern breakdown:
r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'

^ - start of string
(?=.*[A-Z]) - lookahead: check uppercase exists (doesnt move position)
(?=.*[a-z]) - lookahead: check lowercase exists (still at start!)
(?=.*\d) - lookahead: check digit exists (still at start!)
.{8,} - NOW consume: match 8+ characters
$ - end of string

Key concept: All three lookaheads check from position 0!


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 4 - Lookahead Practice
Question: Write a pattern using lookaheads to check:

Contains uppercase
Contains digit
Contains special char [!@#$%^&*]
Minimum 10 characters

pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{10,}$'
password = "Test123!@#"

if re.search(pattern, password):
    print("Strong password ✓")
else:
    print("Password doesn't meet requirements")
Pattern checks:

(?=.*[A-Z]) - has uppercase ✓
(?=.*\d) - has digit ✓
(?=.*[!@#$%^&*]) - has special char ✓
.{10,} - at least 10 chars ✓

Note: Added ^ and $ anchors for exact matching.


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 5 - Detecting Weak Patterns
Weak patterns to avoid:

Sequential numbers: 123, 456, 789
Sequential letters: abc, xyz
Repeated characters: aaa, 111
Common words: password, admin

Question: Write pattern to detect 3+ repeated characters (like "aaa" or "111").

This uses backreferences - a new concept.
Pattern: (.)\1{2,}
Breakdown:

(.) - capture any character in group 1
\1 - match the SAME character as group 1
{2,} - repeat 2+ more times (total 3+)

How it works:
pythonpassword = "Test111Pass"

pattern = r'(.)\1{2,}'
match = re.search(pattern, password)

if match:
    print(f"Found repeated: {match.group()}")
    # "Found repeated: 111"
Step by step:
"Test111Pass"
     ^
     (.) captures '1'
     \1 matches another '1'
     \1 matches another '1'
     Total: "111" ✓
More examples:
pythonre.search(r'(.)\1{2,}', "aaa")      # Matches "aaa"
re.search(r'(.)\1{2,}', "aaabbb")   # Matches "aaa"
re.search(r'(.)\1{2,}', "Test")     # None
re.search(r'(.)\1{2,}', "bookkeeper") # Matches "ooo" or "eee"

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 6 - Sequential Patterns
Question: Detect sequential numbers like "123", "234", "789".
Hint: Use alternation |

Sequential patterns are different from repeated.
Repeated: same char (aaa, 111) → use backreference
Sequential: different chars (123, abc) → list them explicitly
For sequential numbers:
pythonpattern = r'(012|123|234|345|456|567|678|789|890)'
For sequential letters:
pattern = r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)'
Test:
pythonpassword = "Pass123word"

if re.search(r'(012|123|234|345|456|567|678|789)', password):
    print("Contains sequential numbers ✗")
    # Matches "123"
Common weak patterns to check:
weak_patterns = [
    r'(.)\1{2,}',           # Repeated chars (aaa, 111)
    r'(012|123|234|345|456|567|678|789)',  # Sequential numbers
    r'(abc|bcd|xyz)',       # Sequential letters
    r'(password|admin|user|test)',  # Common words
    r'(qwerty|asdfgh)',     # Keyboard patterns
]

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 7 - Password Strength Scoring
Scoring system:

Base: 0 points
Has uppercase: +1
Has lowercase: +1
Has digit: +1
Has special char: +1
Length 8-12: +1
Length 13+: +2
No weak patterns: +1

Question: Write function to score a password.

1. Variable Scope Problem
pythonfor pattern in weak_patterns:
    weak_pattern = re.search(pattern, password)
    if weak_pattern:
        break
if not weak_pattern:  # Could be undefined if loop doesn't run!
    score +=1
Better approach using any():
pythonhas_weak = any(re.search(pattern, password) for pattern in weak_patterns)
if not has_weak:
    score += 1
2. Return Type Inconsistency
pythonif len(password) < 8:
    return 'password too short'  # String
# ...
return score  # Int
Better:
if len(password) < 8:
    return 0  # Or handle separately

Improved Version
weak_patterns = [
    r'(.)\1{2,}',                              # Repeated chars
    r'(012|123|234|345|456|567|678|789)',      # Sequential numbers
    r'(abc|bcd|xyz)',                          # Sequential letters
    r'(password|admin|user|test)',             # Common words
    r'(qwerty|asdfgh)',                        # Keyboard patterns
]

def password_score(password):
    """Score password strength (0-8 scale)"""
    score = 0

    # Length scoring
    if len(password) >= 13:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        return 0  # Too short

    # Character type checks
    checks = [
        (r'[A-Z]', "uppercase"),
        (r'[a-z]', "lowercase"),
        (r'\d', "digit"),
        (r'[!@#$%^&*]', "special char"),
    ]

    for pattern, _ in checks:
        if re.search(pattern, password):
            score += 1

    # Check for weak patterns
    has_weak = any(re.search(pattern, password, re.IGNORECASE)
                   for pattern in weak_patterns)
    if not has_weak:
        score += 1

    return score

# Test
passwords = [
    "weak",           # 0 (too short)
    "password123",    # Low (common word)
    "Test123!",       # 6 (good)
    "MyP@ssw0rd2024", # 8 (excellent)
]

for pwd in passwords:
    score = password_score(pwd)
    print(f"{pwd:20} → Score: {score}/8")

Adding Feedback Function
def password_feedback(password):
    """Provide detailed feedback on password strength"""
    feedback = []

    if len(password) < 8:
        feedback.append("❌ Too short (minimum 8 characters)")
    elif len(password) < 13:
        feedback.append("⚠️  Could be longer (13+ recommended)")
    else:
        feedback.append("✓ Good length")

    if not re.search(r'[A-Z]', password):
        feedback.append("❌ Add uppercase letters")
    else:
        feedback.append("✓ Has uppercase")

    if not re.search(r'[a-z]', password):
        feedback.append("❌ Add lowercase letters")
    else:
        feedback.append("✓ Has lowercase")

    if not re.search(r'\d', password):
        feedback.append("❌ Add numbers")
    else:
        feedback.append("✓ Has numbers")

    if not re.search(r'[!@#$%^&*]', password):
        feedback.append("❌ Add special characters (!@#$%^&*)")
    else:
        feedback.append("✓ Has special characters")

    # Check weak patterns
    for pattern in weak_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            feedback.append("⚠️  Contains weak pattern (repeated/sequential/common)")
            break
    else:
        feedback.append("✓ No weak patterns detected")

    return feedback

# Test
password = "Test123"
score = password_score(password)
feedback = password_feedback(password)

print(f"Password: {password}")
print(f"Score: {score}/8")
print("\nFeedback:")
for item in feedback:
    print(f"  {item}")

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

# Character type checks
r'[A-Z]'           # Uppercase
r'[a-z]'           # Lowercase
r'\d'              # Digit
r'[!@#$%^&*]'      # Special characters

# Lookahead validation (all requirements in one pattern)
r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$'

# Weak pattern detection
r'(.)\1{2,}'       # Repeated characters (aaa, 111)
r'(123|234|345)'   # Sequential numbers
r'(abc|bcd|xyz)'   # Sequential letters
r'(password|admin)' # Common words (use re.IGNORECASE)

# Backreference syntax
(.)     # Capture character
\1      # Match same character as group 1
\1{2,}  # Same character 2+ more times (3+ total)

# Using any() for multiple checks
has_weak = any(re.search(pattern, pwd) for pattern in patterns)



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
