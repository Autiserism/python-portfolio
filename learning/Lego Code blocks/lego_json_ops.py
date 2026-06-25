# ======================================================================
# LEGO CODE BLOCKS — JSON OPS
# lego_json_ops.py
# ======================================================================
# PURPOSE : Reusable JSON load / save / read / manipulate patterns
# USE     : Open in Mu, find your block, copy what you need
# CRASH   : >'name'< is intentionally invalid — forces you to rename
#           before the program will run
# FILL-IN : string_var1, dict_var1, list_var1 etc. = rename to match
#           your data + follow the #<<<< comment on that line
# ======================================================================


# ======================================================================
# REQUIRED IMPORTS — paste these at the top of your project file
# ======================================================================

from pathlib import Path
import json, os


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
# BLOCK JSON-1 — Single JSON File: Load on Start / Save on Quit
# ======================================================================
# DESCRIPTION : Loads one .json file into a variable at program start.
#               If the file doesn't exist yet, starts with an empty dict.
#               save_quit() writes everything back to disk and confirms.
#               Use this for any program that needs one persistent data file
#               (expense tracker, contact book, to-do list, etc.)
# FEEDS       : any dict or list you want to persist between runs
# RETURNS     : dict_var1 holds the loaded data on startup;
#               save_quit() writes it back when you're done
# TAGS        : json, load, save, persist, single file, startup
# ======================================================================

file_path = data_dir / >'filename.json'<  #<<<< set your .json filename here

if file_path.exists() and file_path.is_file():
    dict_var1 = json.loads(file_path.read_text())   #<<<< rename dict_var1 to match your data
else:
    dict_var1 = {}   #<<<< swap {} for [] if your root data is a list

def save_quit():
    file_path.write_text(json.dumps(dict_var1, indent=4))   #<<<< match variable name above
    print('Saved successfully.')


# ======================================================================
# BLOCK JSON-2 — Multiple JSON Files: Load Each Into Its Own Variable
# ======================================================================
# DESCRIPTION : Loads several .json files from the same project folder
#               into separate named variables. The helper functions
#               load_json() and save_json() are reusable across all of them.
#               Pattern taken from M1P6 Text Adventure (rooms, monsters,
#               items, etc.) — works for any project splitting data across
#               multiple files.
# FEEDS       : .json filenames as strings; files must be in data_dir
#               (run the PATH SETUP block above first)
# RETURNS     : each var holds the parsed contents of its file;
#               save_json() writes one file back after you modify it
# TAGS        : json, multiple files, load, save, split data, helpers
# ======================================================================

def load_json(path):
    path = Path(path)
    if path.exists():
        return json.loads(path.read_text())
    return {}   #<<<< swap {} for [] if that file holds a list

def save_json(path, data):
    path = Path(path)
    path.write_text(json.dumps(data, indent=4))
    print(f'{path.name} saved.')

# — Declare filenames — rename these to match your actual files
json_file1 = >'file1.json'<   #<<<< rename
json_file2 = >'file2.json'<   #<<<< rename
json_file3 = >'file3.json'<   #<<<< rename

# — Load each one into its own variable
var1 = load_json(json_file1)   #<<<< rename var1 to describe what it holds
var2 = load_json(json_file2)   #<<<< rename var2
var3 = load_json(json_file3)   #<<<< rename var3

# — Save one file back after modifying its variable
save_json(json_file1, var1)   #<<<< match file name and variable name

# — Bulk load pattern: loop when you have many files
all_files = [json_file1, json_file2, json_file3]   #<<<< add filenames as needed
all_vars  = [load_json(f) for f in all_files]      # result: list of dicts/lists in same order


# ======================================================================
# BLOCK JSON-3 — Add or Update a Key in a Loaded JSON Dict
# ======================================================================
# DESCRIPTION : Adds a new entry or overwrites an existing one inside a
#               loaded JSON dict. Python doesn't care if the key already
#               exists — same syntax either way.
#               Changes are in memory only until you call save_quit() or
#               save_json().
# FEEDS       : dict_var1 (a loaded JSON dict already in memory),
#               string_var1 (the key name), and whatever value you're storing
# RETURNS     : dict_var1 updated in memory — call save when ready
# TAGS        : json, add, update, key, dict, nested
# ======================================================================

# — Add or update a flat key
dict_var1[string_var1] = string_var2   #<<<< string_var1=key name | string_var2=value

# — Add or update with a nested dict as the value
dict_var1[string_var1] = {             #<<<< string_var1=outer key name
    'field1': string_var2,             #<<<< rename field1/field2 to your actual sub-keys
    'field2': int_var1                 #<<<< int_var1=any numeric value
}

