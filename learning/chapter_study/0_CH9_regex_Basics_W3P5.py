W3P5 - Mini Address Book Pattern Prep
Your project: Build an address book with add/search/view contacts. Validate input, search by name/phone/email.

Session: Contact Management Patterns

Round 1 - Review: Contact Validation
You already know these from W3P1, but lets refresh:
# Name (first + last)
r'^[A-Za-z]+\s[A-Za-z]+$'

# Phone (flexible format)
r'^\d{3}[-.]?\d{3}[-.]?\d{4}$'

# Email
r'^[\w._-]+@[\w.-]+\.[a-zA-Z]{2,}$'
Question: Write validation for a full address format:
"123 Main St, Toronto, ON, M5V 3A8"
Pattern should capture: street, city, province, postal code

r'^([\d\s\w]+),\s(\w+),\s([A-Z]{2}),\s([A-Za-z]\d[A-Za-z][\s.-]?\d[A-Za-z]\d)$'
#  Group 1       Group 2  Group 3      Group 4 (postal code)
Test:
address = "123 Main St, Toronto, ON, M5V 3A8"
pattern = re.compile(r'^([\d\s\w]+),\s(\w+),\s([A-Z]{2}),\s([A-Za-z]\d[A-Za-z][\s.-]?\d[A-Za-z]\d)$')
match = pattern.search(address)

if match:
    street, city, province, postal = match.groups()
    print(f"Street: {street}")
    print(f"City: {city}")
    print(f"Province: {province}")
    print(f"Postal: {postal}")
Output:
Street: 123 Main St
City: Toronto
Province: ON
Postal: M5V 3A8
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 2 - Partial Name Search
Scenario: Search contacts by partial name match.
contacts = [
    "John Smith",
    "Jane Johnson",
    "Bob Johnston",
    "Alice Johns"
]
Question: Find all contacts with "John" (case-insensitive).

r'john'  # Matches: the word "john"
For searching multiple contacts:
contacts = [
    "John Smith",
    "Jane Johnson",
    "Bob Johnston",
    "Alice Johns"
]

# Find all contacts containing "john" (case-insensitive)
results = [name for name in contacts
           if re.search(r'john', name, re.IGNORECASE)]

print(results)
# ['John Smith', 'Jane Johnson', 'Bob Johnston', 'Alice Johns']
Pattern: Use list comprehension with re.search() to filter.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 3 - Search by Multiple Fields
Scenario: Contact dictionary with multiple fields.
contacts = [
    {"name": "John Smith", "phone": "416-555-1234", "email": "john@email.com"},
    {"name": "Jane Johnson", "phone": "647-555-5678", "email": "jane@test.com"},
    {"name": "Bob Wilson", "phone": "416-555-9999", "email": "bob@email.com"}
]
Question: Write a function to search contacts by ANY field (name, phone, or email).

def search_contacts(contacts, query):
    """Search contacts by any field"""
    results = []

    for contact in contacts:
        # Check all values in contact
        for value in contact.values():
            if re.search(query, str(value), re.IGNORECASE):
                results.append(contact)
                break  # Found match, stop checking this contact

    return results

# Test
contacts = [
    {"name": "John Smith", "phone": "416-555-1234", "email": "john@email.com"},
    {"name": "Jane Johnson", "phone": "647-555-5678", "email": "jane@test.com"},
    {"name": "Bob Wilson", "phone": "416-555-9999", "email": "bob@email.com"}
]

# Search for "john"
results = search_contacts(contacts, "john")
print(results)
# [{'name': 'John Smith', ...}, {'name': 'Jane Johnson', ...}]

# Search for "416"
results = search_contacts(contacts, "416")
print(results)
# [{'name': 'John Smith', ...}, {'name': 'Bob Wilson', ...}]

# Search for "email.com"
results = search_contacts(contacts, "email")
print(results)
# [{'name': 'John Smith', ...}, {'name': 'Bob Wilson', ...}]
Key points:

str(value) handles non-string fields (like phone numbers stored as int)
break stops checking once match found in one field
Returns full contact dictionaries

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 4 - Phone Number Normalization
Problem: Users enter phones in different formats:

"4165551234"
"416-555-1234"
"(416) 555-1234"
"416.555.1234"

Question: Write function to extract just the digits for comparison.

phones = ["4165551234", "416-555-1234", "(416) 555-1234", "416.555.1234"]
cleaned = cleanPN(phones)
print(cleaned)
# ['4165551234', '4165551234', '4165551234', '4165551234']

Alternative Approaches
Option 1 - List comprehension (more Pythonic):

def clean_phones(phones):
    return [re.sub(r'[^\d]', '', phone) for phone in phones]

Option 2 - Using \D (non-digit shorthand):
def clean_phone(phone):
    return re.sub(r'\D', '', phone)  # \D = [^\d]

