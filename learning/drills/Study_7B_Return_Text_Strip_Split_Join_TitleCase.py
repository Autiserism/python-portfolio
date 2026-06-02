'''Write a function called clean_text that takes a string and:

Strips whitespace from both ends
Replaces all double spaces with single spaces
Returns the cleaned string in title case

Test it with:
python text = "   hello   world   this  is  a  test   "   '''

text = "   hello   world   this  is  a  test   "

def clean_text(text):
    text = text.strip()
    text = text.split()
    text = ' '.join(text)
    return text.title()


result = clean_text(text)
print(result)
