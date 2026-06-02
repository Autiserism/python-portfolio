'''
Drill 2
Write a program that:

Creates a folder called test_files in your home directory
Creates three text files inside it — file1.txt, file2.txt, file3.txt — each with different content written to them
Reads each file back and prints the contents
Uses glob() to find all .txt files in the folder and prints their names
'''

from pathlib import Path
import os

save_path = Path.home()
folder = save_path / 'test_files'
os.makedirs (folder, exist_ok=True)

file1 = folder / 'file1.txt'
file2 = folder / 'file2.txt'
file3 = folder / 'file3.txt'

file1.write_text('file one')
file2.write_text('file two')
file3.write_text('file three')

print(file1.read_text())
print(file2.read_text())
print(file3.read_text())

for file in folder.glob('*.txt'):
    print(file.name)












