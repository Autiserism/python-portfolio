'''
M1P1 — Unit Converter
Convert between length, weight, and temperature.
User picks a category, picks the conversion type,
enters a value, gets the result.
Loops so they can keep converting without restarting.
Input validation throughout.
Clean formatted output.
'''

"""Length"""

length_units = [ 'inch', 'feet', 'yard', 'mile', 'millimeter', 'centimeter', 'meter', 'kilometer']#, "Quit"

def length_menu():
    """select the starting unit"""
    while True:
        print('Enter the number to the left of the mesurment to select it or 9 to Exit')
        for i, e in enumerate(length_units, 1):
            print (i,e)
        try:
            index = int(input('\nWhat is the starting unit?: ')) -1
            if index == 8: # because of the -1 index
                break
            unit = length_units[index]
            number = float(input('enter the length amount: '))
            if number <=0:
                print('distance cant be 0 or negative')
            remaining_list = list(filter(lambda temp: temp != unit, length_units))
            for i, e in enumerate(remaining_list, 1):
                print (i,e)
            index = int(input('\nEnter the unit to convert too: ')) -1
            convert = remaining_list[index]
            result = length_conversion(unit, number, convert)
            print(f"{number} {unit} is equal to {round(result)} {convert}")
        except ValueError:
            print('invalid input try again')
            continue
        except IndexError:
            print('invalid option selected try again')
            continue


def length_conversion(unit, number, convert):
    distance = {
        'inch': {
            'feet':       number / 12,
            'yard':       number / 36,
            'mile':       number / 63360,
            'millimeter': number * 25.4,
            'centimeter': number * 2.54,
            'meter':      number * 0.0254,
            'kilometer':  number * 0.0000254
        },
        'feet': {
            'inch':       number * 12,
            'yard':       number / 3,
            'mile':       number / 5280,
            'millimeter': number * 304.8,
            'centimeter': number * 30.48,
            'meter':      number * 0.3048,
            'kilometer':  number * 0.0003048
        },
        'yard': {
            'inch':       number * 36,
            'feet':       number * 3,
            'mile':       number / 1760,
            'millimeter': number * 914.4,
            'centimeter': number * 91.44,
            'meter':      number * 0.9144,
            'kilometer':  number * 0.0009144
        },
        'mile': {
            'inch':       number * 63360,
            'feet':       number * 5280,
            'yard':       number * 1760,
            'millimeter': number * 1_609_344,
            'centimeter': number * 160934.4,
            'meter':      number * 1609.344,
            'kilometer':  number * 1.60934
        },
        'millimeter': {
            'inch':       number / 25.4,
            'feet':       number / 304.8,
            'yard':       number / 914.4,
            'mile':       number / 1_609_344,
            'centimeter': number / 10,
            'meter':      number / 1000,
            'kilometer':  number / 1_000_000
        },
        'centimeter': {
            'inch':       number / 2.54,
            'feet':       number / 30.48,
            'yard':       number / 91.44,
            'mile':       number / 160934.4,
            'millimeter': number * 10,
            'meter':      number / 100,
            'kilometer':  number / 100000
        },
        'meter': {
            'inch':       number * 39.3701,
            'feet':       number * 3.28084,
            'yard':       number * 1.09361,
            'mile':       number / 1609.344,
            'millimeter': number * 1000,
            'centimeter': number * 100,
            'kilometer':  number / 1000
        },
        'kilometer': {
            'inch':       number * 39370.1,
            'feet':       number * 3280.84,
            'yard':       number * 1093.61,
            'mile':       number / 1.60934,
            'millimeter': number * 1_000_000,
            'centimeter': number * 100000,
            'meter':      number * 1000
        }
    }
    if unit in distance and convert in distance[unit]:
        return round(distance[unit][convert], 6)


"""Weight"""

weight_units = ["milligrams", "grams", "kilograms", "pounds", "stone", "ounces", "tonnes" ]#,"Quit"

def weight_menu():
    """select the starting unit"""
    while True:
        print('Enter the number to the left of the mesurment to select it or 9 to Exit')
        for i, e in enumerate(weight_units, 1):
            print (i,e)
        try:
            index = int(input('\nWhat is the starting unit?: ')) -1
            if index == 8: # because of the -1 index
                break
            unit = weight_units[index]
            number = float(input('enter the weight amount: '))
            if number <= 0:
                print("Weight cant be 0 or negative")
                continue
            remaining_list = list(filter(lambda temp: temp != unit, weight_units))
            for i, e in enumerate(remaining_list, 1):
                print (i,e)
            index = int(input('\nEnter the unit to convert too: ')) -1
            convert = remaining_list[index]
            result = weight_conversion(unit, number, convert)
            print(f"{number} {unit} is equal to {round(result)} {convert}")
        except ValueError:
            print('invalid input try again')
            continue
        except IndexError:
            print('invalid option selected try again')
            continue

