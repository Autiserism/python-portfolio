Nested Dictionary Access - Complete Guide
First - Your Dictionary Needs Colons!
# ❌ YOUR SYNTAX - Missing colons after outer keys
stocked_items = {
    'milk' { 'price': 5, 'stock': 10, 'category': 'dairy'},  # ERROR
    'beef' { 'price': 25, 'stock': 8, 'category': 'meat'},   # ERROR
    'rice' { 'price': 4, 'stock': 30, 'category': 'grain'}   # ERROR
}         ^#missing :

# ✅ CORRECT SYNTAX - Colon after each outer key
stocked_items = {
    'milk': { 'price': 5, 'stock': 10, 'category': 'dairy'},
    'beef': { 'price': 25, 'stock': 8, 'category': 'meat'},
    'rice': { 'price': 4, 'stock': 30, 'category': 'grain'}
}

Basic Access Patterns
stocked_items = {
    'milk': {'price': 5, 'stock': 10, 'category': 'dairy'},
    'beef': {'price': 25, 'stock': 8, 'category': 'meat'},
    'rice': {'price': 4, 'stock': 30, 'category': 'grain'}
}

# ✅ Get entire inner dictionary for an item
print(stocked_items['beef'])
# {'price': 25, 'stock': 8, 'category': 'meat'}

# ✅ Get specific value - CHAIN the brackets
print(stocked_items['beef']['price'])  # 25
print(stocked_items['milk']['stock'])  # 10
print(stocked_items['rice']['category'])  # 'grain'

# Visual breakdown:
stocked_items['beef']['price']
       ↓          ↓        ↓
       |          |        └── Get value at 'price' key
       |          └── This returns the inner dict: {'price': 25, 'stock': 8, 'category': 'meat'}
       └── Start here: get value at 'beef' key

Step-by-Step Access
# Breaking it down into steps for clarity

# Step 1: Get the beef dictionary
beef_data = stocked_items['beef']
print(beef_data)  # {'price': 25, 'stock': 8, 'category': 'meat'}

# Step 2: Get the price from that dictionary
beef_price = beef_data['price']
print(beef_price)  # 25


# OR do it all in one line (same result)
beef_price = stocked_items['beef']['price']
print(beef_price)  # 25

User Input Examples
Example 1: Simple Lookup
stocked_items = {
    'milk': {'price': 5, 'stock': 10, 'category': 'dairy'},
    'beef': {'price': 25, 'stock': 8, 'category': 'meat'},
    'rice': {'price': 4, 'stock': 30, 'category': 'grain'}
}

# Get item from user
item = input('Enter item name: ')  # User types: beef

# Access the price
price = stocked_items[item]['price']
print(f'The price of {item} is ${price}')
# The price of beef is $25
Example 2: With Error Handling
# ✅ SAFE - Check if item exists first
item = input('Enter item name: ')  # User might type 'chicken'

if item in stocked_items:
    price = stocked_items[item]['price']
    print(f'The price of {item} is ${price}')
else:
    print(f'Sorry, {item} is not in stock')


# ✅ ALTERNATIVE - Use .get() method
item = input('Enter item name: ')
item_data = stocked_items.get(item)

if item_data:
    price = item_data['price']
    print(f'The price of {item} is ${price}')
else:
    print(f'Sorry, {item} is not in stock')


# ✅ ONE-LINER with .get() and default
item = input('Enter item name: ')
price = stocked_items.get(item, {}).get('price', 'Item not found')
print(f'Price: {price}')
Example 3: Full Item Lookup Program
stocked_items = {
    'milk': {'price': 5, 'stock': 10, 'category': 'dairy'},
    'beef': {'price': 25, 'stock': 8, 'category': 'meat'},
    'rice': {'price': 4, 'stock': 30, 'category': 'grain'}
}

while True:
    print('\n--- Inventory Lookup ---')
    item = input('Enter item name (or "quit" to exit): ').lower()

    if item == 'quit':
        break

    if item in stocked_items:
        data = stocked_items[item]
        print(f'\n{item.upper()}:')
        print(f'  Price: ${data["price"]}')
        print(f'  Stock: {data["stock"]} units')
        print(f'  Category: {data["category"]}')
    else:
        print(f'Sorry, {item} not found in inventory')

