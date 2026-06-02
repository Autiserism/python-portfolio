# Write your code here :-)
import re
from collections import Counter

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

def unique_messages(logs):
    """Extract all unique log messages"""
    pattern = re.compile(r'\[.+\]\s[A-Z]+:\s(.+)')
    result = pattern.findall(logs)
    return list(set(result))

def log_level_counts(logs):
    """Count occurrences of each log level"""
    pattern = re.compile(r'(ERROR|WARNING|INFO|DEBUG|CRITICAL)')
    result = pattern.findall(logs)
    return dict(Counter(result))

def timestamp_range(logs):
    """Get first and last timestamps"""
    pattern = re.compile(r'\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\]')
    result = pattern.findall(logs)
    return result[0], result[-1]

# Generate report
print("=" * 60)
print("LOG ANALYSIS REPORT")
print("=" * 60)

print("\nUnique Messages:")
messages = unique_messages(logs)
for i, msg in enumerate(messages, 1):
    print(f"  {i}. {msg}")

print("\n" + "-" * 60)
print("\nLog Level Distribution:")
counts = log_level_counts(logs)
for level, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {level:10} : {count:3} ({'█' * count})")

print("\n" + "-" * 60)
print("\nTime Range:")
start, end = timestamp_range(logs)
print(f"  From: {start}")
print(f"  To:   {end}")

print("\n" + "=" * 60)
