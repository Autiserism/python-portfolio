#Write a for loop that goes through this list and prints only the words that are 4 letters orlonger:
#words = ["cat", "elephant", "dog", "python", "ant", "tiger"]

words = ["cat", "elephant", "dog", "python", "ant", "tiger"]
for word in words:
    if len(word) <= 4:
        continue
    print(word)
