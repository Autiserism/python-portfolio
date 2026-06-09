'''
M1P1 — Unit Converter
Convert between length, weight, and temperature.
User picks a category, picks the conversion type,
enters a value, gets the result.
Loops so they can keep converting without restarting.
Input validation throughout.
Clean formatted output.
'''
#have option to show all converted units append to a list?
#have a random mesurment option?



"""Length"""

length_units = [ 'inch', 'feet', 'yard', 'mile', 'millimeter', 'centimeter', 'meter', 'kilometer']#, "Quit"

def length_convertion(unit, number , convert):
    distance =[
    {'length' : 'inch', 'feet' : inch to feet conversion },#inch start
    {'length' : 'inch', 'yard' : inch to     conversion},
    {'length' : 'inch', 'mile' : inch to     conversion},
    {'length' : 'inch', 'millimeter' : inch to     conversion},
    {'length' : 'inch', 'centimeter' : inch to     conversion},
    {'length' : 'inch', 'meter' : inch to     conversion},
    {'length' : 'inch', 'kilometer' : inch to     conversion},# inch end
    {'length' : 'feet', 'inch' :  to     conversion}, #feet start
    {'length' : 'feet', 'yard' :  to     conversion},
    {'length' : 'feet', 'mile' :  to     conversion},
    {'length' : 'feet', 'millimeter' :  to     conversion},
    {'length' : 'feet', 'centimeter' :  to     conversion},
    {'length' : 'feet', 'meter' :  to     conversion},
    {'length' : 'feet', 'kilometer' :  to     conversion},#feet end
    {'length' : 'yard', 'inch' :  to     conversion}, #yard start
    {'length' : 'yard', 'feet' :  to feet conversion },
    {'length' : 'yard', 'mile' :  to     conversion},
    {'length' : 'yard', 'millimeter' :  to     conversion},
    {'length' : 'yard', 'centimeter' :  to     conversion},
    {'length' : 'yard', 'meter' :  to     conversion},
    {'length' : 'yard', 'kilometer' :  to     conversion},#yard end
    {'length' : 'mile', 'inch' :  to     conversion},# mile start
    {'length' : 'mile', 'feet' :  to feet conversion },
    {'length' : 'mile', 'yard' :  to     conversion},
    {'length' : 'mile', 'mile' :  to     conversion},
    {'length' : 'mile', 'millimeter' :  to     conversion},
    {'length' : 'mile', 'centimeter' :  to     conversion},
    {'length' : 'mile', 'meter' :  to     conversion},
    {'length' : 'mile', 'kilometer' :  to     conversion},#mile end
    {'length' : 'millimeter', 'inch' :  to     conversion},#millimeter start
    {'length' : 'millimeter', 'feet' :  to feet conversion },
    {'length' : 'millimeter', 'yard' :  to     conversion},
    {'length' : 'millimeter', 'mile' :  to     conversion},
    {'length' : 'millimeter', 'centimeter' :  to     conversion},
    {'length' : 'millimeter', 'meter' :  to     conversion},
    {'length' : 'millimeter', 'kilometer' :  to     conversion},# millimeter end
    {'length' : 'centimeter', 'inch' :  to     conversion},# centimeter start
    {'length' : 'centimeter', 'feet' :  to feet conversion },
    {'length' : 'centimeter', 'yard' :  to     conversion},
    {'length' : 'centimeter', 'mile' :  to     conversion},
    {'length' : 'centimeter', 'millimeter' :  to     conversion},
    {'length' : 'centimeter', 'meter' :  to     conversion},
    {'length' : 'centimeter', 'kilometer' :  to     conversion},# centimeter end
    {'length' : 'meter', 'inch' :  to     conversion},#meter start
    {'length' : 'meter', 'feet' :  to feet conversion },
    {'length' : 'meter', 'yard' :  to     conversion},
    {'length' : 'meter', 'mile' :  to     conversion},
    {'length' : 'meter', 'millimeter' :  to     conversion},
    {'length' : 'meter', 'centimeter' :  to     conversion},
    {'length' : 'meter', 'kilometer' :  to     conversion},#meter end
    {'length' : 'kilometer', 'inch' :  to     conversion},# kilometer start
    {'length' : 'kilometer', 'feet' :  to feet conversion },
    {'length' : 'kilometer', 'yard' :  to     conversion},
    {'length' : 'kilometer', 'mile' :  to     conversion},
    {'length' : 'kilometer', 'millimeter' :  to     conversion},
    {'length' : 'kilometer', 'centimeter' :  to     conversion},
    {'length' : 'kilometer', 'meter' :  to     conversion}#kilometer end
    ]
    for item in distance:
        if item['length'] == unit and item[convert]:
            return item[convert]





"""Weight"""

weight_units = ["milligrams", "grams", "kilograms", "pounds", "stone", "ounces", "tonnes" ]#,"Quit"

