#W3P4 — Password Strength Checker W3P4_password_checker.py
#Full password validator using regex.
#Check length, uppercase, lowercase, digits, special characters.
#Give a strength score out of 5. Suggest improvements for anything missing. Log all attempts.
import re, logging

logging.basicConfig(level=logging.DEBUG)
score = 0
checks = [
    (r'[A-Z]', "Needs 1 Uppercase"),
    (r'[a-z]', "Needs 1 Lowercase"),
    (r'\d', "Needs 1 Digit"),
    (r'[!@#$%^&*]', "Needs 1 Special character (!@#$%^&*)"),
    (r'.{8,}', "Needs to be, Minimum 8 characters long")
]
weak_patterns = [
    (r'(.)\1{2,}', "Cant have Repeated characters (aaa, 111)"),
    (r'012|123|234|345|456|567|678|789',"Cant have Sequential numbers (123,234, etc...)"),
    (r'abc|bcd|xyz', "Cant Have Sequential letters (abc,xyz)"),
    (r'password|admin|user|test',"Cant have Common words"),
    (r'qwerty|asdfgh', "Cant have Keyboard patterns (qwerty,asdfgh)")
]
def check_password(password):
    global score
    score = 0
    suggest_fix = []
    if len(password) != (len(''.join(password.split()))):
        suggest_fix.append('Password cant have any spaces')
        return suggest_fix
    for weak, WDesc in weak_patterns:
        pattern = re.search(weak, password)
        if pattern:
            suggest_fix.append(WDesc)
            score -=1
    for check, CDesc in checks:
        pattern = re.search(check, password)
        if pattern:
            score +=1
        else:
            suggest_fix.append(CDesc)
    return suggest_fix

print("""A strong password has atleast:1
Uppercase
Lowercase
Number
Special Character (!@#$%^&*)
============================
Minimum 8 Characters long
Without Common words or Sequenial Characters or easy to guess patterns
""")

while score <5:
    password = input('Enter a strong Password\n')
    logging.debug(f'{len(password)} attempted')
    result = check_password(password)
    if score <=0:
        print("i wouldn't trust you to lock a door")
    if score <5:
        print(f"Strength score:{score}/5 \nYour Password")
        for i in result:
            print(i)
            logging.debug(f"{i}")
        print('try again\n')
print(f'Strength:{score}/5 Stong Password')
logging.debug(f"password passed Checks")



















































































