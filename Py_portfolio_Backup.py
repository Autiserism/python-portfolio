from pathlib import Path
import zipfile, os, datetime

now = datetime.datetime.now()
time_date = now.strftime("%m-%d-%Y")
print(time_date)

location   = Path.home() / 'projects'
walk_here  = Path.home() / 'Documents' / 'python_portfolio'
zip_path   = location / f'Python_Backups-{time_date}.zip'

backup_zip = zipfile.ZipFile(zip_path, 'w')
amount = 0

for folder_name, subfolders, filenames in os.walk(walk_here):
    folder_name = Path(folder_name)
    for filename in filenames:
        if filename.endswith(('.py', '.json','.csv','.txt','.xml','.pdf', '.yaml', '.yml','.db', '.sqlite', '.sqlite3','.md','.env', '.cfg', '.ini', '.toml',)):
            full_path = folder_name / filename
            arc_path  = full_path.relative_to(walk_here)  # strips everything before python_portfolio
            backup_zip.write(full_path, arcname=arc_path)
            amount += 1

backup_zip.close()
print("Total files added:", amount)

extract_zip = zipfile.ZipFile(zip_path)
print(extract_zip.namelist())
extract_zip.close()
print(f'backed up as = Python_Backups-{time_date}.zip')
e = input('>')
'''
filename.endswith((
    # code
    '.py',
    # data
    '.json', '.csv', '.txt', '.xml', '.yaml', '.yml',
    # database
    '.db', '.sqlite', '.sqlite3',
    # docs
    '.md', '.pdf',
    # environment
    '.env', '.cfg', '.ini', '.toml',
))
'''
