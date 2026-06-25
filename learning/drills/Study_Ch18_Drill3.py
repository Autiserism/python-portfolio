'''
Drill 3 — Final Chapter 18 drill
Write a program that fetches data from a public JSON API and saves the result to both a JSON file and a CSV file.
Use the Open Meteo weather API — no API key required:
https://api.open-meteo.com/v1/forecast?latitude=42.3&longitude=-83.0&current_weather=true
That's roughly Windsor's coordinates. Use urllib.request.urlopen() to fetch it:

import urllib.request
import json

url = 'your_url_here'
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode('utf-8'))
Parse the response, save the current weather data to a JSON file, and write the key fields to a CSV file.
'''
from pathlib import Path
import urllib.request
import json,os,datetime,csv
now = datetime.datetime.now()
time_date = now.strftime("%m-%d-%Y")

file_path = Path.home() / 'projects'/ 'CH18ATBS'
os.chdir(file_path)
save_parse = file_path / 'weather_API_test.json'

url = 'https://api.open-meteo.com/v1/forecast?latitude=42.3&longitude=-83.0&current_weather=true'
response = urllib.request.urlopen(url)
weather_data = json.loads(response.read().decode('utf-8'))

save_parse.write_text(json.dumps(weather_data, indent=4))
print(f'Saved to {file_path.name}')

print(weather_data)
cw = weather_data["current_weather"]
fieldnames = ['time', 'temperature', 'windspeed']

with open('weather_API_test.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        'time': cw['time'],
        'temperature': cw['temperature'],
        'windspeed': cw['windspeed']
    })

print('CSV written.')

print(f"{'*'*10}weather report {'*'*10}")

with open('weather_API_test.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print('time',row['time'],'temperature'.ljust(9,'='),row['temperature'],'windspeed',row['windspeed'])





'''
"current_weather": {
    "time": "2026-06-24T16:15",
    "interval": 900,
    "temperature": 24.7,
    "windspeed": 7.1,
    "winddirection": 210,
    "is_day": 1,
    "weathercode": 0
'current_weather_units': {'time': 'iso8601',
    'interval': 'seconds',
    'temperature': '°C',
    'windspeed': 'km/h',
    'winddirection': '°',
    'is_day': '',
    'weathercode': 'wmo code'}
'''