Accessing Multiple Values
python# ✅ Get all values for one item
item = 'beef'
price = stocked_items[item]['price']
stock = stocked_items[item]['stock']
category = stocked_items[item]['category']

print(f'{item}: ${price}, {stock} in stock, {category} section')
# beef: $25, 8 in stock, meat section


# ✅ BETTER - Unpack all at once
item = 'beef'
data = stocked_items[item]
print(f"{item}: ${data['price']}, {data['stock']} in stock, {data['category']} section")

Modifying Values with User Input
# ✅ Update stock after purchase
item = input('What item did you sell? ')  # User types: milk
quantity = int(input('How many? '))  # User types: 3

if item in stocked_items:
    stocked_items[item]['stock'] -= quantity
    print(f'Updated stock for {item}: {stocked_items[item]["stock"]} remaining')
else:
    print('Item not found')

# Before: 'milk': {'price': 5, 'stock': 10, 'category': 'dairy'}
# After:  'milk': {'price': 5, 'stock': 7, 'category': 'dairy'}


# ✅ Update price
item = input('Which item price to update? ')
new_price = float(input('New price: '))

if item in stocked_items:
    old_price = stocked_items[item]['price']
    stocked_items[item]['price'] = new_price
    print(f'Updated {item} from ${old_price} to ${new_price}')

User Input - Choose What to Look Up
stocked_items = {
    'milk': {'price': 5, 'stock': 10, 'category': 'dairy'},
    'beef': {'price': 25, 'stock': 8, 'category': 'meat'},
    'rice': {'price': 4, 'stock': 30, 'category': 'grain'}
}

item = input('Enter item name: ')  # milk
field = input('What do you want to know? (price/stock/category): ')  # price

if item in stocked_items:
    if field in stocked_items[item]:
        value = stocked_items[item][field]
        print(f'The {field} of {item} is: {value}')
        # The price of milk is: 5
    else:
        print(f'Invalid field: {field}')
else:
    print(f'Item {item} not found')

Checking If Something Exists
# ✅ Check if item exists
if 'beef' in stocked_items:
    print('We have beef!')

# ✅ Check if specific field exists in an item
if 'beef' in stocked_items and 'price' in stocked_items['beef']:
    print(f"Beef price: ${stocked_items['beef']['price']}")

# ✅ Safe access with multiple checks
item = input('Enter item: ')
if item in stocked_items:
    if 'price' in stocked_items[item]:
        print(f"Price: ${stocked_items[item]['price']}")
    else:
        print('Price not available')
else:
    print('Item not in stock')

Looping Through Nested Dictionary
python# ✅ Loop through all items and their details
for item_name, item_data in stocked_items.items():
    print(f'\n{item_name}:')
    print(f'  Price: ${item_data["price"]}')
    print(f'  Stock: {item_data["stock"]}')
    print(f'  Category: {item_data["category"]}')

# Output:
# milk:
#   Price: $5
#   Stock: 10
#   Category: dairy
# beef:
#   Price: $25
#   Stock: 8
#   Category: meat
# ...etc


# ✅ Loop through and access specific fields
for item_name, item_data in stocked_items.items():
    print(f'{item_name}: ${item_data["price"]}')
# milk: $5
# beef: $25
# rice: $4


# ✅ Find all items in a category
category_search = input('Enter category: ')  # dairy

print(f'Items in {category_search}:')
for item_name, item_data in stocked_items.items():
    if item_data['category'] == category_search:
        print(f'  {item_name}: ${item_data["price"]}')

Practical Examples with User Input
Example: Shopping Program
stocked_items = {
    'milk': {'price': 5, 'stock': 10, 'category': 'dairy'},
    'beef': {'price': 25, 'stock': 8, 'category': 'meat'},
    'rice': {'price': 4, 'stock': 30, 'category': 'grain'}
}

total = 0

