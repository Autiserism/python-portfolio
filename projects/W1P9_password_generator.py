#Ask the user how long they want the password.
#Randomly pick characters from a string of letters,
#numbers and special characters. Print the generated password.



# import random

# string_char = 'abcde...ABCDE...1234...!@#$'

# define generate_pass(length)
#     gen_pass = ''
#     for i in range(length)
#         gen_pass = gen_pass + random.choice(string_char)
#     return gen_pass

# while True
#     ask for password length, convert to int
#     if length < 8 print error and continue
#     else break

# print generate_pass(length)



import random
string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
def generate_pass (length):
    gen_pass = ''
    for i in range(length):
        gen_pass = gen_pass + random.choice(string_char)
    return gen_pass

while True:
    length = int(input('Enter A Password Length: '))
    if length < 8 :
        print('Password must be atleast 8 characters')
        continue
    else:
        break

while True:
    print(generate_pass(length))
    if input("Generate another? yes or no: ") != 'yes':
        break