Option 3 - For single phone in search:
def normalize_phone(phone):
    """Remove all non-digits from phone number"""
    return re.sub(r'\D', '', phone)

# Search with normalized comparison
def search_by_phone(contacts, search_phone):
    normalized_search = normalize_phone(search_phone)

    results = []
    for contact in contacts:
        normalized_contact = normalize_phone(contact['phone'])
        if normalized_search in normalized_contact:
            results.append(contact)

    return results

# Test
search_by_phone(contacts, "(416) 555-1234")
# Finds: 416-555-1234, (416) 555-1234, 4165551234

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 5 - Extracting Area Code
Question: Extract just the area code from normalized phone.
phone = "4165551234"  # Want: "416"

pattern = re.compile(r'^(\d{3})')

phone = "4165551234"
match = pattern.search(phone)
area_code = match.group(1)
print(area_code)  # "416"
Or even simpler - string slicing:
phone = "4165551234"
area_code = phone[:3]
print(area_code)  # "416"
When you WOULD need (?:\.?):
  # For non-normalized phones
pattern = re.compile(r'^(\d{3})[\-\.]?(\d{3})[\-\.]?(\d{4})$')
phone = "416-555-1234"
match = pattern.search(phone)
area, prefix, suffix = match.groups()
# "416", "555", "1234"
For W3P5: Since youre normalizing phones, use string slicing phone[:3].


------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 6 - Display Formatting
Scenario: Store normalized "4165551234", display as "(416) 555-1234".

Question: Write function to format phone for display.

Digit Extraction - Three Approaches
Your Method:
patternPN = re.compile(r'(\d{1})')
results = re.findall(patternPN, num)
results = ''.join(results)
# Works! Finds each digit, joins them
Simpler - sub():

  results = re.sub(r'\D', '', num)
# Removes non-digits directly (one operation)
Simplest - findall():

  results = ''.join(re.findall(r'\d', num))
# No need for {1}, \d already means one digit
All work! re.sub(r'\D', '') is most common.

Display Formatting - Your Code Analysis
Your display function:

  pattern = re.compile(r'^(1)?(\d{3})(\d{3})(\d{4})')
ext, area, prefix, suffix = match.groups()
if not ext:

    ext = '0'
print(f"+{ext}({area}){prefix}-{suffix}")
Strengths:
✓ Handles optional country code with (1)?
✓ Captures all components
✓ Good formatting structure
Issue:
Setting ext = '0' makes "+0(416)555-1234" - should be "(416) 555-1234" without +0.

Improved Version
  def display_phone(phone):
    """Format normalized phone for display"""
    # Remove all non-digits
    digits = re.sub(r'\D', '', phone)

    # Pattern: optional 1, then 10 digits
    pattern = re.compile(r'^(1)?(\d{3})(\d{3})(\d{4})$')
    match = pattern.search(digits)

    if not match:
        return phone  # Invalid format, return as-is

    country, area, prefix, suffix = match.groups()

    # Format based on whether country code present
    if country:
        return f"+1 ({area}) {prefix}-{suffix}"
    else:
        return f"({area}) {prefix}-{suffix}"

# Test
phones = [
    "4175551234",
    "+1 415-555-1234",
    "(414) 555-1234",
    "411.555.1234"
]

for phone in phones:
    print(f"{phone:20} → {display_phone(phone)}")
Output:
4175551234           → (417) 555-1234
+1 415-555-1234      → +1 (415) 555-1234
(414) 555-1234       → (414) 555-1234
411.555.1234         → (411) 555-1234

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

W3P5 Pattern Cheat Sheet
python# Validation (from W3P1)
r'^[A-Za-z]+\s[A-Za-z]+$'                    # Name
r'^\d{3}[-.]?\d{3}[-.]?\d{4}$'              # Phone
r'^[\w._-]+@[\w.-]+\.[a-zA-Z]{2,}$'         # Email

# Address parsing
r'^([\d\s\w]+),\s(\w+),\s([A-Z]{2}),\s([A-Za-z]\d[A-Za-z]\s?\d[A-Za-z]\d)$'

# Phone normalization
re.sub(r'\D', '', phone)                     # Remove non-digits

# Partial search (any field)
re.search(query, str(value), re.IGNORECASE)

# Format phone for display
r'^(1)?(\d{3})(\d{3})(\d{4})$'              # Extract components

# Search contacts
[c for c in contacts if re.search(query, str(c['field']), re.IGNORECASE)]

Key Functions for W3P5
python# 1. Add contact with validation
def add_contact(name, phone, email, address):
    # Validate each field
    # Normalize phone
    # Store in list/dict

# 2. Search contacts
def search_contacts(contacts, query):
    # Search all fields
    # Return matches

# 3. Display contact
def display_contact(contact):
    # Format phone nicely
    # Pretty print all fields

# 4. List all contacts
def list_contacts(contacts):
    # Loop and display

# 5. Delete contact
def delete_contact(contacts, query):
    # Find and remove




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
