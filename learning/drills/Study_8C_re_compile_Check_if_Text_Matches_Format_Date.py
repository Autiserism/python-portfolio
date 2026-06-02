'''
Write a program that uses regex to find all dates in a string in the format MM/DD/YYYY and prints them as a list.
Test it with:
text = "Important dates: 01/15/2023, 12/31/1999, and 7/4/1776. Invalid: 13/45/2023 and 1/1/23."
Expected output: ['01/15/2023', '12/31/1999']
Note — valid months are 01-12, valid days are 01-31, valid years are 4 digits.
7/4/1776 has single digit month/day so it won't match, and 13/45/2023 has invalid month/day.'''


import re

text = "Important dates: 01/15/2023, 12/31/1999, and 7/4/1776. Invalid: 13/45/2023 and 1/1/23."

proper_date = re.compile(r'(?:0[1-9]|1[0-2])/(?:0[1-9]|[12][0-9]|3[01])/\d{4}')
date = proper_date.findall(text)
print(date)


'''
proper_date = re.compile(r'[0-1][0-9]/[0-3][0-9]/\d{4}') allows 19/39/2026 as a valid date

proper_date = re.compile(r'(?:0[1-9]|1[0-2])/[0-3][0-9]/\d{4}')
(?:...) means "group this but don't capture it" so findall() returns the full match instead.

The day 39 issue:
[0-3][0-9] allows 00-39 which isn't fully valid. The precise fix:
python(?:0[1-9]|[12][0-9]|3[01])

0[1-9] → 01-09
[12][0-9] → 10-29
3[01] → 30-31

This is getting into advanced regex territory.
For most real programs you'd validate dates with Python's datetime module rather than regex alone —
regex can check the format but not whether a date is actually valid. Worth knowing that limitation.'''
