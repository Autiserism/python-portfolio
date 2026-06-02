'''
W3P3 — Log File Analyzer W3P3_log_analyzer.py
Generate a fake log file using logging with different levels.
Then use regex to search through it —
extract all error messages, count occurrences of each level, find all timestamps. Display a summary report.
'''
import re

logs = """
[2024-01-15 14:23:45] ERROR: Database connection failed
[2024-01-16 14:23:46] INFO: Connection restored
[2024-01-17 14:23:45] ERROR: Database connection failed
[2024-01-18 14:23:46] INFO: Retrying connection
[2024-01-19 14:23:47] ERROR: Timeout occurred
[2024-01-20 14:23:48] WARNING: High memory usage
[2024-02-15 14:23:45] ERROR: Database connection failed
[2024-02-15 14:23:46] INFO: Retrying connection
[2024-02-15 14:23:47] ERROR: Timeout occurred
[2024-02-15 14:23:48] WARNING: High memory usage
"""

def error_mesages(logs):
    pattern = re.compile(r'\[.+\]\s[A-Z]+:\s(.+)')
    result = pattern.findall(logs)
    result = set(result)
    return list(result)

def error_count(logs):
    errors = {}
    pattern = re.compile(r'(ERROR|WARNING|INFO|DEBUG|CRITICAL)')
    result = pattern.findall(logs)
    for word in result:
        errors.setdefault(word, 0)
        errors[word] += 1
    return errors

def timestamps(logs):
    date_range = []
    pattern = re.compile(r'\[.+\]')
    result = pattern.findall(logs)
    date_range.append(result[0])
    date_range.append(result[-1])
    return date_range

print("Summary report: \nUnique errors\n")
errorM = error_mesages(logs)
for e in errorM:
    print(e)
print('\nError counts')
errorC = error_count(logs)
print(errorC)
print('\nTime frame')
timeline = timestamps(logs)
print(f"{timeline[0]} to {timeline[1]}")



Alternative approaches (all work):
Using Counter (more Pythonic):
pythonfrom collections import Counter

def error_count(logs):
    pattern = re.compile(r'(ERROR|WARNING|INFO|DEBUG|CRITICAL)')
    result = pattern.findall(logs)
    return dict(Counter(result))
Using get():
pythonfor word in result:
    errors[word] = errors.get(word, 0) + 1




















