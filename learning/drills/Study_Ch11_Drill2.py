'''
Drill 2
Write a program that uses os.walk() to go through your entire python_portfolio folder and:

Count the total number of .py files across all subfolders
Print the name of each file and which subfolder it's in
Print the total count at the end
'''

from pathlib import Path
import os

home_path = Path.home()
walk_dir = home_path / 'Documents' / 'python_portfolio'
amount = 0
for filepath, subfolder,files in os.walk(walk_dir):


    for f in goop.glob('*.py'):
        amount +=1


    print (amount)






















