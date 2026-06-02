'''
sorted() with lambda
Write a function called rank_items that takes a list of dictionaries each with a name and score key.
Return the list sorted from highest to lowest score. Print the ranked results with position numbers.
Test with:
'''

items = [
    {'name': 'Tyler', 'score': 72},
    {'name': 'Bob', 'score': 91},
    {'name': 'Sarah', 'score': 85},
    {'name': 'Mike', 'score': 68},
    {'name': 'Jess', 'score': 79}
]

def rank_items(items):
    H2L = sorted(items, key=lambda x: x['score'] ,reverse=True)
    for i in H2L:
        print(f"{i['name']} {i['score']}")


rank_items(items)















