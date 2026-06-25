# ======================================================================
# LEGO CODE BLOCKS — CSV OPS
# lego_csv_ops.py
# ======================================================================
# PURPOSE : Reusable CSV read / write / filter / process patterns
# USE     : Open in Mu, find your block, copy what you need
# CRASH   : >'name'< is intentionally invalid — forces you to rename
#           before the program will run
# FILL-IN : string_var1, dict_var1, list_var1 etc. = rename to match
#           your data + follow the #<<<< comment on that line
# ======================================================================
#
# THE "with open()" ANATOMY — read this once, reference as needed:
#
#   with open( PATH, MODE, newline='', encoding='utf-8' ) as f:
#              |     |     |           |
#              |     |     |           utf-8 handles most text files
#              |     |     ALWAYS include newline='' for CSV on Windows
#              |     |     (skipping it causes every row to double-space)
#              |     |
#              |     MODES:
#              |       'r'  → read only (file must exist)
#              |       'w'  → write — creates file, OVERWRITES if exists
#              |       'a'  → append — adds to end, creates if not exist
#              |       'r+' → read AND write (file must exist)
#              |
#              PATH  → a string or Path object pointing to the file
#
#   Everything inside the indented block has access to f (the file object).
#   The file closes automatically when the block ends — no f.close() needed.
#
# ======================================================================


# ======================================================================
# REQUIRED IMPORTS — paste these at the top of your project file
# ======================================================================

import csv, os
from pathlib import Path


# ======================================================================
# PATH / DIRECTORY SETUP
# ======================================================================
# DESCRIPTION : Creates a project folder and sets it as the working
#               directory. Required boilerplate for any project that
#               reads or writes files. One folder per project.
# FILL IN     : foldername — the folder inside ~/projects/ for this project
# ======================================================================

data_dir = Path.home() / 'projects' / >'foldername'<  #<<<< rename to your project folder
data_dir.mkdir(parents=True, exist_ok=True)
os.chdir(data_dir)


# ======================================================================
# BLOCK CSV-1 — Write a CSV File (Simple Rows, No Headers)
# ======================================================================
# DESCRIPTION : Creates a new CSV file and writes rows to it as plain
#               lists. Each list becomes one row. If the file already
#               exists it is overwritten — 'w' mode.
#               Use DictWriter (CSV-3) instead if you want named columns.
# FEEDS       : a list of lists — each inner list is one row of values
# RETURNS     : a CSV file written to disk
# TAGS        : csv, write, create, rows, writer, lists
# ======================================================================

rows_to_write = [                      #<<<< replace these with your actual rows
    ['Alice', 30, 'Windsor'],          # each inner list = one row
    ['Bob',   25, 'Toronto'],
    ['Carol', 35, 'Ottawa'],
]

with open(>'filename.csv'<, 'w', newline='') as f:   #<<<< rename the file
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])          #<<<< header row — rename columns
    for row in rows_to_write:
        writer.writerow(row)

print('CSV written.')


# ======================================================================
# BLOCK CSV-2 — Read a CSV File (Simple Rows as Lists)
# ======================================================================
# DESCRIPTION : Reads a CSV file row by row. Each row comes back as a
#               plain list — access cells by index (row[0], row[1], etc.).
#               reader.line_num tracks the current line number.
#               Use DictReader (CSV-4) instead if the file has a header row
#               and you want to access cells by column name.
# FEEDS       : an existing CSV file
# RETURNS     : prints or processes each row; use list(reader) to load all
# TAGS        : csv, read, rows, reader, list, index
# ======================================================================

with open(>'filename.csv'<, 'r', newline='') as f:   #<<<< rename the file
    reader = csv.reader(f)
    for row in reader:
        if reader.line_num == 1:
            continue   #<<<< remove this line if there's no header to skip
        print(row)     #<<<< replace with what you actually want to do with each row
        # row[0] → first column | row[1] → second column | etc.

# — Load entire file into memory as a list of lists (for random access)
with open(>'filename.csv'<, 'r', newline='') as f:   #<<<< rename the file
    reader = csv.reader(f)
    all_rows = list(reader)   # all_rows[0][0] → row 0, col 0

# NOTE: A reader can only be iterated ONCE per open() call.
#       If you need to loop it again, reopen the file.


# ======================================================================
# BLOCK CSV-3 — Write a CSV File with Column Headers (DictWriter)
# ======================================================================
# DESCRIPTION : Creates a CSV where each row is a dict keyed by column
#               names. DictWriter writes the header row for you.
#               Cleaner than CSV-1 when you have named columns — you write
#               row['Name'] instead of row[0].
# FEEDS       : a list of dicts — each dict is one row, keys = column names
# RETURNS     : a CSV file with a header row written to disk
# TAGS        : csv, write, headers, DictWriter, dict, columns
# ======================================================================

fieldnames = ['Name', 'Age', 'City']   #<<<< your column headers — must match dict keys below

rows_to_write = [
    {'Name': 'Alice', 'Age': 30,  'City': 'Windsor'},   #<<<< replace with your data
    {'Name': 'Bob',   'Age': 25,  'City': 'Toronto'},
    {'Name': 'Carol', 'Age': 35,  'City': 'Ottawa'},
]

with open(>'filename.csv'<, 'w', newline='') as f:   #<<<< rename the file
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()                              # writes the column name row
    for row in rows_to_write:
        writer.writerow(row)