def weight_conversion(unit, number, convert):
    mass = {
        'milligrams': {
            'grams':     number / 1000,
            'kilograms': number / 1_000_000,
            'pounds':    number / 453592,
            'stone':     number / 6_350_293,
            'ounces':    number / 28349.5,
            'tonnes':    number / 1_000_000_000
        },
        'grams': {
            'milligrams': number * 1000,
            'kilograms':  number / 1000,
            'pounds':     number / 453.592,
            'stone':      number / 6350.29,
            'ounces':     number / 28.3495,
            'tonnes':     number / 1_000_000
        },
        'kilograms': {
            'milligrams': number * 1_000_000,
            'grams':      number * 1000,
            'pounds':     number * 2.20462,
            'stone':      number / 6.35029,
            'ounces':     number * 35.274,
            'tonnes':     number / 1000
        },
        'pounds': {
            'milligrams': number * 453592,
            'grams':      number * 453.592,
            'kilograms':  number / 2.20462,
            'stone':      number / 14,
            'ounces':     number * 16,
            'tonnes':     number / 2204.62
        },
        'stone': {
            'milligrams': number * 6_350_293,
            'grams':      number * 6350.29,
            'kilograms':  number * 6.35029,
            'pounds':     number * 14,
            'ounces':     number * 224,
            'tonnes':     number * 0.00635029
        },
        'ounces': {
            'milligrams': number * 28349.5,
            'grams':      number * 28.3495,
            'kilograms':  number / 35.274,
            'pounds':     number / 16,
            'stone':      number / 224,
            'tonnes':     number / 35274
        },
        'tonnes': {
            'milligrams': number * 1_000_000_000,
            'grams':      number * 1_000_000,
            'kilograms':  number * 1000,
            'pounds':     number * 2204.62,
            'stone':      number * 157.473,
            'ounces':     number * 35274
        }
    }
    if unit in mass and convert in mass[unit]:
        return round(mass[unit][convert], 6)

"""Temperature"""

temperature_units = ['celsius', 'fahrenheit', 'kelvin' ]#, "Quit"

def temperature_menu():
    """select the starting unit"""
    while True:
        print('Enter the number to the left of the mesurment to select it or 9 to Exit')
        for i, e in enumerate(temperature_units, 1):
            print (i,e)
        try:
            index = int(input('\nWhat is the starting unit?: ')) -1
            if index == 8: # because of the -1 index
                break
            unit = temperature_units[index]
            number = float(input('enter the temperature number: '))
            remaining_list = list(filter(lambda temp: temp != unit, temperature_units))
            for i, e in enumerate(remaining_list, 1):
                print (i,e)
            index = int(input('\nEnter the unit to convert too: ')) -1
            convert = remaining_list[index]
            result = temperature_conversion(unit, number, convert)
            print(f"{number} {unit} is equal to {round(result)} {convert}")
        except ValueError:
            print('invalid input try again')
            continue
        except IndexError:
            print('invalid option selected try again')
            continue

def temperature_conversion(unit, number, convert):
    temps = {
        'celsius':
            {'fahrenheit': (number * 9/5) + 32 ,
            'kelvin': number + 273.15
            },
        'fahrenheit':
            {'celsius': (number - 32) * 5/9,
            'kelvin':  (number - 32) * 5/9 + 273.15
            },
        'kelvin':
            {'celsius': number - 273.15,
            'fahrenheit':(number - 273.15) * 9/5 + 32}
    }
    if unit in temps and convert in temps[unit]:
        return temps[unit][convert]

"""Main Menu"""

print("Conversion Calculator")
while True:
    try:
        choice = int(input("""What type of units would you like to convert?
        1. Lenght
        2. Weight
        3. Temperature
        Or
        9. To Quit\n"""))
    except ValueError:
        print('Enter the number to the left of the mesurment to select it')
        continue
    if choice == 1:
        length_menu()
        continue
    if choice == 2:
        weight_menu()
        continue
    if choice == 3:
        temperature_menu()
        continue
    if choice == 9:
        break
    else:
        print('Invalid selection its 1,2,3 and 9')
        continue






















