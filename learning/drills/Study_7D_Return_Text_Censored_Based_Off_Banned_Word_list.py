'''Write a function called censor that takes a string and a list of banned words, replaces every banned word with *** and returns the censored string.
Test it with:
text = "the quick brown fox jumps over the lazy dog"
banned = ["fox", "lazy"]
Expected output: "the quick brown *** jumps over the *** dog" '''

text = "the quick Brown fox jumps over the lazy dog"
banned = ["fox", "lazy"]
def censor(text, banned):
    censored = []
    text = text.split()
    for word in text:
        if word not in banned:
            censored.append(word)
        else:
            censored.append('***')
    return ' '.join(censored)
result = censor(text, banned)
print(result)