print('CSV written.')


# ======================================================================
# BLOCK CSV-4 — Read a CSV File with Column Headers (DictReader)
# ======================================================================
# DESCRIPTION : Reads a CSV that has a header row. Each row comes back as
#               a dict — access cells by column name (row['Name']) instead
#               of index. DictReader uses the first row as keys automatically.
#               This is the most readable way to work with real-world CSV files.
# FEEDS       : an existing CSV file that has a header row
# RETURNS     : each row as a dict; access by column name
# TAGS        : csv, read, headers, DictReader, dict, column name
# ======================================================================

with open(>'filename.csv'<, 'r', newline='') as f:   #<<<< rename the file
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Age'], row['City'])   #<<<< use your actual column names

# — Load all rows into a list of dicts for later use
with open(>'filename.csv'<, 'r', newline='') as f:   #<<<< rename the file
    reader = csv.DictReader(f)
    all_rows = list(reader)   # all_rows[0]['Name'] → first row, Name column

# — Print formatted with rjust / ljust padding
with open(>'filename.csv'<, 'r', newline='') as f:   #<<<< rename the file
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'].ljust(15), row['Age'].rjust(5))   #<<<< your columns + widths


# ======================================================================
# BLOCK CSV-5 — Append a New Row to an Existing CSV
# ======================================================================
# DESCRIPTION : Opens an existing CSV in append mode and adds one new row
#               at the end without touching anything already in the file.
#               Works with both plain writer and DictWriter.
#               Use 'a' mode — 'w' would overwrite everything.
# FEEDS       : an existing CSV file and the new row data to add
# RETURNS     : one new row appended to the file
# TAGS        : csv, append, add row, write, 'a' mode
# ======================================================================

# — Append with DictWriter (has headers)
fieldnames = ['Name', 'Age', 'City']   #<<<< must match the existing file's columns

new_row = {'Name': 'Dave', 'Age': 28, 'City': 'London'}   #<<<< your new row data

with open(>'filename.csv'<, 'a', newline='') as f:   #<<<< rename the file
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(new_row)
print('Row appended.')

# — Append with plain writer (no headers)
new_row_list = ['Dave', 28, 'London']   #<<<< values in same column order as the file

with open(>'filename.csv'<, 'a', newline='') as f:   #<<<< rename the file
    writer = csv.writer(f)
    writer.writerow(new_row_list)
print('Row appended.')


# ======================================================================
# BLOCK CSV-6 — Read CSV, Filter Rows by Column Value
# ======================================================================
# DESCRIPTION : Reads a CSV and only processes rows where a specific column
#               matches a condition. Use this to pull matching records from a
#               larger file (e.g. all expenses in one category, all entries
#               above a threshold, etc.)
# FEEDS       : an existing CSV with headers; a value to filter by
# RETURNS     : prints or collects only the matching rows
# TAGS        : csv, filter, read, DictReader, match, condition, search
# ======================================================================

filter_value = string_var1   #<<<< the value you're searching for in that column

matched_rows = []

with open(>'filename.csv'<, 'r', newline='') as f:   #<<<< rename the file
    reader = csv.DictReader(f)
    for row in reader:
        if row['City'] == filter_value:              #<<<< 'City' = column to filter on
            matched_rows.append(row)

for row in matched_rows:
    print(row['Name'], row['Age'], row['City'])   #<<<< columns to display

# — Filter by numeric condition (convert first — CSV values are strings)
with open(>'filename.csv'<, 'r', newline='') as f:   #<<<< rename the file
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Age']) > 30:                     #<<<< 'Age' = numeric column | 30 = threshold
            print(row['Name'], row['Age'])


# ======================================================================
# BLOCK CSV-7 — Read a CSV, Process Rows, Write a New CSV
# ======================================================================
# DESCRIPTION : Full pipeline — reads an existing CSV, does something to
#               each row (add a column, transform a value, filter rows),
#               and writes the results to a new output file.
#               Pattern from Ch18 Drill 2: read student scores, calculate
#               averages, write results.
# FEEDS       : an existing CSV input file
# RETURNS     : a new CSV output file with the processed rows
# TAGS        : csv, read, process, write, pipeline, transform, new file
# ======================================================================

input_fieldnames  = ['Name', 'Score1', 'Score2', 'Score3']   #<<<< input file columns
output_fieldnames = ['Name', 'Average', 'Grade']              #<<<< output file columns

def process_row(row):
    '''Takes one input row dict, returns one output row dict.'''
    scores  = [int(row['Score1']), int(row['Score2']), int(row['Score3'])]  #<<<< your score cols
    average = round(sum(scores) / len(scores), 2)
    grade   = 'A' if average >= 90 else 'B' if average >= 80 else 'C' if average >= 70 else 'F'
    return {'Name': row['Name'], 'Average': average, 'Grade': grade}       #<<<< match output_fieldnames

# — Open input and output files together in one with block
with (open(>'input.csv'<,  'r', newline='') as infile,    #<<<< rename input file
      open(>'output.csv'<, 'w', newline='') as outfile):  #<<<< rename output file
    reader = csv.DictReader(infile,  fieldnames=input_fieldnames)
    writer = csv.DictWriter(outfile, fieldnames=output_fieldnames)
    writer.writeheader()
    next(reader)   # skip header row from input file (remove if no header)
    for row in reader:
        writer.writerow(process_row(row))

print('Done — output written.')
