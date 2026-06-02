# Write a function called word_count that takes a string,
# counts how many times each word appears
# and returns a dictionary with the word as the key and the count as the value.
# Test it with: text = "the cat sat on the mat the cat"
# Expected output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}
# Hint — you can split a string into a list of words using .split(). "hello world".split() returns ["hello", "world"].

def word_count(text):
    count = {}
    for word in text.split():
        count.setdefault(word, 0)
        count[word] = count[word] + 1
    return count

text = "the cat sat on the mat the cat"
result = word_count(text)
print(result)