while True:
    item = input('What item to buy? (or "done" to finish): ').lower()

    if item == 'done':
        break

    if item not in stocked_items:
        print(f'Sorry, {item} not available')
        continue

    # Check stock
    if stocked_items[item]['stock'] == 0:
        print(f'Sorry, {item} is out of stock')
        continue

    # Get quantity
    quantity = int(input('How many? '))

    if quantity > stocked_items[item]['stock']:
        print(f'Only {stocked_items[item]["stock"]} available')
        continue

    # Process purchase
    item_price = stocked_items[item]['price']
    cost = item_price * quantity
    total += cost
    stocked_items[item]['stock'] -= quantity

    print(f'Added {quantity} {item}(s) for ${cost}')

print(f'\nTotal: ${total}')
Example: Inventory Report
python# Find low stock items
print('LOW STOCK ALERT:')
for item, data in stocked_items.items():
    if data['stock'] < 10:
        print(f'  {item}: only {data["stock"]} left')

# Output:
# LOW STOCK ALERT:
#   beef: only 8 left


# Find expensive items
print('\nEXPENSIVE ITEMS (over $10):')
for item, data in stocked_items.items():
    if data['price'] > 10:
        print(f'  {item}: ${data["price"]}')

# Output:
# EXPENSIVE ITEMS (over $10):
#   beef: $25

Common Access Patterns - Quick Reference
python# Get one specific value
price = stocked_items['beef']['price']

# Get all data for one item
beef_data = stocked_items['beef']

# User input access
item = input('Enter item: ')
price = stocked_items[item]['price']

# Safe user input access
item = input('Enter item: ')
if item in stocked_items:
    price = stocked_items[item]['price']

# Modify a value
stocked_items['milk']['stock'] -= 1

# Add new item
stocked_items['eggs'] = {'price': 3, 'stock': 24, 'category': 'dairy'}

# Loop all items
for name, data in stocked_items.items():
    print(f'{name}: ${data["price"]}')

# Search by field value
for name, data in stocked_items.items():
    if data['category'] == 'dairy':
        print(name)

Error Examples to Avoid
# ❌ Accessing non-existent item
print(stocked_items['chicken']['price'])  # KeyError

# ✅ Fix
if 'chicken' in stocked_items:
    print(stocked_items['chicken']['price'])


# ❌ Accessing non-existent field
print(stocked_items['beef']['color'])  # KeyError

# ✅ Fix
if 'color' in stocked_items['beef']:
    print(stocked_items['beef']['color'])


# ❌ Wrong order of keys
print(stocked_items['price']['beef'])  # KeyError

# ✅ Correct order
print(stocked_items['beef']['price'])


Batch Updates - Multiple Items at Once
Update Same Field Across All Items
stocked_items = {
    'milk': {'price': 5, 'stock': 10, 'category': 'dairy'},
    'beef': {'price': 25, 'stock': 8, 'category': 'meat'},
    'rice': {'price': 4, 'stock': 30, 'category': 'grain'}
}

# ✅ Increase all prices by 10%
for item in stocked_items:
    stocked_items[item]['price'] *= 1.10

print(stocked_items)
# All prices increased by 10%


# ✅ Add 'on_sale' field to all items
for item in stocked_items:
    stocked_items[item]['on_sale'] = False

print(stocked_items['milk'])
# {'price': 5.5, 'stock': 10, 'category': 'dairy', 'on_sale': False}


# ✅ Remove 'category' from all items
for item in stocked_items:
    if 'category' in stocked_items[item]:
        del stocked_items[item]['category']


# ✅ Set all stock to specific amount
new_stock = 50
for item in stocked_items:
    stocked_items[item]['stock'] = new_stock

Update Specific Items Only
python# ✅ Update only items in a list
items_to_update = ['milk', 'rice']
discount = 0.90  # 10% discount

for item in items_to_update:
    if item in stocked_items:
        stocked_items[item]['price'] *= discount
        print(f'Discounted {item}')


# ✅ With user input - select multiple items
print('Available items:', ', '.join(stocked_items.keys()))
items_input = input('Enter items to update (comma-separated): ')  # milk, beef
items_to_update = [item.strip() for item in items_input.split(',')]

new_price = float(input('New price for all selected: '))

for item in items_to_update:
    if item in stocked_items:
        stocked_items[item]['price'] = new_price
        print(f'Updated {item}')
    else:
        print(f'{item} not found')

