    W3P3 - Log Analyzer Pattern Prep
------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Your project: Parse log files, extract errors/warnings, count occurrences, find patterns.

Session: Log Parsing Patterns

Round 1 - Basic Log Format
Typical log entry:
[2024-01-15 14:23:45] ERROR: Database connection failed
[2024-01-15 14:23:46] INFO: Retrying connection
[2024-01-15 14:23:47] WARNING: High memory usage detected
Question: Write a pattern to match the timestamp [2024-01-15 14:23:45]

First pattern (commented) was close but has typos:
r'\[\d{4}-\d{2}-d{2}\s\d+:d+:\d+\]'
#                 ^      ^  missing backslashes
Second pattern is too broad:
r'^\[.+\]$'
# Problems:
# - .+ matches ANYTHING (not specific to timestamps)
# - ^ and $ mean ENTIRE line is just brackets
# - Would match "[hello world]" or "[xyz]"
Correct pattern:
pattern = re.compile(r'\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\]')
Breakdown:

\[ - literal [
\d{4}-\d{2}-\d{2} - date (YYYY-MM-DD)
\s - space
\d{2}:\d{2}:\d{2} - time (HH:MM:SS)
\] - literal ]

Test:
text = "[2024-01-15 14:23:45] ERROR: Database connection failed"
pattern.findall(text)
# ['[2024-01-15 14:23:45]']

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 2 - Extracting Timestamp Components
Question: Use groups to extract year, month, day, hour, minute, second separately.

pattern = re.compile(r'\[(\d{4})-(\d{2})-(\d{2})\s(\d{2}):(\d{2}):(\d{2})\]')

text = "[2024-01-15 14:23:45] ERROR: Database connection failed"
match = pattern.search(text)

print(match.group(0))  # '[2024-01-15 14:23:45]' (full match)
print(match.group(1))  # '2024' (year)
print(match.group(2))  # '01' (month)
print(match.group(3))  # '15' (day)
print(match.group(4))  # '14' (hour)
print(match.group(5))  # '23' (minute)
print(match.group(6))  # '45' (second)
Or unpack all at once:
year, month, day, hour, minute, second = match.groups()

Pattern: Each () creates a capturing group for extraction.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 3 - Log Level Extraction

Question: Extract the log level (ERROR, WARNING, INFO, DEBUG).
text = "[2024-01-15 14:23:45] ERROR: Database connection failed"
Write pattern to capture just "ERROR".

pattern = re.compile(r'[A-Z]+:')

Close! But issues:

Includes the colon: matches "ERROR:" not "ERROR"
Too broad: would match "HELLO:" or "ANYTHING:"

Better - specific log levels:

pattern = re.compile(r'(ERROR|WARNING|INFO|DEBUG)')

Or if you want just uppercase before colon:
pattern = re.compile(r'([A-Z]+):')
# Captures group without colon
Test:
text = "[2024-01-15 14:23:45] ERROR: Database connection failed"

# Option 1: Specific levels
pattern1 = re.compile(r'(ERROR|WARNING|INFO|DEBUG)')
pattern1.search(text).group()  # 'ERROR'

# Option 2: Any uppercase before colon
pattern2 = re.compile(r'([A-Z]+):')
pattern2.search(text).group(1)  # 'ERROR' (group 1, without colon)

For W3P3, use Option 1 - explicit log levels are safer.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 4 - Complete Log Entry Pattern
Question: Capture timestamp, log level, and message in one pattern.
 text = "[2024-01-15 14:23:45] ERROR: Database connection failed"
Want:

Group 1: Timestamp
Group 2: Log level
Group 3: Message

Your pattern:
  r'(\[.+\])\s(ERROR|WARNING|INFO|DEBUG):\s([\w\s]+)'
Issues:

.+ in timestamp too broad (matches any characters)
[\w\s]+ in message wont capture punctuation

