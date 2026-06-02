'''
Reusable helper chain
Write three helpers:

find_item(items, name) — finds item by name, returns it or None                                         0

calculate_average(scores) — takes a list of numbers, returns average                                    0

get_rating(average) — returns 'excellent' above 85, 'good' above 70, 'poor' below                       X

Then write a program that stores products as dictionaries with a name and list of review scores.        X

Use all three helpers to find a product, calculate its average review score and print its rating.
'''

products = {'item1': {'scores' : [99, 88, 77, 78, 79, 97]},
'item2':{'scores' : [69, 58, 97, 38, 79, 50]},
'item3':{'scores' : [25, 80, 40, 68, 59, 67]},
}

nuerm = int(sum(products['item2']['scores']) / len(products['item2']['scores']))

print(nuerm)


def find_item(products ,name):
    for item in products:
        if item == name:
            return item
    print('not found')
    return None

def calculate_average(scores):
    ave = sum(scores) / len(scores)
    return int(ave)

def get_rating(ave):
    rating = 'excellent' if ave >= 85 else 'good' if ave >= 70 else 'poor'
    return rating


while True:
    choice = int(input("make a selection \n1 Find item \n2 evaluate item"))
    if choice == 1:
        name = input("enter item: ")
        soup = find_item(products, name)
        if soup is None:
            print('error')
            continue
        print(products[soup])
        continue
    if choice == 2:
        for k in products.keys():
            print(k)
        choice = input('enter item: ')
        noup = find_item(products, choice)
        if noup is None:
            print('no')
            continue
        slizer = calculate_average(products[noup]['scores'])
        zimbe = get_rating(slizer)
        print(f"{noup} {slizer} {zimbe}")

    else:
        print('no')