Update Multiple Fields at Once
python# ✅ Update multiple fields for one item using .update()
stocked_items['milk'].update({
    'price': 6,
    'stock': 20,
    'on_sale': True,
    'supplier': 'Dairy Farm Co.'
})
print(stocked_items['milk'])


# ✅ Update multiple fields for multiple items
updates = {
    'milk': {'price': 6, 'stock': 15},
    'beef': {'price': 28, 'stock': 12},
    'rice': {'price': 5, 'stock': 40}
}

for item, new_data in updates.items():
    if item in stocked_items:
        stocked_items[item].update(new_data)
        print(f'Updated {item}')


# ✅ With user input - batch update
while True:
    item = input('Item to update (or "done"): ')
    if item == 'done':
        break

    if item not in stocked_items:
        print('Item not found')
        continue

    price = input('New price (or press Enter to skip): ')
    stock = input('New stock (or press Enter to skip): ')

    if price:
        stocked_items[item]['price'] = float(price)
    if stock:
        stocked_items[item]['stock'] = int(stock)

    print(f'Updated {item}')

Conditional Updates - Only If Conditions Met
Update Based on Current Value
python# ✅ Increase price only for items under $10
for item, data in stocked_items.items():
    if data['price'] < 10:
        data['price'] *= 1.20  # 20% increase
        print(f'Increased price for {item}')

# Only milk and rice get updated (beef is already $25)


# ✅ Restock only low-stock items
restock_amount = 20

for item, data in stocked_items.items():
    if data['stock'] < 10:
        data['stock'] += restock_amount
        print(f'Restocked {item}: now {data["stock"]} units')


# ✅ Mark expensive items as 'premium'
for item, data in stocked_items.items():
    if data['price'] > 15:
        data['premium'] = True
    else:
        data['premium'] = False

print(stocked_items['beef'])
# {..., 'premium': True}

Update Based on Category
python# ✅ Discount all dairy products
for item, data in stocked_items.items():
    if data['category'] == 'dairy':
        data['price'] *= 0.85  # 15% discount
        data['on_sale'] = True
        print(f'{item} is on sale!')


# ✅ Add supplier based on category
suppliers = {
    'dairy': 'Dairy Farm Co.',
    'meat': 'Butcher Shop',
    'grain': 'Grain Wholesalers'
}

for item, data in stocked_items.items():
    category = data['category']
    if category in suppliers:
        data['supplier'] = suppliers[category]


# ✅ Different markup for different categories
markups = {
    'dairy': 1.05,  # 5% increase
    'meat': 1.15,   # 15% increase
    'grain': 1.08   # 8% increase
}

for item, data in stocked_items.items():
    category = data['category']
    if category in markups:
        old_price = data['price']
        data['price'] *= markups[category]
        print(f'{item}: ${old_price} → ${data["price"]:.2f}')

Update Based on Multiple Conditions
python# ✅ Discount items that are both low-stock AND expensive
for item, data in stocked_items.items():
    if data['stock'] < 10 and data['price'] > 10:
        data['price'] *= 0.90  # 10% off
        data['clearance'] = True
        print(f'{item} marked for clearance')


# ✅ Add 'urgent_restock' flag
for item, data in stocked_items.items():
    if data['stock'] < 5 or data['stock'] == 0:
        data['urgent_restock'] = True
    else:
        data['urgent_restock'] = False


# ✅ Complex condition - high price OR low stock
for item, data in stocked_items.items():
    if data['price'] > 20 or data['stock'] < 10:
        data['manager_review'] = True
        print(f'{item} flagged for manager review')


# ✅ Category-specific stock thresholds
thresholds = {
    'dairy': 15,    # Dairy needs more stock
    'meat': 5,      # Meat can be lower
    'grain': 25     # Grain needs lots
}

for item, data in stocked_items.items():
    category = data['category']
    if category in thresholds:
        if data['stock'] < thresholds[category]:
            data['needs_restock'] = True
            print(f'{item} needs restocking')

Conditional Update with User Input
python# ✅ User sets condition and update
print('Update items based on condition')
field = input('Which field to check? (price/stock/category): ')  # price
operator = input('Condition (>, <, ==): ')  # >
value = input('Value to compare: ')  # 10

