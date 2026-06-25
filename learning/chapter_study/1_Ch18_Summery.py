----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'CSV — Reading with csv.reader
//////////////////////////////////////////////////////////////////////
What it is:
    A CSV file stores tabular data as plain text — each line is a row, and commas separate the cells within that row.
    Pythons csv module provides a reader object that handles the parsing correctly,
    including edge cases like values that contain commas wrapped in quotes.

Why it matters:
    You cant reliably parse CSV with split(',') because values can contain commas and other special characters —
    the csv module handles all of that for you automatically.

Functions/attributes at a glance:

csv.reader(file_obj) — wraps an open file object and returns an iterable reader

.line_num — integer attribute on the reader tracking the current line number (starts at 1)

list(reader) — converts the reader to a list of lists for random access

Example:
import csv

# Load entire file into memory as a list of lists
with open('example.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

data[0][0]    # first row, first cell
data[0][1]    # first row, second cell
data[1][1]    # second row, second cell

# Memory-efficient iteration
with open('example.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue   # skip header row
        print(row)

Gotcha:
    A reader object can only be iterated once —
    if you need to loop through it again, you must reopen the file and create a new reader object.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'CSV — Writing with csv.writer
//////////////////////////////////////////////////////////////////////
What it is:
    csv.writer takes an open file and lets you write rows to it one at a time using .writerow(),
    passing a list of values. It automatically handles escaping — if a value contains a comma, it wraps it in double quotes.

Why it matters:
    Lets your program export structured data to a format any spreadsheet app or other tool
    can open without you manually handling formatting edge cases.

Functions/methods at a glance:

csv.writer(file_obj) — creates a writer object from an open file

.writerow(list) — writes one row to the CSV; returns the number of characters written

Example:
import csv

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])             # header
    writer.writerow(['Alice', 30, 'San Francisco'])
    writer.writerow(['Hello, world!', 42, 'New York'])   # comma auto-escaped

Gotcha:
    On Windows, you must pass newline='' to open() when writing CSV —
    forgetting it causes every row to be double-spaced because Windows adds an extra newline.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'CSV — Custom Delimiter and Line Terminator
//////////////////////////////////////////////////////////////////////
What it is:
    By default a CSV uses commas between cells and a single newline at the end of each row.
    You can change both by passing delimiter and lineterminator keyword arguments to csv.writer().
    Tab-separated files (.tsv) are a common variation.

Why it matters:
    Some tools or data sources use tab or pipe (|) separation instead of commas —
    this lets you produce or consume those formats with the same csv module.

Example:
import csv

with open('output.tsv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator='\n\n')
    writer.writerow(['spam', 'eggs', 'bacon'])
    writer.writerow([1, 2, 3])
# produces tab-separated rows with a blank line between each

Gotcha:
    Changing lineterminator affects every row — '\n\n' double-spaces all rows, not just some of them.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'CSV — DictReader and DictWriter for Header Rows
//////////////////////////////////////////////////////////////////////
What it is:
    Instead of working with rows as plain lists,
    DictReader and DictWriter use the first row of the CSV as column headers
    and represent each subsequent row as a dictionary keyed by those headers. This makes your code self-documenting —
    you reference row['Fruit'] instead of row[1].

Why it matters:
    Most real CSV files have headers — using DictReader removes the need to manually skip or track the first row,
    and using DictWriter lets you write rows in any key order without worrying about column position.

Functions/methods at a glance:

csv.DictReader(file_obj) — reads rows as dicts using the first row as keys

csv.DictReader(file_obj, ['col1', 'col2']) — manually supplies header names for files without them

csv.DictWriter(file_obj, fieldnames) — writes dicts as rows; column order follows fieldnames

.writeheader() — writes the header row to the file (call once before writerow)

.writerow(dict) — writes one row; missing keys become empty cells, key order doesnt matter

Example:
import csv

# Reading
with open('data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Timestamp'], row['Fruit'], row['Quantity'])

# Writing
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'Pet', 'Phone'])
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
    writer.writerow({'Name': 'Bob', 'Phone': '555-9999'})  # missing 'Pet' → blank cell

Gotcha:
    If you use DictReader on a file without headers and dont supply your own header list,
    it will treat the first data row as the keys — your actual data starts at row 2 and row 1 is silently consumed as column names.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'JSON — Reading and Writing with json.loads() and json.dumps()
//////////////////////////////////////////////////////////////////////
What it is:
    JSON is a text format for storing structured data — dictionaries, lists, strings, numbers, booleans, and null values —
    in a way any programming language can read.
    Pythons json module converts between JSON strings and native Python data structures in both directions.

Why it matters:
    JSON is the standard format for web APIs and config files —
    knowing how to read and write it is essential for any program that communicates with external services or saves structured data to disk.

JSON ↔ Python type mapping:

JSON            Python
{} object       dict
[] array        list
"string"        str
123 / 1.5       int / float
true / false    True / False
null            None

Functions at a glance:

json.loads(string) — parses a JSON string and returns a Python dict/list/value

json.dumps(data) — converts a Python dict/list to a JSON-formatted string

json.dumps(data, indent=2) — same but formatted with indentation for readability

Example:
import json

# String → Python (reading)
json_str = '{"name": "Alice", "age": 30, "car": null, "active": true}'
data = json.loads(json_str)
print(data['name'])     # 'Alice'
print(data['car'])      # None
print(data['active'])   # True

