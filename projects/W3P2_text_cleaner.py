'''
W3P2 — Text Cleaner W3P2_text_cleaner.py
Ask user to paste messy text.
Clean it using regex and string methods.
Remove extra spaces, fix capitalization, remove special characters, censor a list of banned words.
Display before and after.
'''
import re

banned = ['world', 'bad', 'test']

def text_scrup(user_text):
    user_text = re.sub(r'[^A-Za-z\s.!?]', '',user_text)
    user_text = user_text.strip()
    user_text = ' '.join(user_text.split())
    user_text = user_text.lower()
    user_text = re.sub(r'(^|[.!?]\s)([a-z])', lambda m: m.group(1) + m.group(2).upper(), user_text)
    user_text = censor(user_text)
    return user_text

def censor(user_text):
    for word in banned:
        user_text = re.sub(rf'\b{word}\b', '*'*len(word), user_text, flags=re.IGNORECASE)
    return user_text
'''
def censor(user_text):
    def replace_word(match):
        return '*' * len(match.group())

    # Build pattern: \b(word1|word2|word3)\b
    pattern = r'\b(' + '|'.join(re.escape(word) for word in banned) + r')\b'
    return re.sub(pattern, replace_word, user_text, flags=re.IGNORECASE)
'''



user_text = "  hELLo!!!   WoRLD???    This  is   bad  badtext...   hELLo WOrLD. hoW ARE yOu? Hello! World? 123... test@#$"
#user_text = input('paste your text: ')
print(f"Before \n{user_text}")
result = text_scrup(user_text)
print(f"After \n{result}")




















