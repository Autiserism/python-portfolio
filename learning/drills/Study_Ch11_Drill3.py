'''
Drill 3
Write a program that:

Creates a zip file called portfolio_backup.zip in your Documents folder
Adds all .py files from your python_portfolio folder and subfolders to the zip
Prints how many files were added
Then opens the zip and prints the list of all files inside it using namelist()
'''

from pathlib import Path
import zipfile, os

file_path = Path.home()
location = file_path / 'Documents'
location = Path(location)
walk_here = file_path / 'Documents' / 'python_portfolio'

zip_filename = 'Python_Backups.zip'
zip_path = location / zip_filename
backup_zip = zipfile.ZipFile(zip_path, 'w')


amount = 0
for folder_name, subfolders, filenames in os.walk(walk_here):
    folder_name = Path(folder_name)
    for filename in filenames:
        if filename.endswith('.py'):
            backup_zip.write(folder_name / filename)
            amount +=1
backup_zip.close()
print ("total files added: ", amount)

extract_zip = zipfile.ZipFile(zip_path)
extract_zip.namelist()
print(extract_zip.namelist())
extract_zip.close()

