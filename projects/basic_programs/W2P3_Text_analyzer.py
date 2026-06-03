'''
Ask the user to type or paste a paragraph.
Count total words, unique words,
average word length,
longest word and most common word.
Display a formatted report.
'''


def word_count (text_split):
    return len(text_split)

def unique_word_count (text_split):
    return len(set(text_split))

def words_appearing_once(text_split):
    counts = {}
    for word in text_split:
        counts.setdefault(word, 0)
        counts[word] += 1
    once = []
    for word, num in counts.items():
        if num == 1:
            once.append(word)
    return once

def av_word_len (text_split):
    lengths = []
    for word in text_split:
        lengths.append(len(word))
    return sum(lengths) / len(lengths)

def longest_word(text_split):
    longest = text_split[0]
    for word in text_split:
        if len(word) > len(longest):
            longest = word
    return longest


def most_common_word(text_split):
    counts = {}
    for word in text_split:
        counts.setdefault(word, 0)
        counts[word] +=1
    most_common = ''
    highest = 0
    for word, count in counts.items():
        if count > highest:
            highest = count
            most_common = word
    return most_common, highest



pasted_text = input('paste a paragraph: ')
text_split = pasted_text.lower().split()

total = word_count(text_split)
unique = unique_word_count(text_split)
once = words_appearing_once(text_split)
average = av_word_len(text_split)
longest = longest_word(text_split)
common_word, common_count = most_common_word(text_split)


print(f"Total word count = {total}")
print(f"Unique words = {unique}")
print(f"Words that only appeard once \n{once}")
print(f"The average word length was \n{average} characters ")
print(f"The longest word was {longest} at {len(longest)} characters")
print(f"The most common word was \n{common_word} \nappearing \n{common_count} times")




# define word_count(text_split)
#     return len(text_split)  # len() does the counting automatically

# define unique_word_count(text_split)
#     return len(set(text_split))  # set() removes duplicates automatically

# define words_appearing_once(text_split)
#     counts = {}
#     for word in text_split
#         counts.setdefault(word, 0)
#         counts[word] += 1
#     once = []
#     for word, count in counts.items()
#         if count == 1
#             once.append(word)
#     return once

# define av_word_len(text_split)
#     lengths = []
#     for word in text_split
#         lengths.append(len(word))
#     return sum(lengths) / len(lengths)

# define longest_word(text_split)
#     longest = text_split[0]
#     for word in text_split
#         if len(word) > len(longest)
#             longest = word
#     return longest

# define most_common_word(text_split)
#     counts = {}
#     for word in text_split
#         counts.setdefault(word, 0)
#         counts[word] += 1
#     most_common = ''
#     highest = 0
#     for word, count in counts.items()
#         if count > highest
#             highest = count
#             most_common = word
#     return most_common, highest

# pasted_text = input('paste a paragraph: ')
# text_split = pasted_text.lower().split()

# total = word_count(text_split)
# unique = unique_word_count(text_split)
# once = words_appearing_once(text_split)
# average = av_word_len(text_split)
# longest = longest_word(text_split)
# common_word, common_count = most_common_word(text_split)

# print formatted report






