# Convert value to correct type
if field == 'stock':
    value = int(value)
elif field == 'price':
    value = float(value)

update_field = input('Which field to update? ')  # on_sale
new_value = input('New value: ')  # True

# Convert new_value if needed
if new_value.lower() == 'true':
    new_value = True
elif new_value.lower() == 'false':
    new_value = False

# Apply conditional update
for item, data in stocked_items.items():
    current_value = data.get(field)

    # Check condition
    condition_met = False
    if operator == '>' and current_value > value:
        condition_met = True
    elif operator == '<' and current_value < value:
        condition_met = True
    elif operator == '==' and current_value == value:
        condition_met = True

    # Update if condition met
    if condition_met:
        data[update_field] = new_value
        print(f'Updated {item}')

Batch Add/Remove Items
Add Multiple Items at Once
python# ✅ Add several new items
new_items = {
    'eggs': {'price': 3, 'stock': 24, 'category': 'dairy'},
    'chicken': {'price': 12, 'stock': 15, 'category': 'meat'},
    'pasta': {'price': 2, 'stock': 50, 'category': 'grain'}
}

stocked_items.update(new_items)
print(f'Added {len(new_items)} new items')


# ✅ Add items from user input
num_items = int(input('How many items to add? '))

for i in range(num_items):
    print(f'\n--- Item #{i+1} ---')
    name = input('Name: ')
    price = float(input('Price: '))
    stock = int(input('Stock: '))
    category = input('Category: ')

    stocked_items[name] = {
        'price': price,
        'stock': stock,
        'category': category
    }

print(f'Added {num_items} items')
Remove Multiple Items
python# ✅ Remove items in a list
items_to_remove = ['milk', 'rice']

for item in items_to_remove:
    if item in stocked_items:
        del stocked_items[item]
        print(f'Removed {item}')


# ✅ Remove all items matching condition (out of stock)
items_to_remove = []

for item, data in stocked_items.items():
    if data['stock'] == 0:
        items_to_remove.append(item)

for item in items_to_remove:
    del stocked_items[item]
    print(f'Removed {item} (out of stock)')


# ✅ Remove all items in a category
category_to_remove = input('Remove all items in category: ')  # dairy

items_to_remove = [
    item for item, data in stocked_items.items()
    if data['category'] == category_to_remove
]

confirm = input(f'Remove {len(items_to_remove)} items? (y/n): ')
if confirm == 'y':
    for item in items_to_remove:
        del stocked_items[item]
    print(f'Removed all {category_to_remove} items')

Complex Batch Operations
Tiered Pricing Update
python# ✅ Different discounts based on price tiers
for item, data in stocked_items.items():
    price = data['price']

    if price > 20:
        discount = 0.85  # 15% off expensive items
    elif price > 10:
        discount = 0.90  # 10% off mid-range
    else:
        discount = 0.95  # 5% off cheap items

    old_price = price
    data['price'] = price * discount
    print(f'{item}: ${old_price:.2f} → ${data["price"]:.2f}')
Bulk Stock Adjustment with Limits
python# ✅ Add stock but cap at maximum
max_stock = 100
add_amount = 20

for item, data in stocked_items.items():
    old_stock = data['stock']
    new_stock = old_stock + add_amount

    # Cap at maximum
    if new_stock > max_stock:
        data['stock'] = max_stock
        print(f'{item}: capped at {max_stock}')
    else:
        data['stock'] = new_stock
        print(f'{item}: {old_stock} → {new_stock}')
Category-Based Field Addition
python# ✅ Add different fields based on category
for item, data in stocked_items.items():
    category = data['category']

    if category == 'dairy':
        data['refrigerated'] = True
        data['expiration_days'] = 7
    elif category == 'meat':
        data['refrigerated'] = True
        data['expiration_days'] = 3
    elif category == 'grain':
        data['refrigerated'] = False
        data['shelf_life_months'] = 12

print(stocked_items['milk'])
# {..., 'refrigerated': True, 'expiration_days': 7}

Conditional Update with Logging
python# ✅ Track what was changed
changes_log = []