# — Add a new item to a list that lives inside a dict key
dict_var1[string_var1].append(string_var2)   #<<<< key must already hold a list

# — Remove a key entirely
dict_var1.pop(string_var1, None)   #<<<< None means no crash if key doesn't exist


# ======================================================================
# BLOCK JSON-4 — Safely Read Values from a JSON Dict (Flat and Nested)
# ======================================================================
# DESCRIPTION : Reads values out of a loaded JSON dict using .get() so
#               your program doesn't crash if a key is missing — it returns
#               a fallback value instead. Covers flat, one-level deep, and
#               two-levels deep access.
# FEEDS       : dict_var1 (a loaded JSON dict)
# RETURNS     : the value at that key, or the fallback if key not found
# TAGS        : json, read, get, nested, safe access, fallback
# ======================================================================

# — Flat: single key
value = dict_var1.get(string_var1, None)   #<<<< string_var1=key | None=fallback if missing

# — One level deep (dict inside a dict)
value = dict_var1.get(string_var1, {}).get(string_var2, None)
#                    ^outer key    ^fallback if outer missing  ^inner key

# — Two levels deep
value = (dict_var1
         .get(string_var1, {})
         .get(string_var2, {})
         .get(string_var3, None))   #<<<< chain as deep as your structure goes

# — Print all top-level keys and their values (flat dict)
for key, val in dict_var1.items():
    print(f'{key}: {val}')

# — Print all keys and values from a nested dict one level deep
for key, inner in dict_var1.items():
    if isinstance(inner, dict):
        for sub_key, sub_val in inner.items():
            print(f'  {key} → {sub_key}: {sub_val}')
    else:
        print(f'{key}: {inner}')

# — Check if a key exists before using it
if string_var1 in dict_var1:
    print(dict_var1[string_var1])


# ======================================================================
# BLOCK JSON-5 — Sort a List of Dicts by a Key (String / Number / Date)
# ======================================================================
# DESCRIPTION : Sorts a list of dicts by one chosen key. Works for
#               strings, numbers, or date strings. sorted() does not
#               modify the original list — it returns a new one.
#               Pattern from Stuff_to_add.txt notes + M1P4 task reminder.
# FEEDS       : list_var1 — a list of dicts (e.g. [{}, {}, {}] from JSON)
# RETURNS     : sorted_list — new sorted list; original list_var1 unchanged
# TAGS        : json, sort, list of dicts, lambda, date, sorted, strptime
# ======================================================================

import datetime

# — Sort by string or number key — ascending (A→Z or low→high)
sorted_list = sorted(list_var1, key=lambda x: x[string_var1])
#                               ^each dict    ^key to sort by

# — Sort descending (Z→A or high→low)
sorted_list = sorted(list_var1, key=lambda x: x[string_var1], reverse=True)

# — Sort by date string — format MM/DD/YYYY
sorted_list = sorted(
    list_var1,
    key=lambda x: datetime.datetime.strptime(x[string_var1], '%m/%d/%Y')
    #                                         ^the date key   ^match your date format
    # Common formats: '%m/%d/%Y' → 06/24/2026 | '%Y-%m-%d' → 2026-06-24
)

# — Print numbered results after sorting
for i, item in enumerate(sorted_list, 1):
    print(f"{i}. {item[string_var1]} — {item[string_var2]}")   #<<<< keys to display


# ======================================================================
# BLOCK JSON-6 — Fetch JSON from a Public URL and Save to File
# ======================================================================
# DESCRIPTION : Pulls JSON data from an API URL using the standard library
#               (no pip install needed). Parses the response, saves it to a
#               .json file, and lets you access any key from the response.
#               Good starting point for any API that returns plain JSON.
# FEEDS       : a URL string that returns JSON when you visit it in a browser
# RETURNS     : dict_var1 holds the parsed response; file saved to disk
# TAGS        : json, api, url, fetch, urllib, save, request
# ======================================================================

import urllib.request

url = 'https://your-api-url-here.com/endpoint'   #<<<< paste your URL here as a string

response  = urllib.request.urlopen(url)
dict_var1 = json.loads(response.read().decode('utf-8'))   #<<<< rename dict_var1

# — Save raw response to file
file_path.write_text(json.dumps(dict_var1, indent=4))
print(f'Saved to {file_path.name}')

# — Read a specific key from the response
value = dict_var1.get(string_var1, 'key not found')   #<<<< string_var1=key you want
print(value)

# — Example: Windsor weather (no API key needed)
# url = 'https://api.open-meteo.com/v1/forecast?latitude=42.3&longitude=-83.0&current_weather=true'
# dict_var1 = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
# print(dict_var1['current_weather'])
