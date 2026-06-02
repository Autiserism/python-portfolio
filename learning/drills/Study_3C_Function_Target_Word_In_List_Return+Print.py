# Write a function called find_word that takes a list of words and a target word as arguments.
# Loop through the list and return "Found it" if the target is in the list,
# otherwise return "Not found". Print the result.
# Test it twice — once with a word that exists, once with a word that doesn't.
# words = ["cat", "elephant", "dog", "python", "tiger"]

words = ["cat", "elephant", "dog", "python", "tiger"]
target = "dog"
def find_word(words, target):
    for word in words:
        if word == target:
            return 'found it'
    return 'not found'
result = find_word(words, target)
print(result)

words = ["cat", "elephant", "dog", "python", "tiger"]
target = "sheep"
def find_word(words, target):
    for word in words:
        if word == target:
            return 'found it'
    return 'not found'
result = find_word(words, target)
print(result)
