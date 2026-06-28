'''
M1P8 — JSON API Fetcher (Ch 18)
Connect to a free public API (weather and exchange rates are good options).
User inputs a query (city name, currency pair etc.),
program fetches the data, parses the JSON response,
and displays it cleanly in the terminal.
Error handling for failed requests or bad input. Optionally saves results to a file.
'''
from pathlib import Path
import urllib.request, urllib.error
import json,os,datetime,csv
now = datetime.datetime.now()
time_date = now.strftime("%m-%d-%Y")

file_path = Path.home() / 'projects'/ 'CH18ATBS'
os.chdir(file_path)
save_parse = file_path / 'weather_API.json'
file_name = 'weather_API.csv'





def city_loc(name):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={name}&count=1&language=en&format=json"
    try:
        response = urllib.request.urlopen(geo_url)
    except urllib.error.URLError:
        print('Network error — check your connection')
        return None
    loc_data = json.loads(response.read().decode('utf-8'))
    return loc_data

def pick_a_city():
    while True:
        try:
            pick_city = input("enter city name or 'Quit' to exit:\n").strip().lower()
            if pick_city == 'quit':
                print('exiting')
                return None
            location_data = city_loc(pick_city)
            city_name = location_data["results"][0]['name']
            contry_name = location_data["results"][0]["country"]
            choice = input(f"Type 'yes' to confirm that\n{pick_city} located in {contry_name} is correct\n(if its not hit enter to try again)\n")
            if choice == 'yes':
                break
            else:
                continue
        except KeyError:
            print('wasnt able to find a city of that name try again')
            continue
    return location_data

def weather_url(latitude,longitude):
    if not latitude or not longitude:
        return
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
    response = urllib.request.urlopen(url)
    weather_data = json.loads(response.read().decode('utf-8'))
    return weather_data

def save_parses(location_data,weather_data):
    combined = {
        'location': location_data["results"][0],
        'weather': weather_data["current_weather"]
    }
    save_parse.write_text(json.dumps(combined, indent=4))
    print(f'Saved to {file_path.name}')

def write_to_csv(location_data,weather_data):
    cw = weather_data["current_weather"]
    ld = location_data["results"][0]
    fieldnames = ['city', 'country', 'time', 'temperature', 'windspeed']
    with open(file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            'city' : ld['name'],
            'country' : ld["country"],
            'time': cw['time'],
            'temperature': cw['temperature'],
            'windspeed': cw['windspeed']
        })
    print('CSV written.')

def print_report():
    print(f"{'*'*10}weather report {'*'*10}")
    with open(file_name, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print('City',row['city'],'\nCountry',row['country'],'\nTime',row['time'],'\nTemperature',row['temperature'],'\nWindspeed',row['windspeed'])

menu_options = ['Check weather','Quit']

def main_menu():
    while True:
        print('*'*5,'Main menu','*'*5)
        for i, item in enumerate(menu_options,1):
            print(i,item)
        choice = input('\nEnter a number: ').strip()
        if choice == '1':
            location_data = pick_a_city()
            if not location_data:
                print('')
                continue
            lat = location_data["results"][0]["latitude"]
            long = location_data["results"][0]["longitude"]
            weather_data = weather_url(lat,long)
            save_parses(location_data,weather_data)
            write_to_csv(location_data,weather_data)
            print_report()

        elif choice == '2':
            print('Goodbye.')
            break
        else:
            print('Invalid choice — enter 1 or 2.')

main_menu()










