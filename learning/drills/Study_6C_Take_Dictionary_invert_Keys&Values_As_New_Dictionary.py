# Write a function called invert_dict that takes a dictionary
# and returns a new dictionary with the keys and values swapped.
# Test it with: original = {'a': 1, 'b': 2, 'c': 3}
# Expected output: {1: 'a', 2: 'b', 3: 'c'}

original = {'a': 1, 'b': 2, 'c': 3}

def invert_dict(original):
    new = {}
    for v, k in original.items():
       new[k] = v
    return new

inverted = invert_dict(original)
print(inverted)



