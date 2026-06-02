'''
Word frequency

Write a program that asks for a paragraph,
builds a word frequency dictionary,
then prints the top 3 most common words in order from most to least common.

Hint — after building the frequency dictionary you can sort it. Here's a new concept:

sorted(counts.items(), key=lambda x: x[1], reverse=True)

This sorts the dictionary items by value in descending order. lambda x: x[1]
means "sort by the second item in each tuple" which is the count.
'''

# get paragraph from user
# lowercase and split into words
# build frequency dictionary
# sort the dictionary by count highest to lowest
# take the first 3 items from the sorted result
# print each one with its count


user_input = 'paste a paragraph the the the dog dog'
text_split = user_input.lower().split()
counts = {}
for word in text_split:
    counts.setdefault(word, 0)
    counts[word] +=1
sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)
top3 = sorted_words[:3]
for word, count in top3:
    print(f'{word}: {count} times')

'''
user_input = 'paste a paragraph the the the dog dog'  # This is the text the program will examine.

text_split = user_input.lower().split()
# lower() makes every letter lowercase so 'Dog' and 'dog' count as the same word.
# split() breaks the sentence into a list of individual words.
# Result:
# ['paste', 'a', 'paragraph', 'the', 'the', 'the', 'dog', 'dog']

counts = {}
# Create an empty dictionary.
# This will store each word and how many times it appears.
# Example shape:
# {'dog': 2, 'the': 3}

for word in text_split:
    # Loop through each word in the list one at a time.

    counts.setdefault(word, 0)
    # If the word is not already in the dictionary, add it with a starting value of 0.
    # If it is already there, do nothing.
    # This prevents an error when we try to add 1 to it.

    counts[word] += 1
    # Increase that word's count by 1 because we just found it again.

sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)
# counts.items() gives pairs like:
# [('paste', 1), ('a', 1), ('paragraph', 1), ('the', 3), ('dog', 2)]
#
# sorted(...) sorts those pairs into order.
# key=lambda x: x[1] tells Python to sort by the second part of each pair, which is the count.
# reverse=True means sort from highest count to lowest count.
#
# Result:
# [('the', 3), ('dog', 2), ('paste', 1), ('a', 1), ('paragraph', 1)]

top3 = sorted_words[:3]
# Take only the first 3 items from the sorted list.
# These are the 3 most common words.
#
# Result:
# [('the', 3), ('dog', 2), ('paste', 1)]

for word, count in top3:
    # Loop through each top result.
    # Each item is a pair like ('the', 3)
    # word gets 'the'
    # count gets 3

    print(f'{word}: {count} times')
    # Print the word and its count in a readable format.
    # Example:
    # the: 3 times


                Output


the: 3 times
dog: 2 times
paste: 1 times
'''




