'''
Drill B — Check before access
Write a function called safe_get that takes a dictionary and a key.
If the key exists return the value.
If not print 'key not found' and return None.
Test it with 5 lookups — some valid some not.
'''

safest_gettest ={ 'safer' : {'name' : 'Zinbe', 'type': 'hawktua'}, 'safist' : {'name' : 'Gort', 'type': 'sam hammich'}}

def safe_get(safest_gettest,key):
    if key in safest_gettest:
        return safest_gettest[key]
    else:
        print('the cheese man requires a bigger tax key not found')
        return None



while True:
    key = input("enter key: ")
    result = safe_get(safest_gettest, key)
    if result is not None:
        print(f'Found: {result}')
    if key == '':
        break

'''while True:

    key = input("get safe: ")
    safe_get(safest_gettest,key)
    if key in safest_gettest:
        print(f"your did it {safest_gettest[key]}")
        continue
    else:
        print('\nsafe not are you yet\n- Yoda')
        continue
'''




