# Python → String (writing)
python_data = {'name': 'Alice', 'age': 30, 'car': None, 'active': True}
json.dumps(python_data)              # compact single-line string
json.dumps(python_data, indent=2)    # readable indented output

# Read/write JSON file
with open('data.json', 'w') as f:
    f.write(json.dumps(python_data, indent=2))

with open('data.json') as f:
    loaded = json.loads(f.read())

Gotcha:
    json.dumps() only works with basic Python types —
    passing a datetime object, a set, or any custom class will raise a TypeError. Convert to strings or lists first.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'XML — Reading with xml.etree.ElementTree
//////////////////////////////////////////////////////////////////////
What it is:
    XML stores data as a tree of nested tags called elements.
    Pythons xml.etree.ElementTree module parses XML into a tree of Element objects.
    You navigate it by indexing children (root[0]), reading .tag and .text attributes, or iterating with .iter().

Why it matters:
    A lot of legacy software, enterprise data exports, Microsoft file formats (.docx, .xlsx),
    and RSS/Atom feeds use XML — being able to parse it lets your program work with these data sources.

Key attributes and methods:

ET.fromstring(xml_string) — parses an XML string and returns the root Element

ET.parse('file.xml').getroot() — loads XML from a file and returns the root Element

element.tag — the elements tag name as a string (e.g. 'name')

element.text — the text content between opening and closing tags (or None for empty/self-closing tags)

list(element) — returns a list of immediate child Elements

element[n] — access the nth child element by index

element.iter() — iterate over all descendants recursively

element.iter('tag') — iterate over only descendants with a matching tag name

Example:
import xml.etree.ElementTree as ET

xml_string = """<person>
    <name>Alice Doe</name>
    <age>30</age>
    <address>
        <city>San Francisco</city>
    </address>
</person>"""

root = ET.fromstring(xml_string)

root.tag            # 'person'
root[0].tag         # 'name'
root[0].text        # 'Alice Doe'
root[1].text        # '30'
root[2][0].text     # 'San Francisco'

# Iterate all children
for child in root:
    print(child.tag, '--', child.text)

# Iterate all descendants recursively
for elem in root.iter():
    print(elem.tag, '--', elem.text)

# Filter by tag
for elem in root.iter('city'):
    print(elem.text)    # 'San Francisco'

# Load from a file instead
tree = ET.parse('data.xml')
root = tree.getroot()

Gotcha:
    Self-closing tags like <car/> have None for .text — checking their value without a None guard will not behave how you expect.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'XML — Writing with xml.etree.ElementTree
//////////////////////////////////////////////////////////////////////
What it is:
    You build XML documents from scratch by creating an Element as the root,
    then attaching SubElement objects to it. You set text content via .text and XML attributes via .set().
    When done, ET.tostring() converts the whole tree to bytes, which you decode to a string.

Why it matters:
    Lets your program produce XML output for tools, APIs, or file formats that require it —
    without manually constructing tag strings by hand.

Functions/methods at a glance:

ET.Element('tag') — creates a root element

ET.SubElement(parent, 'tag') — creates a child element under a parent

element.text = 'value' — sets the text content between the tags

element.set('attr', 'value') — sets an XML attribute on the tag

ET.tostring(element, encoding='utf-8').decode('utf-8') — returns the full XML as a string

Example:
import xml.etree.ElementTree as ET

person = ET.Element('person')

name = ET.SubElement(person, 'name')
name.text = 'Alice Doe'

age = ET.SubElement(person, 'age')
age.text = '30'          # all XML text must be a string

address = ET.SubElement(person, 'address')
city = ET.SubElement(address, 'city')
city.text = 'San Francisco'

# Add an XML attribute
car = ET.SubElement(person, 'car')
car.set('xsi:nil', 'true')

# Convert to string and write to file
xml_output = ET.tostring(person, encoding='utf-8').decode('utf-8')
with open('output.xml', 'w') as f:
    f.write(xml_output)

Gotcha:
    ET.tostring() returns bytes, not a string —
    you must call .decode('utf-8') on it before writing to a text file or working with it as a string.
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'Format Comparison at a Glance
//////////////////////////////////////////////////////////////////////
Feature             CSV             JSON                            XML

Best for	Flat tabular data, 	 Nested structured data, 	     Legacy systems,
            spreadsheet rows          APIs                       document formats

Python              csv             json                            xml.etree.ElementTree
module

Human               Yes             Yes                             Yes (verbose)
readable

Supports            No              Yes                             Yes
nesting

Data                Strings only    str, int, float,                Strings only (by default)
types                               bool, list, dict,None

File extension      .csv            .json                           .xml
----------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
----------------------------------------------------------------------
'Summary:
//////////////////////////////////////////////////////////////////////
CSV: open file → csv.reader() or csv.DictReader() to read; csv.writer() or csv.DictWriter() to write; always pass newline='' on Windows when writing

DictReader/DictWriter use the first row as column headers — cleaner than managing list indexes manually

JSON: json.loads(string) → Python dict/list; json.dumps(data) → JSON string; use indent=2 for readable output; only basic Python types are supported

XML reading: ET.fromstring() or ET.parse() → root Element → navigate with [n], .tag, .text, .iter()

XML writing: ET.Element() → ET.SubElement() → .text / .set() → ET.tostring().decode()

All XML text values are strings — no automatic type conversion like JSON provides

For small projects where XML is inconvenient, xmltodict (third-party) can convert XML directly to a Python dict