def weight_conversion(unit, number , convert):
    mass = [
    {'weight' : 'milligrams', 'grams' :  to  conversion },#milligrams start
    {'weight' : 'milligrams', 'kilograms' :  to  conversion },
    {'weight' : 'milligrams', 'pounds' :  to  conversion },
    {'weight' : 'milligrams', 'stone' :  to  conversion },
    {'weight' : 'milligrams', 'ounces' :  to  conversion },
    {'weight' : 'milligrams', 'tonnes' :  to  conversion },#milligrams end
    {'weight' : 'grams', 'milligrams' :  to  conversion },#grams start
    {'weight' : 'grams', 'kilograms' :  to  conversion },
    {'weight' : 'grams', 'pounds' :  to  conversion },
    {'weight' : 'grams', 'stone' :  to  conversion },
    {'weight' : 'grams', 'ounces' :  to  conversion },
    {'weight' : 'grams', 'tonnes' :  to  conversion },#grams end
    {'weight' : 'kilograms', 'milligrams' :  to  conversion },#kilograms start
    {'weight' : 'kilograms', 'grams' :  to  conversion },
    {'weight' : 'kilograms', 'pounds' :  to  conversion },
    {'weight' : 'kilograms', 'stone' :  to  conversion },
    {'weight' : 'kilograms', 'ounces' :  to  conversion },
    {'weight' : 'kilograms', 'tonnes' :  to  conversion },#kilograms end
    {'weight' : 'pounds', 'milligrams' :  to  conversion },#pounds start
    {'weight' : 'pounds', 'grams' :  to  conversion },
    {'weight' : 'pounds', 'kilograms' :  to  conversion },
    {'weight' : 'pounds', 'stone' :  to  conversion },
    {'weight' : 'pounds', 'ounces' :  to  conversion },
    {'weight' : 'pounds', 'tonnes' :  to  conversion },#pounds end
    {'weight' : 'stone', 'milligrams' :  to  conversion },#stone start
    {'weight' : 'stone', 'grams' :  to  conversion },
    {'weight' : 'stone', 'kilograms' :  to  conversion },
    {'weight' : 'stone', 'pounds' :  to  conversion },
    {'weight' : 'stone', 'ounces' :  to  conversion },
    {'weight' : 'stone', 'tonnes' :  to  conversion },#stone end
    {'weight' : 'ounces', 'milligrams' :  to  conversion },#ounces start
    {'weight' : 'ounces', 'grams' :  to  conversion },
    {'weight' : 'ounces', 'kilograms' :  to  conversion },
    {'weight' : 'ounces', 'pounds' :  to  conversion },
    {'weight' : 'ounces', 'stone' :  to  conversion },
    {'weight' : 'ounces', 'tonnes' :  to  conversion },#ounces end
    {'weight' : 'tonnes', 'milligrams' :  to  conversion },#tonnes start
    {'weight' : 'tonnes', 'grams' :  to  conversion },
    {'weight' : 'tonnes', 'kilograms' :  to  conversion },
    {'weight' : 'tonnes', 'pounds' :  to  conversion },
    {'weight' : 'tonnes', 'stone' :  to  conversion },
    {'weight' : 'tonnes', 'ounces' :  to  conversion }#tonnes end
    ]
    for item in mass:
    if item['weight'] == unit and item[convert]:
        return item[convert]




"""Temperature"""

temperature_units = ['celsius', 'fahrenheit', 'kelvin' ]#, "Quit"

def temperature_conversion(unit, number , convert):
    temps = [
    {'temperature' : 'celsius', 'fahrenheit' :  to  conversion },#celsius start
    {'temperature' : 'celsius', 'kelvin' :  to  conversion },#celsius end
    {'temperature' : 'fahrenheit', 'celsius' :  to  conversion },#fahrenheit start
    {'temperature' : 'fahrenheit', 'kelvin' :  to  conversion },#fahrenheit end
    {'temperature' : 'kelvin', 'celsius' :  to  conversion },#kelvin start
    {'temperature' : 'kelvin', 'fahrenheit' :  to  conversion },#kelvin end
        for item in temps:
    if item['temperature'] == unit and item[convert]:
        return item[convert]

"""Menu Helper"""


print("Conversion Calculator")
def main_menu():
    print()
if choice == length:
    helper = length_units

if choice == weight:
    helper == weight_units
if choice == temperature:
    helper == temperature_units
        while true
        enumerate helper
        select what unit or
        print quit to exit
        unit = helper choice
        if unit == "Quit": 9?
            break
        number = how many
        what to convert it to
        convert = enumerate helper choice
        if unit == convert:
            print same thing
            continue
        if choice == length:
            result = length_convertion(unit, number, convert)
        elif choice == weight:
            result = weight_conversion(unit, number, convert)
        elif choice == temperature_conversion(unit, number, convert)
        print(f"{number} {unit}(s) to {convert}(s) is {result}")
        continue
        '''


    for i in range(len(helper)):
        index = i + 1
        items = helper[i]
        print(f"{index}: {items.ljust(5)}")
    try:
        convert_me = int(input('enter The Number to the left of the unit for conversion : ')) -1
        selected = data_list[convert_me]

        return
    except ValueError:
        print('invalid input')
        return
    except IndexError:
        print('invalid input')
        return


number = float(input("Enter The value: ")

choice = input("enter the starting measurment type")






