Better:
 pattern = re.compile(r'(\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\])\s(ERROR|WARNING|INFO|DEBUG):\s(.+)')
Breakdown:

(\[...\]) - specific timestamp pattern
\s - space
(ERROR|WARNING|INFO|DEBUG) - log level ✓ (yours was perfect!)
:\s - colon + space
(.+) - message (everything remaining)

Test:
 text = "[2024-01-15 14:23:45] ERROR: Database connection failed"
match = pattern.search(text)

print(match.group(1))  # '[2024-01-15 14:23:45]'
print(match.group(2))  # 'ERROR'
print(match.group(3))  # 'Database connection failed'

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 5 - Filtering by Log Level
Scenario: Find all ERROR entries in a log file.
logs = """
[2024-01-15 14:23:45] ERROR: Database connection failed
[2024-01-15 14:23:46] INFO: Retrying connection
[2024-01-15 14:23:47] ERROR: Timeout occurred
[2024-01-15 14:23:48] WARNING: High memory usage
"""
Question: Write pattern with findall() to get all ERROR messages only.

Two approaches:
Option A - Get full ERROR lines:

 pattern = re.compile(r'\[.+\]\sERROR:\s.+')
errors = pattern.findall(logs)
# ['[2024-01-15 14:23:45] ERROR: Database connection failed',
#  '[2024-01-15 14:23:47] ERROR: Timeout occurred']

Option B - Get just ERROR messages:

 pattern = re.compile(r'\[.+\]\sERROR:\s(.+)')
messages = pattern.findall(logs)
# ['Database connection failed', 'Timeout occurred']
Key difference:

No capturing groups = findall() returns full matches
One capturing group = findall() returns just the group

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 6 - Counting Errors
Question: How would you count total ERROR entries?

  pattern = re.compile(r'\[.+\]\sERROR:\s(.+)')
messages = pattern.findall(logs)
amount = len(messages)

Or one-liner:
  error_count = len(re.findall(r'\[.+\]\sERROR:\s.+', logs))

Pattern: len(findall()) counts occurrences

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 7 - Extracting IP Addresses from Logs
Log with IPs:
  logs = """
[2024-01-15 14:23:45] ERROR: Connection from 192.168.1.100 failed
[2024-01-15 14:23:46] WARNING: Suspicious activity from 10.0.0.50
"""
Question: Write pattern to extract IP addresses.
Format: XXX.XXX.XXX.XXX (each part 1-3 digits)

pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

logs = """
[2024-01-15 14:23:45] ERROR: Connection from 192.168.1.100 failed
[2024-01-15 14:23:46] WARNING: Suspicious activity from 10.0.0.50
"""

ips = pattern.findall(logs)
print(ips)
# ['192.168.1.100', '10.0.0.50']
Pattern breakdown:

\d{1,3} - 1 to 3 digits
\. - literal dot (escaped)
Repeat 4 times

Note: This matches IP format but doesnt validate ranges (0-255). For logs, this is fine!

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

    Round 8 - Filtering Logs by Time Range
Scenario: Find logs between 14:23:45 and 14:23:47.
  logs = """
[2024-01-15 14:23:45] ERROR: Database connection failed
[2024-01-15 14:23:46] INFO: Retrying connection
[2024-01-15 14:23:47] ERROR: Timeout occurred
[2024-01-15 14:23:48] WARNING: High memory usage
"""
Question: How would you approach this?
A. Regex only
B. Regex + Python logic

Answer: B. regex to take the logs break it into groups then sorting the groups with a logic

Approach:
pythonimport re

# Extract timestamp and full entry
pattern = re.compile(r'(\[\d{4}-\d{2}-\d{2}\s(\d{2}:\d{2}:\d{2})\])(.+)')

results = []
for line in logs.strip().split('\n'):
    match = pattern.search(line)
    if match:
        full_timestamp = match.group(1)
        time_only = match.group(2)  # HH:MM:SS
        full_entry = match.group(3)

        # Filter by time range
        if '14:23:45' <= time_only <= '14:23:47':
            results.append(line)

