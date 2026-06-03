'''
Ask the user to type a sentence.
Count how many times each word appears
and display the results using a dictionary.
Ignore case.
'''

import re

def word_count(text):
    count = {}
   text = text.lower()
    for word in text.split():
        count.setdefault(word, 0)
        count[word] = count[word] + 1
    return count

text = input('type a sentence: ')
result = word_count(text)
print(result)




'''
sentence = []
dictionary = {}
sentence = input('Type a sentence: ')

def word_count (dictionary):
    sentence = sentence.lower()
    for word in sentence.split():
        dictionary.setdefault(word,0)
        dictionary[word] = dictionary[word]+1
    return dictionary

result = word_count(dictionary)
print(word_count)'''














