_ is Pythons "throwaway variable" convention.

What _ Means
The data structure:
  checks = [
    (r'[A-Z]', "uppercase"),      # Tuple: (pattern, description)
    (r'[a-z]', "lowercase"),
    (r'\d', "digit"),
    (r'[!@#$%^&*]', "special char"),
]
Each item is a tuple with TWO values.

Normal unpacking (using both values):
  for pattern, description in checks:
    if re.search(pattern, password):
        print(f"Found {description}")
        score += 1
Using _ (ignoring second value):
  for pattern, _ in checks:
    if re.search(pattern, password):
        score += 1
_ means: "I know there's a second value, but I'm not using it."

Why Use _?

Signals intent - tells other programmers "this value exists but isn't needed"
Cleaner than unused variable - avoids linter warnings
Convention - universally understood in Python


More Examples
Example 1 - Tuple unpacking:
  coordinates = (10, 20, 30)

# Want only x and y, ignore z
x, y, _ = coordinates
print(x, y)  # 10 20
Example 2 - Loop with index:
  items = ['a', 'b', 'c']

# Want items but not index
for _, item in enumerate(items):
    print(item)
Example 3 - Multiple throwaway values:
  data = (1, 2, 3, 4, 5)

# Want first and last only
first, _, _, _, last = data
# OR with * (Python 3)
first, *_, last = data

In Your Original Code
You wrote:
  has_upper = re.search(r'[A-Z]', password)
if has_upper:
    score +=1
has_lower = re.search(r'[a-z]', password)
if has_lower:
    score += 1
# ... repeat 4 times
My version with tuple unpacking:
  checks = [
    (r'[A-Z]', "uppercase"),
    (r'[a-z]', "lowercase"),
    (r'\d', "digit"),
    (r'[!@#$%^&*]', "special char"),
]

for pattern, _ in checks:  # _ ignores the description
    if re.search(pattern, password):
        score += 1
Same result, less repetition!

When You WOULD Use the Second Value
  def password_feedback(password):
    checks = [
        (r'[A-Z]', "uppercase letters"),
        (r'[a-z]', "lowercase letters"),
        (r'\d', "numbers"),
        (r'[!@#$%^&*]', "special characters"),
    ]

    missing = []
    for pattern, description in checks:  # NOW we use description
        if not re.search(pattern, password):
            missing.append(description)

    if missing:
        print(f"Password missing: {', '.join(missing)}")

Summary:

_ = "I'm unpacking this but not using it"
Convention, not special syntax
Makes code cleaner and signals intent