print(results)
# ['[2024-01-15 14:23:45] ERROR: Database connection failed',
#  '[2024-01-15 14:23:46] INFO: Retrying connection',
#  '[2024-01-15 14:23:47] ERROR: Timeout occurred']
Pattern:

Regex captures components
Python string comparison filters (<= works on time strings!)
Collect matching entries

For dates, use datetime module for proper comparison.

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

Round 9 - Multi-line Log Entries
Problem: Some errors span multiple lines.
logs = """
[2024-01-15 14:23:45] ERROR: Database connection failed
    Traceback:
        at line 42
[2024-01-15 14:23:46] INFO: Connection restored
"""
Question: How would you match the complete ERROR entry (including traceback)?

pattern = re.compile(r'(\[.+\])\s(ERROR):\s([\w\s]+:)\n([\w\s]+)')

Good attempt! But issues:

Only captures 2 lines (error + one traceback line)
[\w\s]+ wont match numbers/punctuation in "at line 42"
Real tracebacks could be many lines

Better approach - match until next log entry:
python# Match ERROR and everything until next timestamp
pattern = re.compile(r'\[.+?\]\sERROR:.*?(?=\n\[|\Z)', re.DOTALL)
Pattern breakdown:

\[.+?\] - timestamp (non-greedy)
\sERROR: - log level
.*? - everything (non-greedy)
(?=\n\[|\Z) - lookahead: stop at next [ or end of string
re.DOTALL - makes . match newlines

Test:
pythonlogs = """
[2024-01-15 14:23:45] ERROR: Database connection failed
    Traceback:
        at line 42
[2024-01-15 14:23:46] INFO: Connection restored
"""

pattern = re.compile(r'\[.+?\]\sERROR:.*?(?=\n\[|\Z)', re.DOTALL)
errors = pattern.findall(logs)

print(errors[0])
# [2024-01-15 14:23:45] ERROR: Database connection failed
#     Traceback:
#         at line 42
Key concepts:

.*? with re.DOTALL matches across lines
(?=...) lookahead stops at next entry without consuming it

------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

W3P3 Pattern Cheat Sheet
python# Timestamp extraction
r'\[(\d{4}-\d{2}-\d{2})\s(\d{2}:\d{2}:\d{2})\]'

# Log level extraction
r'(ERROR|WARNING|INFO|DEBUG)'

# Complete log entry (single line)
r'(\[.+?\])\s(ERROR|WARNING|INFO|DEBUG):\s(.+)'

# Filter specific log level
r'\[.+?\]\sERROR:\s.+'

# Extract just the message
r'\[.+?\]\sERROR:\s(.+)'

# Count errors
len(re.findall(r'\[.+?\]\sERROR:\s.+', logs))

# IP addresses
r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# Multi-line entries
r'\[.+?\]\sERROR:.*?(?=\n\[|\Z)'  # with re.DOTALL

# Filter by time
# 1. Extract with: r'(\d{2}:\d{2}:\d{2})'
# 2. Compare with: if '14:23:45' <= time <= '14:23:47'

Key Patterns for W3P3
✓ Timestamp parsing with groups
✓ Log level filtering with alternation |
✓ Counting with len(findall())
✓ IP address extraction
✓ Time range filtering (regex + logic)
✓ Multi-line matching with re.DOTALL and lookahead



------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------

one giant regex with groups:

pattern = re.compile(r'\[(.+?)\]\s(ERROR|WARNING|INFO|DEBUG|CRITICAL):\s(.+)')
for match in pattern.finditer(logs):
    timestamp = match.group(1)
    level = match.group(2)
    message = match.group(3)

finditer() is new — like findall() but returns match objects instead of strings, so you can use .group() on each one.
The tradeoff:

One pattern = less code, but harder to read
Three patterns = more code, but each does one clear job



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