for item, data in stocked_items.items():
    old_price = data['price']

    # Apply 10% increase to items under $10
    if old_price < 10:
        new_price = old_price * 1.10
        data['price'] = new_price

        changes_log.append({
            'item': item,
            'field': 'price',
            'old_value': old_price,
            'new_value': new_price,
            'reason': 'Price increase for low-cost items'
        })

# Print change report
print('\n--- CHANGE REPORT ---')
for change in changes_log:
    print(f"{change['item']}: {change['field']} changed from "
          f"${change['old_value']:.2f} to ${change['new_value']:.2f}")
    print(f"  Reason: {change['reason']}\n")

Batch Update Menu System
pythondef batch_update_menu():
    while True:
        print('\n--- BATCH UPDATE MENU ---')
        print('1. Update all prices by percentage')
        print('2. Update all stock levels')
        print('3. Add field to all items')
        print('4. Remove field from all items')
        print('5. Update items by category')
        print('6. Update items by price range')
        print('7. Update items by stock level')
        print('8. Back to main menu')

        choice = input('Choose option: ')

        if choice == '1':
            percent = float(input('Percent change (+10 or -10): '))
            multiplier = 1 + (percent / 100)
            for item in stocked_items:
                stocked_items[item]['price'] *= multiplier
            print(f'All prices changed by {percent}%')

        elif choice == '2':
            change = int(input('Add (+) or subtract (-) amount: '))
            for item in stocked_items:
                stocked_items[item]['stock'] += change
            print(f'All stock levels adjusted by {change}')

        elif choice == '3':
            field = input('Field name to add: ')
            value = input('Value for all items: ')
            for item in stocked_items:
                stocked_items[item][field] = value
            print(f'Added {field} to all items')

        elif choice == '4':
            field = input('Field to remove from all: ')
            count = 0
            for item in stocked_items:
                if field in stocked_items[item]:
                    del stocked_items[item][field]
                    count += 1
            print(f'Removed {field} from {count} items')

        elif choice == '5':
            category = input('Which category: ')
            field = input('Field to update: ')
            value = input('New value: ')
            count = 0
            for item, data in stocked_items.items():
                if data.get('category') == category:
                    data[field] = value
                    count += 1
            print(f'Updated {count} items in {category}')

        elif choice == '6':
            min_price = float(input('Minimum price: '))
            max_price = float(input('Maximum price: '))
            field = input('Field to update: ')
            value = input('New value: ')
            count = 0
            for item, data in stocked_items.items():
                if min_price <= data['price'] <= max_price:
                    data[field] = value
                    count += 1
            print(f'Updated {count} items in price range')

        elif choice == '7':
            threshold = int(input('Stock threshold: '))
            condition = input('Above or below threshold? (above/below): ')
            field = input('Field to update: ')
            value = input('New value: ')
            count = 0
            for item, data in stocked_items.items():
                if condition == 'below' and data['stock'] < threshold:
                    data[field] = value
                    count += 1
                elif condition == 'above' and data['stock'] > threshold:
                    data[field] = value
                    count += 1
            print(f'Updated {count} items')

        elif choice == '8':
            break

# Run it
batch_update_menu()

Quick Reference - Batch & Conditional Patterns
python# ===== BATCH UPDATES =====

# Update all items - same field
for item in stocked_items:
    stocked_items[item]['price'] *= 1.10

# Update specific items
items_list = ['milk', 'beef']
for item in items_list:
    if item in stocked_items:
        stocked_items[item]['on_sale'] = True

# Update multiple fields per item
for item in stocked_items:
    stocked_items[item].update({'field1': value1, 'field2': value2})


# ===== CONDITIONAL UPDATES =====

# By value comparison
for item, data in stocked_items.items():
    if data['price'] > 10:
        data['expensive'] = True

# By category
for item, data in stocked_items.items():
    if data['category'] == 'dairy':
        data['refrigerate'] = True

# Multiple conditions
for item, data in stocked_items.items():
    if data['stock'] < 10 and data['price'] > 5:
        data['reorder'] = True

# Complex tier-based
for item, data in stocked_items.items():
    if data['price'] > 20:
        data['tier'] = 'premium'
    elif data['price'] > 10:
        data['tier'] = 'standard'
    else:
        data['tier'] = 'budget'


